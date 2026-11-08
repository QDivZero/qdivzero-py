from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.firewall_rule_response import FirewallRuleResponse
from ...types import Response


def _get_kwargs(
    rule_slug: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/firewall-rules/{rule_slug}".format(
            rule_slug=quote(str(rule_slug), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | FirewallRuleResponse | None:
    if response.status_code == 200:
        response_200 = FirewallRuleResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | FirewallRuleResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    rule_slug: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | FirewallRuleResponse]:
    """Get a firewall rule

     Returns a single firewall rule by slug.

    Args:
        rule_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | FirewallRuleResponse]
    """

    kwargs = _get_kwargs(
        rule_slug=rule_slug,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    rule_slug: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | FirewallRuleResponse | None:
    """Get a firewall rule

     Returns a single firewall rule by slug.

    Args:
        rule_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | FirewallRuleResponse
    """

    return sync_detailed(
        rule_slug=rule_slug,
        client=client,
    ).parsed


async def asyncio_detailed(
    rule_slug: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | FirewallRuleResponse]:
    """Get a firewall rule

     Returns a single firewall rule by slug.

    Args:
        rule_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | FirewallRuleResponse]
    """

    kwargs = _get_kwargs(
        rule_slug=rule_slug,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    rule_slug: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | FirewallRuleResponse | None:
    """Get a firewall rule

     Returns a single firewall rule by slug.

    Args:
        rule_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | FirewallRuleResponse
    """

    return (
        await asyncio_detailed(
            rule_slug=rule_slug,
            client=client,
        )
    ).parsed
