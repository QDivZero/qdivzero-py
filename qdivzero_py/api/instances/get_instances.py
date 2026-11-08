from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.instance_list_response import InstanceListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    state: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["state"] = state

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/instances",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | InstanceListResponse | str | None:
    if response.status_code == 200:
        response_200 = InstanceListResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = cast(str, response.json())
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
) -> Response[ErrorResponse | InstanceListResponse | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    state: str | Unset = UNSET,
) -> Response[ErrorResponse | InstanceListResponse | str]:
    """List inference instances

    Args:
        state (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | InstanceListResponse | str]
    """

    kwargs = _get_kwargs(
        state=state,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    state: str | Unset = UNSET,
) -> ErrorResponse | InstanceListResponse | str | None:
    """List inference instances

    Args:
        state (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | InstanceListResponse | str
    """

    return sync_detailed(
        client=client,
        state=state,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    state: str | Unset = UNSET,
) -> Response[ErrorResponse | InstanceListResponse | str]:
    """List inference instances

    Args:
        state (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | InstanceListResponse | str]
    """

    kwargs = _get_kwargs(
        state=state,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    state: str | Unset = UNSET,
) -> ErrorResponse | InstanceListResponse | str | None:
    """List inference instances

    Args:
        state (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | InstanceListResponse | str
    """

    return (
        await asyncio_detailed(
            client=client,
            state=state,
        )
    ).parsed
