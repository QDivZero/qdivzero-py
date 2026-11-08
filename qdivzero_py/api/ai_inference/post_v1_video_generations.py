from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.post_v1_video_generations_files_body import PostV1VideoGenerationsFilesBody
from ...models.post_v1_video_generations_json_body import PostV1VideoGenerationsJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostV1VideoGenerationsJsonBody | PostV1VideoGenerationsFilesBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/videos",
    }

    if isinstance(body, PostV1VideoGenerationsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostV1VideoGenerationsFilesBody):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorResponse | None:
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ErrorResponse.from_dict(response.json())

        return response_402

    if response.status_code == 413:
        response_413 = ErrorResponse.from_dict(response.json())

        return response_413

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if response.status_code == 502:
        response_502 = ErrorResponse.from_dict(response.json())

        return response_502

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostV1VideoGenerationsJsonBody | PostV1VideoGenerationsFilesBody | Unset = UNSET,
) -> Response[ErrorResponse]:
    """Synchronous video generation

     Generates a video from a prompt and optional image, video, and audio references. Accepts Bearer
    access tokens or API keys. MiniMax-H3 Ref2VA accepts mixed image/video references with optional
    audio, up to nine images, three videos, one audio reference, and twelve references total; audio
    requires at least one image or video. FL2VA accepts up to two images. MiniMax-H3 prompts are limited
    to 7,000 Unicode characters; image references are limited to 30 MiB, video references to 50 MiB,
    audio references to 15 MiB, and the aggregate input-reference plus audio bytes to 64 MiB. HTTP(S)
    audio_reference_url values are limited to 16 KiB; data URLs are limited by the 15 MiB decoded audio
    payload.

    Args:
        body (PostV1VideoGenerationsJsonBody):
        body (PostV1VideoGenerationsFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse]
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
    body: PostV1VideoGenerationsJsonBody | PostV1VideoGenerationsFilesBody | Unset = UNSET,
) -> ErrorResponse | None:
    """Synchronous video generation

     Generates a video from a prompt and optional image, video, and audio references. Accepts Bearer
    access tokens or API keys. MiniMax-H3 Ref2VA accepts mixed image/video references with optional
    audio, up to nine images, three videos, one audio reference, and twelve references total; audio
    requires at least one image or video. FL2VA accepts up to two images. MiniMax-H3 prompts are limited
    to 7,000 Unicode characters; image references are limited to 30 MiB, video references to 50 MiB,
    audio references to 15 MiB, and the aggregate input-reference plus audio bytes to 64 MiB. HTTP(S)
    audio_reference_url values are limited to 16 KiB; data URLs are limited by the 15 MiB decoded audio
    payload.

    Args:
        body (PostV1VideoGenerationsJsonBody):
        body (PostV1VideoGenerationsFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostV1VideoGenerationsJsonBody | PostV1VideoGenerationsFilesBody | Unset = UNSET,
) -> Response[ErrorResponse]:
    """Synchronous video generation

     Generates a video from a prompt and optional image, video, and audio references. Accepts Bearer
    access tokens or API keys. MiniMax-H3 Ref2VA accepts mixed image/video references with optional
    audio, up to nine images, three videos, one audio reference, and twelve references total; audio
    requires at least one image or video. FL2VA accepts up to two images. MiniMax-H3 prompts are limited
    to 7,000 Unicode characters; image references are limited to 30 MiB, video references to 50 MiB,
    audio references to 15 MiB, and the aggregate input-reference plus audio bytes to 64 MiB. HTTP(S)
    audio_reference_url values are limited to 16 KiB; data URLs are limited by the 15 MiB decoded audio
    payload.

    Args:
        body (PostV1VideoGenerationsJsonBody):
        body (PostV1VideoGenerationsFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostV1VideoGenerationsJsonBody | PostV1VideoGenerationsFilesBody | Unset = UNSET,
) -> ErrorResponse | None:
    """Synchronous video generation

     Generates a video from a prompt and optional image, video, and audio references. Accepts Bearer
    access tokens or API keys. MiniMax-H3 Ref2VA accepts mixed image/video references with optional
    audio, up to nine images, three videos, one audio reference, and twelve references total; audio
    requires at least one image or video. FL2VA accepts up to two images. MiniMax-H3 prompts are limited
    to 7,000 Unicode characters; image references are limited to 30 MiB, video references to 50 MiB,
    audio references to 15 MiB, and the aggregate input-reference plus audio bytes to 64 MiB. HTTP(S)
    audio_reference_url values are limited to 16 KiB; data URLs are limited by the 15 MiB decoded audio
    payload.

    Args:
        body (PostV1VideoGenerationsJsonBody):
        body (PostV1VideoGenerationsFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
