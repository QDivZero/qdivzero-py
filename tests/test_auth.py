import threading
import time
from concurrent.futures import ThreadPoolExecutor

import httpx
import pytest

from qdivzero_py.auth import QDivZeroAuth


def _json_response(status: int, payload: dict) -> httpx.Response:
    return httpx.Response(status, json=payload, request=httpx.Request("GET", "http://test"))


def _session_response(request: httpx.Request) -> httpx.Response:
    return httpx.Response(
        200,
        json={},
        headers=[
            ("set-cookie", "qdiv0_access=new-token; Path=/"),
            ("set-cookie", "qdiv0_refresh=r2; Path=/v1/auth/refresh"),
        ],
        request=request,
    )


def test_api_key_sent_as_bearer() -> None:
    seen: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request.headers.get("authorization", ""))
        return _json_response(200, {})

    auth = QDivZeroAuth("http://test", api_key="k-123")
    client = httpx.Client(base_url="http://test", transport=httpx.MockTransport(handler), auth=auth)
    client.get("/v1/auth/me")
    assert seen == ["Bearer k-123"]


def test_access_token_uses_session_cookie() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.headers.get("authorization") is None
        assert "qdiv0_access=session-token" in request.headers.get("cookie", "")
        assert "qdiv0_refresh" not in request.headers.get("cookie", "")
        return _json_response(200, {})

    auth = QDivZeroAuth("http://test", access_token="session-token", refresh_token="refresh-token")
    with httpx.Client(base_url="http://test", transport=httpx.MockTransport(handler), auth=auth) as client:
        assert client.get("/v1/auth/me").status_code == 200


def test_refresh_uses_and_rotates_session_cookies() -> None:
    refresh_calls = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal refresh_calls
        if request.url.path == "/v1/auth/refresh":
            refresh_calls += 1
            assert request.headers.get("cookie") == "qdiv0_refresh=r1"
            assert request.content == b""
            return _session_response(request)
        if "qdiv0_access=new-token" in request.headers.get("cookie", ""):
            return _json_response(200, {})
        return _json_response(401, {})

    auth = QDivZeroAuth("http://test", access_token="stale", refresh_token="r1")
    with httpx.Client(base_url="http://test", transport=httpx.MockTransport(handler), auth=auth) as client:
        assert client.get("/v1/auth/me").status_code == 200
    assert refresh_calls == 1
    assert auth._state.refresh_token == "r2"


def test_401_triggers_refresh_and_retry() -> None:
    refresh_calls = 0
    me_calls = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal refresh_calls, me_calls
        if request.url.path == "/v1/auth/refresh":
            refresh_calls += 1
            return _session_response(request)
        if request.url.path == "/v1/auth/me":
            me_calls += 1
            if "qdiv0_access=new-token" in request.headers.get("cookie", ""):
                return _json_response(200, {})
            return _json_response(401, {})
        return _json_response(404, {})

    auth = QDivZeroAuth("http://test", access_token="stale", refresh_token="r1")
    client = httpx.Client(base_url="http://test", transport=httpx.MockTransport(handler), auth=auth)
    resp = client.get("/v1/auth/me")
    assert resp.status_code == 200
    assert refresh_calls == 1
    assert me_calls == 2


def test_no_refresh_on_login_failure() -> None:
    refresh_calls = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal refresh_calls
        if request.url.path == "/v1/auth/refresh":
            refresh_calls += 1
            return _json_response(500, {})
        if request.url.path == "/v1/auth/login":
            return _json_response(401, {"error": "bad credentials"})
        return _json_response(404, {})

    auth = QDivZeroAuth("http://test")
    client = httpx.Client(base_url="http://test", transport=httpx.MockTransport(handler), auth=auth)
    resp = client.post("/v1/auth/login", json={"email": "a@b.c", "password": "x"})
    assert resp.status_code == 401
    assert refresh_calls == 0


def test_async_client_refreshes_once() -> None:
    import asyncio

    refresh_calls = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal refresh_calls
        if request.url.path == "/v1/auth/refresh":
            refresh_calls += 1
            return _session_response(request)
        if request.url.path == "/v1/auth/me":
            if "qdiv0_access=new-token" in request.headers.get("cookie", ""):
                return _json_response(200, {})
            return _json_response(401, {})
        return _json_response(404, {})

    async def run() -> None:
        auth = QDivZeroAuth("http://test", access_token="stale", refresh_token="r1")
        async with httpx.AsyncClient(
            base_url="http://test", transport=httpx.MockTransport(handler), auth=auth
        ) as client:
            resp = await client.get("/v1/auth/me")
            assert resp.status_code == 200
            assert refresh_calls == 1

    asyncio.run(run())


def test_concurrent_requests_share_refresh() -> None:
    barrier = threading.Barrier(2)
    refresh_calls = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal refresh_calls
        if request.url.path == "/v1/auth/refresh":
            refresh_calls += 1
            time.sleep(0.05)
            return _session_response(request)
        if "qdiv0_access=new-token" in request.headers.get("cookie", ""):
            return _json_response(200, {})
        barrier.wait(timeout=5)
        return _json_response(401, {})

    auth = QDivZeroAuth("http://test", access_token="stale", refresh_token="r1")
    with httpx.Client(base_url="http://test", transport=httpx.MockTransport(handler), auth=auth) as client:
        with ThreadPoolExecutor(max_workers=2) as pool:
            results = list(pool.map(lambda _: client.get("/v1/auth/me").status_code, range(2)))
    assert results == [200, 200]
    assert refresh_calls == 1


def test_async_concurrent_requests_share_refresh() -> None:
    import asyncio

    async def run() -> None:
        stale_count = 0
        refresh_calls = 0
        both_started = asyncio.Event()

        async def handler(request: httpx.Request) -> httpx.Response:
            nonlocal stale_count, refresh_calls
            if request.url.path == "/v1/auth/refresh":
                refresh_calls += 1
                await asyncio.sleep(0.05)
                return _session_response(request)
            if "qdiv0_access=new-token" in request.headers.get("cookie", ""):
                return _json_response(200, {})
            stale_count += 1
            if stale_count == 2:
                both_started.set()
            await both_started.wait()
            return _json_response(401, {})

        auth = QDivZeroAuth("http://test", access_token="stale", refresh_token="r1")
        async with httpx.AsyncClient(
            base_url="http://test", transport=httpx.MockTransport(handler), auth=auth
        ) as client:
            responses = await asyncio.wait_for(asyncio.gather(client.get("/v1/auth/me"), client.get("/v1/auth/me")), 5)
        assert [response.status_code for response in responses] == [200, 200]
        assert refresh_calls == 1

    asyncio.run(run())


def test_missing_session_cookie_does_not_replace_session() -> None:
    auth = QDivZeroAuth("http://test", access_token="old-access", refresh_token="old-refresh")
    response = httpx.Response(
        200,
        json={},
        headers={"set-cookie": "qdiv0_access=new-access; Path=/"},
        request=httpx.Request("POST", "http://test/v1/auth/refresh"),
    )
    with pytest.raises(RuntimeError, match="missing session cookies"):
        auth._state.apply_refresh_response(response)
    assert auth._state.access_token == "old-access"
    assert auth._state.refresh_token == "old-refresh"


def test_credentials_are_not_added_to_another_origin() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert "authorization" not in request.headers
        assert "cookie" not in request.headers
        return _json_response(200, {})

    auth = QDivZeroAuth("http://test", access_token="session", refresh_token="refresh", api_key="secret")
    with httpx.Client(transport=httpx.MockTransport(handler), auth=auth) as client:
        assert client.get("http://other/v1/auth/refresh").status_code == 200
