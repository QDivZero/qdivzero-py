"""QDivZero API client (generated from the OpenAPI spec, with an auth wrapper)."""

import httpx

from qdivzero_py.auth import EMPTY_CREDENTIALS, QDivZeroAuth, load_credentials
from qdivzero_py.client import AuthenticatedClient

__all__ = [
    "AuthenticatedClient",
    "QDivZeroAuth",
    "load_credentials",
    "QDivZero",
]


class QDivZero:
    """Token-first client factory for the QDivZero API."""

    def __init__(
        self,
        base_url: str = "https://api.qdiv0.com",
        *,
        api_key: str = "",
        access_token: str = "",
        refresh_token: str = "",
        email: str = "",
        password: str = "",
        load_credentials_file: bool = True,
    ) -> None:
        file = load_credentials() if load_credentials_file else dict(EMPTY_CREDENTIALS)
        self._base_url = base_url
        self._auth = QDivZeroAuth(
            base_url,
            api_key=api_key,
            access_token=access_token or file["access_token"],
            refresh_token=refresh_token or file["refresh_token"],
            email=email or file["email"],
            password=password or file["password"],
        )
        self._client = httpx.Client(base_url=base_url, auth=self._auth)
        self._async_client = httpx.AsyncClient(base_url=base_url, auth=self._auth)

    @property
    def client(self) -> AuthenticatedClient:
        return AuthenticatedClient(base_url=self._base_url, token="").set_httpx_client(self._client)

    @property
    def async_client(self) -> AuthenticatedClient:
        return AuthenticatedClient(base_url=self._base_url, token="").set_async_httpx_client(self._async_client)

    def login(self, email: str, password: str) -> None:
        self._auth.set_credentials(email, password)
        self._auth.login()

    def refresh(self) -> None:
        self._auth.refresh()
