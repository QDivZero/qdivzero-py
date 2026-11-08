from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.debit_balance_request import DebitBalanceRequest
from ...models.debit_balance_response import DebitBalanceResponse
from ...models.error_response import ErrorResponse
from ...models.queued_debit_response import QueuedDebitResponse
from ...types import Response


def _get_kwargs(
    *,
    body: DebitBalanceRequest,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/billing/debit",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DebitBalanceResponse | ErrorResponse | QueuedDebitResponse | str | None:
    if response.status_code == 200:
        response_200 = DebitBalanceResponse.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = QueuedDebitResponse.from_dict(response.json())

        return response_202

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

    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DebitBalanceResponse | ErrorResponse | QueuedDebitResponse | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: DebitBalanceRequest,
    idempotency_key: str,
) -> Response[DebitBalanceResponse | ErrorResponse | QueuedDebitResponse | str]:
    """Debit the current account balance

     Debits a positive amount from the authenticated account.

    Args:
        idempotency_key (str):
        body (DebitBalanceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DebitBalanceResponse | ErrorResponse | QueuedDebitResponse | str]
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
    body: DebitBalanceRequest,
    idempotency_key: str,
) -> DebitBalanceResponse | ErrorResponse | QueuedDebitResponse | str | None:
    """Debit the current account balance

     Debits a positive amount from the authenticated account.

    Args:
        idempotency_key (str):
        body (DebitBalanceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DebitBalanceResponse | ErrorResponse | QueuedDebitResponse | str
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: DebitBalanceRequest,
    idempotency_key: str,
) -> Response[DebitBalanceResponse | ErrorResponse | QueuedDebitResponse | str]:
    """Debit the current account balance

     Debits a positive amount from the authenticated account.

    Args:
        idempotency_key (str):
        body (DebitBalanceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DebitBalanceResponse | ErrorResponse | QueuedDebitResponse | str]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: DebitBalanceRequest,
    idempotency_key: str,
) -> DebitBalanceResponse | ErrorResponse | QueuedDebitResponse | str | None:
    """Debit the current account balance

     Debits a positive amount from the authenticated account.

    Args:
        idempotency_key (str):
        body (DebitBalanceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DebitBalanceResponse | ErrorResponse | QueuedDebitResponse | str
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
