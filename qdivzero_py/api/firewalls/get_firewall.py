from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.firewall_response import FirewallResponse
from ...types import Response


def _get_kwargs(
    firewall_slug: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/firewalls/{firewall_slug}".format(
            firewall_slug=quote(str(firewall_slug), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | FirewallResponse | None:
    if response.status_code == 200:
        response_200 = FirewallResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | FirewallResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    firewall_slug: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | FirewallResponse]:
    """Get a firewall

     Returns a single firewall by slug.

    Args:
        firewall_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | FirewallResponse]
    """

    kwargs = _get_kwargs(
        firewall_slug=firewall_slug,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    firewall_slug: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | FirewallResponse | None:
    """Get a firewall

     Returns a single firewall by slug.

    Args:
        firewall_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | FirewallResponse
    """

    return sync_detailed(
        firewall_slug=firewall_slug,
        client=client,
    ).parsed


async def asyncio_detailed(
    firewall_slug: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | FirewallResponse]:
    """Get a firewall

     Returns a single firewall by slug.

    Args:
        firewall_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | FirewallResponse]
    """

    kwargs = _get_kwargs(
        firewall_slug=firewall_slug,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    firewall_slug: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | FirewallResponse | None:
    """Get a firewall

     Returns a single firewall by slug.

    Args:
        firewall_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | FirewallResponse
    """

    return (
        await asyncio_detailed(
            firewall_slug=firewall_slug,
            client=client,
        )
    ).parsed
