from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.checkout_session_response import CheckoutSessionResponse
from ...models.create_checkout_session_request import CreateCheckoutSessionRequest
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CreateCheckoutSessionRequest,
    idempotency_key: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/billing/checkout",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CheckoutSessionResponse | ErrorResponse | str | None:
    if response.status_code == 200:
        response_200 = CheckoutSessionResponse.from_dict(response.json())



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

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CheckoutSessionResponse | ErrorResponse | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateCheckoutSessionRequest,
    idempotency_key: str,

) -> Response[CheckoutSessionResponse | ErrorResponse | str]:
    """ Create a checkout session

     Creates a billing checkout session for the authenticated account.

    Args:
        idempotency_key (str):
        body (CreateCheckoutSessionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckoutSessionResponse | ErrorResponse | str]
     """


    kwargs = _get_kwargs(
        body=body,
idempotency_key=idempotency_key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: CreateCheckoutSessionRequest,
    idempotency_key: str,

) -> CheckoutSessionResponse | ErrorResponse | str | None:
    """ Create a checkout session

     Creates a billing checkout session for the authenticated account.

    Args:
        idempotency_key (str):
        body (CreateCheckoutSessionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckoutSessionResponse | ErrorResponse | str
     """


    return sync_detailed(
        client=client,
body=body,
idempotency_key=idempotency_key,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateCheckoutSessionRequest,
    idempotency_key: str,

) -> Response[CheckoutSessionResponse | ErrorResponse | str]:
    """ Create a checkout session

     Creates a billing checkout session for the authenticated account.

    Args:
        idempotency_key (str):
        body (CreateCheckoutSessionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckoutSessionResponse | ErrorResponse | str]
     """


    kwargs = _get_kwargs(
        body=body,
idempotency_key=idempotency_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateCheckoutSessionRequest,
    idempotency_key: str,

) -> CheckoutSessionResponse | ErrorResponse | str | None:
    """ Create a checkout session

     Creates a billing checkout session for the authenticated account.

    Args:
        idempotency_key (str):
        body (CreateCheckoutSessionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckoutSessionResponse | ErrorResponse | str
     """


    return (await asyncio_detailed(
        client=client,
body=body,
idempotency_key=idempotency_key,

    )).parsed
