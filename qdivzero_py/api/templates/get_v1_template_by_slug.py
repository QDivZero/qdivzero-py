from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_template_by_slug_response import GetTemplateBySlugResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    slug: str,
    *,
    locale: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["locale"] = locale

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/templates/by-slug/{slug}".format(
            slug=quote(str(slug), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | GetTemplateBySlugResponse | None:
    if response.status_code == 200:
        response_200 = GetTemplateBySlugResponse.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | GetTemplateBySlugResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    slug: str,
    *,
    client: AuthenticatedClient,
    locale: str | Unset = UNSET,
) -> Response[ErrorResponse | GetTemplateBySlugResponse]:
    """Get a template by slug

     Returns a template variant by its URL slug for the authenticated user.

    Args:
        slug (str):
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetTemplateBySlugResponse]
    """

    kwargs = _get_kwargs(
        slug=slug,
        locale=locale,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    slug: str,
    *,
    client: AuthenticatedClient,
    locale: str | Unset = UNSET,
) -> ErrorResponse | GetTemplateBySlugResponse | None:
    """Get a template by slug

     Returns a template variant by its URL slug for the authenticated user.

    Args:
        slug (str):
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetTemplateBySlugResponse
    """

    return sync_detailed(
        slug=slug,
        client=client,
        locale=locale,
    ).parsed


async def asyncio_detailed(
    slug: str,
    *,
    client: AuthenticatedClient,
    locale: str | Unset = UNSET,
) -> Response[ErrorResponse | GetTemplateBySlugResponse]:
    """Get a template by slug

     Returns a template variant by its URL slug for the authenticated user.

    Args:
        slug (str):
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetTemplateBySlugResponse]
    """

    kwargs = _get_kwargs(
        slug=slug,
        locale=locale,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    slug: str,
    *,
    client: AuthenticatedClient,
    locale: str | Unset = UNSET,
) -> ErrorResponse | GetTemplateBySlugResponse | None:
    """Get a template by slug

     Returns a template variant by its URL slug for the authenticated user.

    Args:
        slug (str):
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetTemplateBySlugResponse
    """

    return (
        await asyncio_detailed(
            slug=slug,
            client=client,
            locale=locale,
        )
    ).parsed
