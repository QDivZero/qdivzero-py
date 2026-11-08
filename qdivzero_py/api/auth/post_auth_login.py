from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.login_request import LoginRequest
from ...models.login_response import LoginResponse
from ...types import Response


def _get_kwargs(
    *,
    body: LoginRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/auth/login",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | LoginResponse | None:
    if response.status_code == 200:
        response_200 = LoginResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | LoginResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: LoginRequest,
) -> Response[ErrorResponse | LoginResponse]:
    """Authenticate a user

     Authenticates a user with email and password. If verification is required, the JSON response may
    include a next_step. Only successful authentication sets the HTTP-only qdiv0_access and
    qdiv0_refresh browser-session cookies; the JSON response contains no access or refresh token values.

    Args:
        body (LoginRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | LoginResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: LoginRequest,
) -> ErrorResponse | LoginResponse | None:
    """Authenticate a user

     Authenticates a user with email and password. If verification is required, the JSON response may
    include a next_step. Only successful authentication sets the HTTP-only qdiv0_access and
    qdiv0_refresh browser-session cookies; the JSON response contains no access or refresh token values.

    Args:
        body (LoginRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | LoginResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: LoginRequest,
) -> Response[ErrorResponse | LoginResponse]:
    """Authenticate a user

     Authenticates a user with email and password. If verification is required, the JSON response may
    include a next_step. Only successful authentication sets the HTTP-only qdiv0_access and
    qdiv0_refresh browser-session cookies; the JSON response contains no access or refresh token values.

    Args:
        body (LoginRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | LoginResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: LoginRequest,
) -> ErrorResponse | LoginResponse | None:
    """Authenticate a user

     Authenticates a user with email and password. If verification is required, the JSON response may
    include a next_step. Only successful authentication sets the HTTP-only qdiv0_access and
    qdiv0_refresh browser-session cookies; the JSON response contains no access or refresh token values.

    Args:
        body (LoginRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | LoginResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
