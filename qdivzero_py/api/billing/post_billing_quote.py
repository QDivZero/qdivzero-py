from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.checkout_quote_request import CheckoutQuoteRequest
from ...models.checkout_quote_response import CheckoutQuoteResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CheckoutQuoteRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/billing/quote",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CheckoutQuoteResponse | ErrorResponse | str | None:
    if response.status_code == 200:
        response_200 = CheckoutQuoteResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = cast(str, response.json())
        return response_401

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())



        return response_409

    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())



        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CheckoutQuoteResponse | ErrorResponse | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CheckoutQuoteRequest,

) -> Response[CheckoutQuoteResponse | ErrorResponse | str]:
    """ Quote a checkout total

     Resolves the authenticated account's application-side tax quote without creating Stripe or checkout
    state.

    Args:
        body (CheckoutQuoteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckoutQuoteResponse | ErrorResponse | str]
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
    client: AuthenticatedClient,
    body: CheckoutQuoteRequest,

) -> CheckoutQuoteResponse | ErrorResponse | str | None:
    """ Quote a checkout total

     Resolves the authenticated account's application-side tax quote without creating Stripe or checkout
    state.

    Args:
        body (CheckoutQuoteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckoutQuoteResponse | ErrorResponse | str
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CheckoutQuoteRequest,

) -> Response[CheckoutQuoteResponse | ErrorResponse | str]:
    """ Quote a checkout total

     Resolves the authenticated account's application-side tax quote without creating Stripe or checkout
    state.

    Args:
        body (CheckoutQuoteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckoutQuoteResponse | ErrorResponse | str]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CheckoutQuoteRequest,

) -> CheckoutQuoteResponse | ErrorResponse | str | None:
    """ Quote a checkout total

     Resolves the authenticated account's application-side tax quote without creating Stripe or checkout
    state.

    Args:
        body (CheckoutQuoteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckoutQuoteResponse | ErrorResponse | str
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
