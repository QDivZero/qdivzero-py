from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.post_v1_video_job_files_body import PostV1VideoJobFilesBody
from ...models.post_v1_video_job_json_body import PostV1VideoJobJsonBody
from ...models.service_video_job_result import ServiceVideoJobResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostV1VideoJobJsonBody | PostV1VideoJobFilesBody | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/video-jobs",
    }

    if isinstance(body, PostV1VideoJobJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostV1VideoJobFilesBody):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ServiceVideoJobResult | None:
    if response.status_code == 202:
        response_202 = ServiceVideoJobResult.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ErrorResponse.from_dict(response.json())

        return response_402

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if response.status_code == 413:
        response_413 = ErrorResponse.from_dict(response.json())

        return response_413

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | ServiceVideoJobResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostV1VideoJobJsonBody | PostV1VideoJobFilesBody | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorResponse | ServiceVideoJobResult]:
    """Submit a recoverable video generation job

     Uses the same JSON or multipart fields, validation, defaults and upload limits as POST /v1/videos.
    Generation continues after the client disconnects. Account-scoped Idempotency-Key prevents repeat
    submissions; a reused key with different input returns 409. Successful MP4 results remain
    downloadable for seven days after completion. Poll the returned Location for status and explicitly
    cancel active jobs when needed.

    Args:
        idempotency_key (str | Unset):
        body (PostV1VideoJobJsonBody):
        body (PostV1VideoJobFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ServiceVideoJobResult]
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
    body: PostV1VideoJobJsonBody | PostV1VideoJobFilesBody | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> ErrorResponse | ServiceVideoJobResult | None:
    """Submit a recoverable video generation job

     Uses the same JSON or multipart fields, validation, defaults and upload limits as POST /v1/videos.
    Generation continues after the client disconnects. Account-scoped Idempotency-Key prevents repeat
    submissions; a reused key with different input returns 409. Successful MP4 results remain
    downloadable for seven days after completion. Poll the returned Location for status and explicitly
    cancel active jobs when needed.

    Args:
        idempotency_key (str | Unset):
        body (PostV1VideoJobJsonBody):
        body (PostV1VideoJobFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ServiceVideoJobResult
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostV1VideoJobJsonBody | PostV1VideoJobFilesBody | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorResponse | ServiceVideoJobResult]:
    """Submit a recoverable video generation job

     Uses the same JSON or multipart fields, validation, defaults and upload limits as POST /v1/videos.
    Generation continues after the client disconnects. Account-scoped Idempotency-Key prevents repeat
    submissions; a reused key with different input returns 409. Successful MP4 results remain
    downloadable for seven days after completion. Poll the returned Location for status and explicitly
    cancel active jobs when needed.

    Args:
        idempotency_key (str | Unset):
        body (PostV1VideoJobJsonBody):
        body (PostV1VideoJobFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ServiceVideoJobResult]
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
    body: PostV1VideoJobJsonBody | PostV1VideoJobFilesBody | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> ErrorResponse | ServiceVideoJobResult | None:
    """Submit a recoverable video generation job

     Uses the same JSON or multipart fields, validation, defaults and upload limits as POST /v1/videos.
    Generation continues after the client disconnects. Account-scoped Idempotency-Key prevents repeat
    submissions; a reused key with different input returns 409. Successful MP4 results remain
    downloadable for seven days after completion. Poll the returned Location for status and explicitly
    cancel active jobs when needed.

    Args:
        idempotency_key (str | Unset):
        body (PostV1VideoJobJsonBody):
        body (PostV1VideoJobFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ServiceVideoJobResult
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
