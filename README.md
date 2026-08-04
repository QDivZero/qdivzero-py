<p align="center">
  <img src="assets/qdiv0-mark.png" alt="QDivZero" width="256">
</p>

# qdivzero-py

Python client for the [QDivZero API](https://api.qdiv0.com), generated
from its [OpenAPI specification](https://api.qdiv0.com/openapi).

[![CI](https://github.com/QDivZero/qdivzero-py/actions/workflows/ci.yml/badge.svg)](https://github.com/QDivZero/qdivzero-py/actions/workflows/ci.yml)

## Install

The package is not on PyPI yet; install directly from Git:

```sh
pip install git+https://github.com/QDivZero/qdivzero-py.git@v1.0.0
```

Requires Python >= 3.11 (the generated code uses `StrEnum`). If you use
[uv](https://docs.astral.sh/uv/), the following is recommended:

```sh
uv add git+https://github.com/QDivZero/qdivzero-py.git@v1.0.0
```

## Quick start

```python
from qdivzero_py import QDivZero
from qdivzero_py.api.accounts.get_accounts import sync_detailed

qd = QDivZero(api_key="your-api-key")
response = sync_detailed(client=qd.client)
if response.status_code != 200:
    raise SystemExit(f"get accounts: status {response.status_code}")
for m in getattr(response.parsed, "memberships", None) or []:
    print(f"account={m.account_id} role={m.role}")
```

## Authentication

Tokens come first; the client falls back to API-key, then access-token, then
refresh-token credentials in that order:

- `QDivZero(api_key="...")` sends the API key as `Authorization: Bearer <key>`.
- `QDivZero(access_token="...")` / `QDivZero(refresh_token="...")` pre-configure
  bearer tokens without logging in.
- `qd.login(email, password)` authenticates with credentials and stores the
  access and refresh tokens.
- When a request fails with `401`, the client transparently refreshes the
  access token (using the refresh token, or re-logging in with stored
  credentials) and retries the request once. Concurrent 401s trigger a single
  refresh. This is implemented as an `httpx.Auth` flow.
- `qd.refresh()` forces a token refresh.

## Credentials file

If `~/.qdivzero/credentials` exists, the client loads it automatically on
`QDivZero(...)`. All fields are optional:

```json
{
  "email": "you@example.com",
  "password": "your-password",
  "access_token": "...",
  "refresh_token": "..."
}
```

`email`/`password` enable on-demand login; `access_token`/`refresh_token`
authenticate directly. Explicit constructor options override file values. Pass
`load_credentials_file=False` to disable auto-loading. Keep the file private
(`chmod 600 ~/.qdivzero/credentials`) and never commit it.

## Error handling

Generated operations return an `httpx.Response` wrapper (`Response`) with a
`status_code` and a `parsed` union of the documented response models, an error
union for documented non-2xx statuses (`ErrorResponse`, `str`, ...), or `None`
for undocumented status codes. If `raise_on_unexpected_status` is enabled, an
unexpected status raises `errors.UnexpectedStatus` instead.

## Regeneration

This library is regenerated automatically from the live spec by the update
workflow (daily at 06:00 UTC, or manually via *Actions → update → Run
workflow*). The upstream spec snapshot is committed at `api/openapi.json`, and
generation is driven by `api/opc-config.yaml`.

**`qdivzero_py/` is generated — do not edit it by hand** (only
`qdivzero_py/__init__.py` is hand-written and preserved). A new release tag
(`v1.0.<n>`) is published on every change.

Known limitation: the PDF invoice response of
`GET /billing/payments/{paymentID}/invoice.pdf` is not generated (the operation
only returns the documented error statuses), so use the endpoint directly with
`httpx` if you need the invoice binary.

## Development

```sh
uv sync
uv tool install openapi-python-client==0.29.0
openapi-python-client generate --path api/openapi.json --config api/opc-config.yaml --meta uv --output-path . --overwrite
```

Checks: `uv run ruff check qdivzero_py tests`, `uv run pytest`.
