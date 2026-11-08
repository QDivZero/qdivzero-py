from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.embeddings_request_envelope import EmbeddingsRequestEnvelope
from ...models.error_response import ErrorResponse
from ...models.post_v1_embeddings_response_200 import PostV1EmbeddingsResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: EmbeddingsRequestEnvelope,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/embeddings",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | PostV1EmbeddingsResponse200 | None:
    if response.status_code == 200:
        response_200 = PostV1EmbeddingsResponse200.from_dict(response.json())

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
) -> Response[ErrorResponse | PostV1EmbeddingsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: EmbeddingsRequestEnvelope,
) -> Response[ErrorResponse | PostV1EmbeddingsResponse200]:
    """OpenAI-compatible embeddings

     Generates embeddings for a text or multimodal input. Accepts Bearer access tokens or API keys.

    Args:
        body (EmbeddingsRequestEnvelope):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PostV1EmbeddingsResponse200]
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
    body: EmbeddingsRequestEnvelope,
) -> ErrorResponse | PostV1EmbeddingsResponse200 | None:
    """OpenAI-compatible embeddings

     Generates embeddings for a text or multimodal input. Accepts Bearer access tokens or API keys.

    Args:
        body (EmbeddingsRequestEnvelope):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PostV1EmbeddingsResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: EmbeddingsRequestEnvelope,
) -> Response[ErrorResponse | PostV1EmbeddingsResponse200]:
    """OpenAI-compatible embeddings

     Generates embeddings for a text or multimodal input. Accepts Bearer access tokens or API keys.

    Args:
        body (EmbeddingsRequestEnvelope):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PostV1EmbeddingsResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: EmbeddingsRequestEnvelope,
) -> ErrorResponse | PostV1EmbeddingsResponse200 | None:
    """OpenAI-compatible embeddings

     Generates embeddings for a text or multimodal input. Accepts Bearer access tokens or API keys.

    Args:
        body (EmbeddingsRequestEnvelope):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PostV1EmbeddingsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
