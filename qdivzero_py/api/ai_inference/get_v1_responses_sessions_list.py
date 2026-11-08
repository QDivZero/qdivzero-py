from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_v1_responses_sessions_list_response_200 import GetV1ResponsesSessionsListResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    model: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["model"] = model

    params["tag"] = tag

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/responses/sessions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | GetV1ResponsesSessionsListResponse200 | None:
    if response.status_code == 200:
        response_200 = GetV1ResponsesSessionsListResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 502:
        response_502 = ErrorResponse.from_dict(response.json())

        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | GetV1ResponsesSessionsListResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    model: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[ErrorResponse | GetV1ResponsesSessionsListResponse200]:
    """List saved Responses conversations

     Lists the account's stored response snapshots (chat logs) with optional model, tag, limit and cursor
    filters.

    Args:
        model (str | Unset):
        tag (str | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetV1ResponsesSessionsListResponse200]
    """

    kwargs = _get_kwargs(
        model=model,
        tag=tag,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    model: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> ErrorResponse | GetV1ResponsesSessionsListResponse200 | None:
    """List saved Responses conversations

     Lists the account's stored response snapshots (chat logs) with optional model, tag, limit and cursor
    filters.

    Args:
        model (str | Unset):
        tag (str | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetV1ResponsesSessionsListResponse200
    """

    return sync_detailed(
        client=client,
        model=model,
        tag=tag,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    model: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[ErrorResponse | GetV1ResponsesSessionsListResponse200]:
    """List saved Responses conversations

     Lists the account's stored response snapshots (chat logs) with optional model, tag, limit and cursor
    filters.

    Args:
        model (str | Unset):
        tag (str | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetV1ResponsesSessionsListResponse200]
    """

    kwargs = _get_kwargs(
        model=model,
        tag=tag,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    model: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> ErrorResponse | GetV1ResponsesSessionsListResponse200 | None:
    """List saved Responses conversations

     Lists the account's stored response snapshots (chat logs) with optional model, tag, limit and cursor
    filters.

    Args:
        model (str | Unset):
        tag (str | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetV1ResponsesSessionsListResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            model=model,
            tag=tag,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
