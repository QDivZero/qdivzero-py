from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.put_v1_responses_sessions_status_body import PutV1ResponsesSessionsStatusBody
from ...models.put_v1_responses_sessions_status_response_200 import PutV1ResponsesSessionsStatusResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: PutV1ResponsesSessionsStatusBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/responses/sessions/status",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | PutV1ResponsesSessionsStatusResponse200 | None:
    if response.status_code == 200:
        response_200 = PutV1ResponsesSessionsStatusResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 502:
        response_502 = ErrorResponse.from_dict(response.json())

        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | PutV1ResponsesSessionsStatusResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PutV1ResponsesSessionsStatusBody,
) -> Response[ErrorResponse | PutV1ResponsesSessionsStatusResponse200]:
    """Flip the account persistence switch

    Args:
        body (PutV1ResponsesSessionsStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PutV1ResponsesSessionsStatusResponse200]
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
    body: PutV1ResponsesSessionsStatusBody,
) -> ErrorResponse | PutV1ResponsesSessionsStatusResponse200 | None:
    """Flip the account persistence switch

    Args:
        body (PutV1ResponsesSessionsStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PutV1ResponsesSessionsStatusResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PutV1ResponsesSessionsStatusBody,
) -> Response[ErrorResponse | PutV1ResponsesSessionsStatusResponse200]:
    """Flip the account persistence switch

    Args:
        body (PutV1ResponsesSessionsStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PutV1ResponsesSessionsStatusResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PutV1ResponsesSessionsStatusBody,
) -> ErrorResponse | PutV1ResponsesSessionsStatusResponse200 | None:
    """Flip the account persistence switch

    Args:
        body (PutV1ResponsesSessionsStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PutV1ResponsesSessionsStatusResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
