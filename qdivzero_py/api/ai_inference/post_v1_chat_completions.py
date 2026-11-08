from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.chat_request_envelope import ChatRequestEnvelope
from ...models.error_response import ErrorResponse
from ...models.post_v1_chat_completions_response_200 import PostV1ChatCompletionsResponse200
from ...models.post_v1_chat_completions_response_403 import PostV1ChatCompletionsResponse403
from ...types import Response


def _get_kwargs(
    *,
    body: ChatRequestEnvelope,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/chat/completions",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | PostV1ChatCompletionsResponse200 | PostV1ChatCompletionsResponse403 | None:
    if response.status_code == 200:
        response_200 = PostV1ChatCompletionsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostV1ChatCompletionsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 502:
        response_502 = ErrorResponse.from_dict(response.json())

        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | PostV1ChatCompletionsResponse200 | PostV1ChatCompletionsResponse403]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ChatRequestEnvelope,
) -> Response[ErrorResponse | PostV1ChatCompletionsResponse200 | PostV1ChatCompletionsResponse403]:
    r"""OpenAI-compatible chat completions

     Executes a chat completion using a managed instance or public model. Accepts Bearer access tokens or
    API keys. Supports streaming (SSE) when \"stream\": true.

    Args:
        body (ChatRequestEnvelope):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PostV1ChatCompletionsResponse200 | PostV1ChatCompletionsResponse403]
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
    body: ChatRequestEnvelope,
) -> ErrorResponse | PostV1ChatCompletionsResponse200 | PostV1ChatCompletionsResponse403 | None:
    r"""OpenAI-compatible chat completions

     Executes a chat completion using a managed instance or public model. Accepts Bearer access tokens or
    API keys. Supports streaming (SSE) when \"stream\": true.

    Args:
        body (ChatRequestEnvelope):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PostV1ChatCompletionsResponse200 | PostV1ChatCompletionsResponse403
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ChatRequestEnvelope,
) -> Response[ErrorResponse | PostV1ChatCompletionsResponse200 | PostV1ChatCompletionsResponse403]:
    r"""OpenAI-compatible chat completions

     Executes a chat completion using a managed instance or public model. Accepts Bearer access tokens or
    API keys. Supports streaming (SSE) when \"stream\": true.

    Args:
        body (ChatRequestEnvelope):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PostV1ChatCompletionsResponse200 | PostV1ChatCompletionsResponse403]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ChatRequestEnvelope,
) -> ErrorResponse | PostV1ChatCompletionsResponse200 | PostV1ChatCompletionsResponse403 | None:
    r"""OpenAI-compatible chat completions

     Executes a chat completion using a managed instance or public model. Accepts Bearer access tokens or
    API keys. Supports streaming (SSE) when \"stream\": true.

    Args:
        body (ChatRequestEnvelope):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PostV1ChatCompletionsResponse200 | PostV1ChatCompletionsResponse403
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
