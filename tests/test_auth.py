import httpx

from qdivzero_py.auth import QDivZeroAuth


def _json_response(status: int, payload: dict) -> httpx.Response:
    return httpx.Response(status, json=payload, request=httpx.Request("GET", "http://test"))


def test_api_key_sent_as_bearer() -> None:
    seen: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request.headers.get("authorization", ""))
        return _json_response(200, {})

    auth = QDivZeroAuth("http://test", api_key="k-123")
    client = httpx.Client(base_url="http://test", transport=httpx.MockTransport(handler), auth=auth)
    client.get("/auth/me")
    assert seen == ["Bearer k-123"]


def test_401_triggers_refresh_and_retry() -> None:
    refresh_calls = 0
    me_calls = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal refresh_calls, me_calls
        if request.url.path == "/auth/refresh":
            refresh_calls += 1
            return _json_response(200, {"access_token": "new-token"})
        if request.url.path == "/auth/me":
            me_calls += 1
            if request.headers.get("authorization") == "Bearer new-token":
                return _json_response(200, {})
            return _json_response(401, {})
        return _json_response(404, {})

    auth = QDivZeroAuth("http://test", access_token="stale", refresh_token="r1")
    client = httpx.Client(base_url="http://test", transport=httpx.MockTransport(handler), auth=auth)
    resp = client.get("/auth/me")
    assert resp.status_code == 200
    assert refresh_calls == 1
    assert me_calls == 2


def test_no_refresh_on_login_failure() -> None:
    refresh_calls = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal refresh_calls
        if request.url.path == "/auth/refresh":
            refresh_calls += 1
            return _json_response(500, {})
        if request.url.path == "/auth/login":
            return _json_response(401, {"error": "bad credentials"})
        return _json_response(404, {})

    auth = QDivZeroAuth("http://test")
    client = httpx.Client(base_url="http://test", transport=httpx.MockTransport(handler), auth=auth)
    resp = client.post("/auth/login", json={"email": "a@b.c", "password": "x"})
    assert resp.status_code == 401
    assert refresh_calls == 0


def test_async_client_refreshes_once() -> None:
    import asyncio

    refresh_calls = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal refresh_calls
        if request.url.path == "/auth/refresh":
            refresh_calls += 1
            return _json_response(200, {"access_token": "new-token"})
        if request.url.path == "/auth/me":
            if request.headers.get("authorization") == "Bearer new-token":
                return _json_response(200, {})
            return _json_response(401, {})
        return _json_response(404, {})

    async def run() -> None:
        auth = QDivZeroAuth("http://test", access_token="stale", refresh_token="r1")
        async with httpx.AsyncClient(base_url="http://test", transport=httpx.MockTransport(handler), auth=auth) as client:
            resp = await client.get("/auth/me")
            assert resp.status_code == 200
            assert refresh_calls == 1

    asyncio.run(run())
