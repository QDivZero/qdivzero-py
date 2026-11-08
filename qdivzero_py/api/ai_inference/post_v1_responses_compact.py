from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.post_v1_responses_compact_response_200 import PostV1ResponsesCompactResponse200
from ...models.responses_request_envelope import ResponsesRequestEnvelope
from ...types import Response


def _get_kwargs(
    *,
    body: ResponsesRequestEnvelope,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/responses/compact",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | PostV1ResponsesCompactResponse200 | None:
    if response.status_code == 200:
        response_200 = PostV1ResponsesCompactResponse200.from_dict(response.json())

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
) -> Response[ErrorResponse | PostV1ResponsesCompactResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ResponsesRequestEnvelope,
) -> Response[ErrorResponse | PostV1ResponsesCompactResponse200]:
    """Compact a Responses conversation

     Compresses a conversation history into a compact representation for context management. Accepts
    Bearer access tokens or API keys.

    Args:
        body (ResponsesRequestEnvelope):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PostV1ResponsesCompactResponse200]
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
    body: ResponsesRequestEnvelope,
) -> ErrorResponse | PostV1ResponsesCompactResponse200 | None:
    """Compact a Responses conversation

     Compresses a conversation history into a compact representation for context management. Accepts
    Bearer access tokens or API keys.

    Args:
        body (ResponsesRequestEnvelope):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PostV1ResponsesCompactResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ResponsesRequestEnvelope,
) -> Response[ErrorResponse | PostV1ResponsesCompactResponse200]:
    """Compact a Responses conversation

     Compresses a conversation history into a compact representation for context management. Accepts
    Bearer access tokens or API keys.

    Args:
        body (ResponsesRequestEnvelope):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PostV1ResponsesCompactResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ResponsesRequestEnvelope,
) -> ErrorResponse | PostV1ResponsesCompactResponse200 | None:
    """Compact a Responses conversation

     Compresses a conversation history into a compact representation for context management. Accepts
    Bearer access tokens or API keys.

    Args:
        body (ResponsesRequestEnvelope):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PostV1ResponsesCompactResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
