from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.firewall_evaluation_request import FirewallEvaluationRequest
from ...models.firewall_evaluation_response import FirewallEvaluationResponse
from ...types import Response


def _get_kwargs(
    firewall_slug: str,
    *,
    body: FirewallEvaluationRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/firewalls/{firewall_slug}:evaluate".format(firewall_slug=quote(str(firewall_slug), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorResponse | FirewallEvaluationResponse | None:
    if response.status_code == 200:
        response_200 = FirewallEvaluationResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorResponse | FirewallEvaluationResponse]:
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
    body: FirewallEvaluationRequest,

) -> Response[ErrorResponse | FirewallEvaluationResponse]:
    """ Evaluate a firewall

     Runs input against a firewall and returns the evaluation result.

    Args:
        firewall_slug (str):
        body (FirewallEvaluationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | FirewallEvaluationResponse]
     """


    kwargs = _get_kwargs(
        firewall_slug=firewall_slug,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    firewall_slug: str,
    *,
    client: AuthenticatedClient,
    body: FirewallEvaluationRequest,

) -> ErrorResponse | FirewallEvaluationResponse | None:
    """ Evaluate a firewall

     Runs input against a firewall and returns the evaluation result.

    Args:
        firewall_slug (str):
        body (FirewallEvaluationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | FirewallEvaluationResponse
     """


    return sync_detailed(
        firewall_slug=firewall_slug,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    firewall_slug: str,
    *,
    client: AuthenticatedClient,
    body: FirewallEvaluationRequest,

) -> Response[ErrorResponse | FirewallEvaluationResponse]:
    """ Evaluate a firewall

     Runs input against a firewall and returns the evaluation result.

    Args:
        firewall_slug (str):
        body (FirewallEvaluationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | FirewallEvaluationResponse]
     """


    kwargs = _get_kwargs(
        firewall_slug=firewall_slug,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    firewall_slug: str,
    *,
    client: AuthenticatedClient,
    body: FirewallEvaluationRequest,

) -> ErrorResponse | FirewallEvaluationResponse | None:
    """ Evaluate a firewall

     Runs input against a firewall and returns the evaluation result.

    Args:
        firewall_slug (str):
        body (FirewallEvaluationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | FirewallEvaluationResponse
     """


    return (await asyncio_detailed(
        firewall_slug=firewall_slug,
client=client,
body=body,

    )).parsed
