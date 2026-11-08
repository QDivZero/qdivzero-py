from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.execution_forecast_request import ExecutionForecastRequest
from ...models.execution_forecast_response import ExecutionForecastResponse
from ...types import Response


def _get_kwargs(
    *,
    body: ExecutionForecastRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/timeseries/forecasts",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ExecutionForecastResponse | None:
    if response.status_code == 200:
        response_200 = ExecutionForecastResponse.from_dict(response.json())

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

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 413:
        response_413 = ErrorResponse.from_dict(response.json())

        return response_413

    if response.status_code == 415:
        response_415 = ErrorResponse.from_dict(response.json())

        return response_415

    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())

        return response_503

    if response.status_code == 504:
        response_504 = ErrorResponse.from_dict(response.json())

        return response_504

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | ExecutionForecastResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ExecutionForecastRequest,
) -> Response[ErrorResponse | ExecutionForecastResponse]:
    """Forecast channel-major time series

     Account-owned serving name or instance UUID. Horizon 1..1024, 1..32 records, 1..32 channels, context
    1..15360. Input/output budgets are one million numbers; request/response limits are 16/32 MiB.
    Quantiles default true; inference timeout is two minutes after readiness.

    Args:
        body (ExecutionForecastRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ExecutionForecastResponse]
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
    body: ExecutionForecastRequest,
) -> ErrorResponse | ExecutionForecastResponse | None:
    """Forecast channel-major time series

     Account-owned serving name or instance UUID. Horizon 1..1024, 1..32 records, 1..32 channels, context
    1..15360. Input/output budgets are one million numbers; request/response limits are 16/32 MiB.
    Quantiles default true; inference timeout is two minutes after readiness.

    Args:
        body (ExecutionForecastRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ExecutionForecastResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ExecutionForecastRequest,
) -> Response[ErrorResponse | ExecutionForecastResponse]:
    """Forecast channel-major time series

     Account-owned serving name or instance UUID. Horizon 1..1024, 1..32 records, 1..32 channels, context
    1..15360. Input/output budgets are one million numbers; request/response limits are 16/32 MiB.
    Quantiles default true; inference timeout is two minutes after readiness.

    Args:
        body (ExecutionForecastRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ExecutionForecastResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ExecutionForecastRequest,
) -> ErrorResponse | ExecutionForecastResponse | None:
    """Forecast channel-major time series

     Account-owned serving name or instance UUID. Horizon 1..1024, 1..32 records, 1..32 channels, context
    1..15360. Input/output budgets are one million numbers; request/response limits are 16/32 MiB.
    Quantiles default true; inference timeout is two minutes after readiness.

    Args:
        body (ExecutionForecastRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ExecutionForecastResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
