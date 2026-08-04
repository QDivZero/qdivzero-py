"""Token-first authentication for the QDivZero API client."""

from __future__ import annotations

import json
import threading
from collections.abc import Iterator
from pathlib import Path
from typing import Any

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
    """Load ~/.qdivzero/credentials. A missing file yields empty values; a malformed file raises."""
    path = credentials_path(home)
    try:
        raw = path.read_text()
    except FileNotFoundError:
        return dict(EMPTY_CREDENTIALS)
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"qdivzero: parse credentials: {exc}") from exc
    return {
        "email": str(parsed.get("email", "")),
        "password": str(parsed.get("password", "")),
        "access_token": str(parsed.get("access_token", "")),
        "refresh_token": str(parsed.get("refresh_token", "")),
        "api_key": str(parsed.get("api_key", "")),
    }


class _AuthState:
    def __init__(self, base_url: str, **opts: str) -> None:
        self.base_url = base_url.rstrip("/")
        self.api_key = opts.get("api_key", "")
        self.access_token = opts.get("access_token", "")
        self.refresh_token = opts.get("refresh_token", "")
        self.email = opts.get("email", "")
        self.password = opts.get("password", "")
        self._lock = threading.Lock()
        self._refreshing = False

    def apply_auth(self, request: httpx.Request, force: bool = False) -> None:
        if not force and "authorization" in request.headers:
            return
        if self.access_token:
            request.headers["authorization"] = f"Bearer {self.access_token}"
        elif self.api_key:
            request.headers["authorization"] = f"Bearer {self.api_key}"

    def can_refresh(self, path: str) -> bool:
        return path not in AUTH_ENDPOINTS and bool(self.refresh_token or (self.email and self.password))

    def begin_refresh(self) -> bool:
        with self._lock:
            if self._refreshing:
                return False
            self._refreshing = True
            return True

    def end_refresh(self) -> None:
        with self._lock:
            self._refreshing = False

    def build_refresh_request(self) -> httpx.Request:
        if self.refresh_token:
            return httpx.Request("POST", f"{self.base_url}/auth/refresh", json={"refresh_token": self.refresh_token})
        if self.email and self.password:
            return httpx.Request("POST", f"{self.base_url}/auth/login", json={"email": self.email, "password": self.password})
        raise RuntimeError("qdivzero: no refresh token or credentials available")

    def apply_refresh_response(self, response: httpx.Response) -> None:
        if response.status_code >= 400:
            raise RuntimeError(f"qdivzero: refresh: status {response.status_code}")
        payload = response.json()
        token = payload.get("access_token")
        if not token:
            raise RuntimeError("qdivzero: refresh: empty access token")
        self.access_token = token
        if payload.get("refresh_token"):
            self.refresh_token = payload["refresh_token"]

    def refresh_once(self) -> None:
        with self._lock:
            if self._refreshing:
                return
            self._refreshing = True
        try:
            self._do_refresh()
        finally:
            with self._lock:
                self._refreshing = False

    def _do_refresh(self) -> None:
        with httpx.Client() as plain:
            self.apply_refresh_response(plain.send(self.build_refresh_request()))


class QDivZeroAuth(httpx.Auth):
    """httpx.Auth that injects the Authorization header and refreshes once on 401."""

    requires_request_body = True

    def __init__(self, base_url: str, **opts: str) -> None:
        super().__init__()
        self._state = _AuthState(base_url, **opts)

    def set_credentials(self, email: str, password: str) -> None:
        self._state.email = email
        self._state.password = password

    def login(self) -> None:
        self._state.refresh_once()

    def refresh(self) -> None:
        self._state.refresh_once()

    def sync_auth_flow(self, request: httpx.Request) -> Iterator[httpx.Request]:
        self._state.apply_auth(request)
        response = yield request
        if response is not None and response.status_code == 401 and self._state.can_refresh(request.url.path):
            if self._state.begin_refresh():
                try:
                    refresh_response = yield self._state.build_refresh_request()
                    self._state.apply_refresh_response(refresh_response)
                finally:
                    self._state.end_refresh()
            retried = self._rebuild_request(request)
            self._state.apply_auth(retried, force=True)
            retried.read()
            yield retried

    async def async_auth_flow(self, request: httpx.Request) -> Any:
        self._state.apply_auth(request)
        response = yield request
        if response is not None and response.status_code == 401 and self._state.can_refresh(request.url.path):
            if self._state.begin_refresh():
                try:
                    refresh_response = yield self._state.build_refresh_request()
                    self._state.apply_refresh_response(refresh_response)
                finally:
                    self._state.end_refresh()
            retried = self._rebuild_request(request)
            self._state.apply_auth(retried, force=True)
            await retried.aread()
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
