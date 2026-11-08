from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.list_user_variants_response import ListUserVariantsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    locale: str | Unset = UNSET,
    category: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    featured_only: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["locale"] = locale

    params["category"] = category

    params["tag"] = tag

    params["featured_only"] = featured_only

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/templates",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ListUserVariantsResponse | None:
    if response.status_code == 200:
        response_200 = ListUserVariantsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | ListUserVariantsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    locale: str | Unset = UNSET,
    category: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    featured_only: bool | Unset = UNSET,
) -> Response[ErrorResponse | ListUserVariantsResponse]:
    """List template variants

     Lists pre-configured deployment template variants visible to the authenticated user.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        locale (str | Unset):
        category (str | Unset):
        tag (str | Unset):
        featured_only (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ListUserVariantsResponse]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        locale=locale,
        category=category,
        tag=tag,
        featured_only=featured_only,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    locale: str | Unset = UNSET,
    category: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    featured_only: bool | Unset = UNSET,
) -> ErrorResponse | ListUserVariantsResponse | None:
    """List template variants

     Lists pre-configured deployment template variants visible to the authenticated user.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        locale (str | Unset):
        category (str | Unset):
        tag (str | Unset):
        featured_only (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ListUserVariantsResponse
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        locale=locale,
        category=category,
        tag=tag,
        featured_only=featured_only,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    locale: str | Unset = UNSET,
    category: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    featured_only: bool | Unset = UNSET,
) -> Response[ErrorResponse | ListUserVariantsResponse]:
    """List template variants

     Lists pre-configured deployment template variants visible to the authenticated user.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        locale (str | Unset):
        category (str | Unset):
        tag (str | Unset):
        featured_only (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ListUserVariantsResponse]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        locale=locale,
        category=category,
        tag=tag,
        featured_only=featured_only,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    locale: str | Unset = UNSET,
    category: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    featured_only: bool | Unset = UNSET,
) -> ErrorResponse | ListUserVariantsResponse | None:
    """List template variants

     Lists pre-configured deployment template variants visible to the authenticated user.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        locale (str | Unset):
        category (str | Unset):
        tag (str | Unset):
        featured_only (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ListUserVariantsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            locale=locale,
            category=category,
            tag=tag,
            featured_only=featured_only,
        )
    ).parsed
