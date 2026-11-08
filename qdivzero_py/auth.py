"""Authentication for the QDivZero API client."""

from __future__ import annotations

import json
import threading
from collections.abc import AsyncIterator, Iterator
from pathlib import Path

import anyio
import httpx

AUTH_ENDPOINTS = ("/auth/login", "/auth/refresh")
EMPTY_CREDENTIALS: dict[str, str] = {
    "email": "",
    "password": "",
    "access_token": "",
    "refresh_token": "",
    "api_key": "",
}


def credentials_path(home: str | None = None) -> Path:
    base = Path(home) if home is not None else Path.home()
    return base / ".qdivzero" / "credentials"


def load_credentials(home: str | None = None) -> dict[str, str]:
    """Load credentials, returning empty values when the file does not exist."""
    try:
        raw = credentials_path(home).read_text()
    except FileNotFoundError:
        return dict(EMPTY_CREDENTIALS)
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"qdivzero: parse credentials: {exc}") from exc
    return {name: str(parsed.get(name, "")) for name in EMPTY_CREDENTIALS}


class _RefreshAttempt:
    def __init__(self) -> None:
        self.done = threading.Event()
        self.error: BaseException | None = None


class _AuthState:
    def __init__(self, base_url: str, **opts: str) -> None:
        self.base_url = base_url.rstrip("/")
        self._origin = httpx.URL(base_url)
        self.api_key = opts.get("api_key", "")
        self.access_token = opts.get("access_token", "")
        self.refresh_token = opts.get("refresh_token", "")
        self.email = opts.get("email", "")
        self.password = opts.get("password", "")
        self._lock = threading.Lock()
        self._attempt: _RefreshAttempt | None = None

    def same_origin(self, url: httpx.URL) -> bool:
        return (url.scheme, url.host, url.port) == (self._origin.scheme, self._origin.host, self._origin.port)

    def apply_auth(self, request: httpx.Request, force: bool = False) -> str:
        if not self.same_origin(request.url):
            return ""
        with self._lock:
            access, refresh, api_key = self.access_token, self.refresh_token, self.api_key
        if force:
            request.headers.pop("authorization", None)
        if "authorization" not in request.headers:
            if access:
                self._set_cookie(request, "qdiv0_access", access)
            elif api_key:
                request.headers["authorization"] = f"Bearer {api_key}"
        if request.url.path.endswith("/auth/refresh") and refresh:
            self._set_cookie(request, "qdiv0_refresh", refresh)
        return access

    @staticmethod
    def _set_cookie(request: httpx.Request, name: str, value: str) -> None:
        parts = [part.strip() for part in request.headers.get("cookie", "").split(";") if part.strip()]
        parts = [part for part in parts if part.partition("=")[0].strip() != name]
        parts.append(f"{name}={value}")
        request.headers["cookie"] = "; ".join(parts)

    def can_refresh(self, url: httpx.URL) -> bool:
        if not self.same_origin(url) or any(url.path.endswith(path) for path in AUTH_ENDPOINTS):
            return False
        with self._lock:
            return bool(self.refresh_token or (self.email and self.password))

    def begin_refresh(self, sent_access: str | None = None) -> tuple[_RefreshAttempt | None, bool]:
        with self._lock:
            if sent_access is not None and self.access_token and self.access_token != sent_access:
                return None, False
            if self._attempt is not None:
                return self._attempt, False
            self._attempt = _RefreshAttempt()
            return self._attempt, True

    def end_refresh(self, attempt: _RefreshAttempt, error: BaseException | None) -> None:
        with self._lock:
            attempt.error = error
            self._attempt = None
            attempt.done.set()

    def build_refresh_request(self, force_login: bool = False) -> httpx.Request:
        with self._lock:
            refresh, email, password = self.refresh_token, self.email, self.password
        if refresh and not force_login:
            return httpx.Request("POST", f"{self.base_url}/v1/auth/refresh", headers={"cookie": f"qdiv0_refresh={refresh}"})
        if email and password:
            return httpx.Request("POST", f"{self.base_url}/v1/auth/login", json={"email": email, "password": password})
        raise RuntimeError("qdivzero: no refresh token or credentials available")

    def apply_refresh_response(self, response: httpx.Response) -> None:
        if response.status_code != 200:
            raise RuntimeError(f"qdivzero: authentication: status {response.status_code}")
        access = response.cookies.get("qdiv0_access")
        refresh = response.cookies.get("qdiv0_refresh")
        if not access or not refresh:
            try:
                step = response.json().get("next_step")
            except (ValueError, AttributeError):
                step = None
            if step:
                raise RuntimeError(f"qdivzero: login: verification required: {step}")
            raise RuntimeError("qdivzero: authentication: missing session cookies")
        with self._lock:
            self.access_token, self.refresh_token = access, refresh

    def refresh_once(self, force_login: bool = False) -> None:
        while True:
            attempt, leader = self.begin_refresh()
            assert attempt is not None
            if leader:
                break
            attempt.done.wait()
            if force_login:
                continue
            if attempt.error:
                raise RuntimeError(f"qdivzero: authentication failed: {attempt.error}") from attempt.error
            return
        try:
            with httpx.Client() as plain:
                self.apply_refresh_response(plain.send(self.build_refresh_request(force_login)))
        except BaseException as exc:
            self.end_refresh(attempt, exc)
            raise
        self.end_refresh(attempt, None)


