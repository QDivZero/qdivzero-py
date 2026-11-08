from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.image_detection_output import ImageDetectionOutput
from ...models.post_v1_image_detections_body import PostV1ImageDetectionsBody
from ...types import Response


def _get_kwargs(
    *,
    body: PostV1ImageDetectionsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/images/detections",
    }

    _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ImageDetectionOutput | None:
    if response.status_code == 200:
        response_200 = ImageDetectionOutput.from_dict(response.json())

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

    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | ImageDetectionOutput]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostV1ImageDetectionsBody,
) -> Response[ErrorResponse | ImageDetectionOutput]:
    """Detect objects or pose keypoints in an uploaded image

     Detects objects or estimates poses using an existing serving name or running instance UUID. Pose
    models return boxes with optional keypoints in checkpoint order, each with pixel x/y coordinates and
    optional confidence (0-1). At most 256 keypoints per detection. PNG/JPEG images up to 16 MiB,
    dimensions up to 16384 pixels per side and 40 million pixels total. Accepts Bearer access tokens or
    API keys.

    Args:
        body (PostV1ImageDetectionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ImageDetectionOutput]
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
    body: PostV1ImageDetectionsBody,
) -> ErrorResponse | ImageDetectionOutput | None:
    """Detect objects or pose keypoints in an uploaded image

     Detects objects or estimates poses using an existing serving name or running instance UUID. Pose
    models return boxes with optional keypoints in checkpoint order, each with pixel x/y coordinates and
    optional confidence (0-1). At most 256 keypoints per detection. PNG/JPEG images up to 16 MiB,
    dimensions up to 16384 pixels per side and 40 million pixels total. Accepts Bearer access tokens or
    API keys.

    Args:
        body (PostV1ImageDetectionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ImageDetectionOutput
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostV1ImageDetectionsBody,
) -> Response[ErrorResponse | ImageDetectionOutput]:
    """Detect objects or pose keypoints in an uploaded image

     Detects objects or estimates poses using an existing serving name or running instance UUID. Pose
    models return boxes with optional keypoints in checkpoint order, each with pixel x/y coordinates and
    optional confidence (0-1). At most 256 keypoints per detection. PNG/JPEG images up to 16 MiB,
    dimensions up to 16384 pixels per side and 40 million pixels total. Accepts Bearer access tokens or
    API keys.

    Args:
        body (PostV1ImageDetectionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ImageDetectionOutput]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostV1ImageDetectionsBody,
) -> ErrorResponse | ImageDetectionOutput | None:
    """Detect objects or pose keypoints in an uploaded image

     Detects objects or estimates poses using an existing serving name or running instance UUID. Pose
    models return boxes with optional keypoints in checkpoint order, each with pixel x/y coordinates and
    optional confidence (0-1). At most 256 keypoints per detection. PNG/JPEG images up to 16 MiB,
    dimensions up to 16384 pixels per side and 40 million pixels total. Accepts Bearer access tokens or
    API keys.

    Args:
        body (PostV1ImageDetectionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ImageDetectionOutput
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