class QDivZeroAuth(httpx.Auth):
    """Send API keys or session cookies and refresh sessions after a 401."""

    requires_request_body = True

    def __init__(self, base_url: str, **opts: str) -> None:
        super().__init__()
        self._state = _AuthState(base_url, **opts)

    def set_credentials(self, email: str, password: str) -> None:
        with self._state._lock:
            self._state.email, self._state.password = email, password

    def login(self) -> None:
        self._state.refresh_once(force_login=True)

    def refresh(self) -> None:
        self._state.refresh_once()

    def sync_auth_flow(self, request: httpx.Request) -> Iterator[httpx.Request]:
        request.read()
        sent_access = self._state.apply_auth(request)
        response = yield request
        if response.status_code != 401 or not self._state.can_refresh(request.url):
            return
        attempt, leader = self._state.begin_refresh(sent_access)
        if leader:
            assert attempt is not None
            try:
                refresh_response = yield self._state.build_refresh_request()
                refresh_response.read()
                self._state.apply_refresh_response(refresh_response)
            except BaseException as exc:
                self._state.end_refresh(attempt, exc)
                raise
            self._state.end_refresh(attempt, None)
        elif attempt is not None:
            attempt.done.wait()
            if attempt.error:
                raise RuntimeError(f"qdivzero: authentication failed: {attempt.error}") from attempt.error
        retried = self._rebuild_request(request)
        self._state.apply_auth(retried, force=True)
        yield retried

    async def async_auth_flow(self, request: httpx.Request) -> AsyncIterator[httpx.Request]:
        await request.aread()
        sent_access = self._state.apply_auth(request)
        response = yield request
        if response.status_code != 401 or not self._state.can_refresh(request.url):
            return
        attempt, leader = self._state.begin_refresh(sent_access)
        if leader:
            assert attempt is not None
            try:
                refresh_response = yield self._state.build_refresh_request()
                await refresh_response.aread()
                self._state.apply_refresh_response(refresh_response)
            except BaseException as exc:
                self._state.end_refresh(attempt, exc)
                raise
            self._state.end_refresh(attempt, None)
        elif attempt is not None:
            await anyio.to_thread.run_sync(attempt.done.wait, abandon_on_cancel=True)
            if attempt.error:
                raise RuntimeError(f"qdivzero: authentication failed: {attempt.error}") from attempt.error
        retried = self._rebuild_request(request)
        self._state.apply_auth(retried, force=True)
        yield retried

    @staticmethod
    def _rebuild_request(request: httpx.Request) -> httpx.Request:
        return httpx.Request(
            request.method,
            request.url,
            headers=request.headers,
            content=request.content,
            extensions=request.extensions,
        )
