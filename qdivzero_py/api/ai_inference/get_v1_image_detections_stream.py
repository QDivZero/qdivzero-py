from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.detection_stream_event import DetectionStreamEvent
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    model: str,
    account_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["model"] = model

    params["account_id"] = account_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/images/detections/stream",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DetectionStreamEvent | ErrorResponse | None:
    if response.status_code == 101:
        response_101 = DetectionStreamEvent.from_dict(response.json())

        return response_101

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DetectionStreamEvent | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    model: str,
    account_id: str | Unset = UNSET,
) -> Response[DetectionStreamEvent | ErrorResponse]:
    """Stream image detection, pose and object tracking over WebSocket

     Upgrades to a WebSocket and sends session.ready with normalized options and max_frame_bytes. Send
    optional session.configure JSON options patches and receive session.configured. Binary messages
    contain one PNG/JPEG image up to 16 MiB, 16384 pixels per side and 40 million pixels total; each
    returns frame.result with increasing frame_id, processing_ms and the existing typed detection result
    including optional pose keypoints. Text controls are limited to 32 KiB. Errors contain type, status,
    optional frame_id and error code/message. One frame executes at a time with at most one pending
    message; overload closes the session. Inference timeout 60 seconds, idle timeout 90 seconds, session
    limit 30 minutes. Browser cookies require a configured allowed Origin; native clients use Bearer API
    keys. account_id is membership-resolved for user credentials and cannot override an account API key.
    Query credentials are not accepted.
    Opt in with session.configure options.tracking=true for ByteTrack. Detections include optional
    positive track_id integers scoped to this connection. Tracking pins frames to the same replica;
    changing inference options resets identities, an empty patch preserves them. Disconnect/reconnect
    starts a new identity space. Tracking state expires after 90 seconds without a processed frame;
    unavailable state or inference errors close the tracking connection after an error event. Still-
    image requests remain stateless.

    Args:
        model (str):
        account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DetectionStreamEvent | ErrorResponse]
    """

    kwargs = _get_kwargs(
        model=model,
        account_id=account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    model: str,
    account_id: str | Unset = UNSET,
) -> DetectionStreamEvent | ErrorResponse | None:
    """Stream image detection, pose and object tracking over WebSocket

     Upgrades to a WebSocket and sends session.ready with normalized options and max_frame_bytes. Send
    optional session.configure JSON options patches and receive session.configured. Binary messages
    contain one PNG/JPEG image up to 16 MiB, 16384 pixels per side and 40 million pixels total; each
    returns frame.result with increasing frame_id, processing_ms and the existing typed detection result
    including optional pose keypoints. Text controls are limited to 32 KiB. Errors contain type, status,
    optional frame_id and error code/message. One frame executes at a time with at most one pending
    message; overload closes the session. Inference timeout 60 seconds, idle timeout 90 seconds, session
    limit 30 minutes. Browser cookies require a configured allowed Origin; native clients use Bearer API
    keys. account_id is membership-resolved for user credentials and cannot override an account API key.
    Query credentials are not accepted.
    Opt in with session.configure options.tracking=true for ByteTrack. Detections include optional
    positive track_id integers scoped to this connection. Tracking pins frames to the same replica;
    changing inference options resets identities, an empty patch preserves them. Disconnect/reconnect
    starts a new identity space. Tracking state expires after 90 seconds without a processed frame;
    unavailable state or inference errors close the tracking connection after an error event. Still-
    image requests remain stateless.

    Args:
        model (str):
        account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DetectionStreamEvent | ErrorResponse
    """

    return sync_detailed(
        client=client,
        model=model,
        account_id=account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    model: str,
    account_id: str | Unset = UNSET,
) -> Response[DetectionStreamEvent | ErrorResponse]:
    """Stream image detection, pose and object tracking over WebSocket

     Upgrades to a WebSocket and sends session.ready with normalized options and max_frame_bytes. Send
    optional session.configure JSON options patches and receive session.configured. Binary messages
    contain one PNG/JPEG image up to 16 MiB, 16384 pixels per side and 40 million pixels total; each
    returns frame.result with increasing frame_id, processing_ms and the existing typed detection result
    including optional pose keypoints. Text controls are limited to 32 KiB. Errors contain type, status,
    optional frame_id and error code/message. One frame executes at a time with at most one pending
    message; overload closes the session. Inference timeout 60 seconds, idle timeout 90 seconds, session
    limit 30 minutes. Browser cookies require a configured allowed Origin; native clients use Bearer API
    keys. account_id is membership-resolved for user credentials and cannot override an account API key.
    Query credentials are not accepted.
    Opt in with session.configure options.tracking=true for ByteTrack. Detections include optional
    positive track_id integers scoped to this connection. Tracking pins frames to the same replica;
    changing inference options resets identities, an empty patch preserves them. Disconnect/reconnect
    starts a new identity space. Tracking state expires after 90 seconds without a processed frame;
    unavailable state or inference errors close the tracking connection after an error event. Still-
    image requests remain stateless.

    Args:
        model (str):
        account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DetectionStreamEvent | ErrorResponse]
    """

    kwargs = _get_kwargs(
        model=model,
        account_id=account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    model: str,
    account_id: str | Unset = UNSET,
) -> DetectionStreamEvent | ErrorResponse | None:
    """Stream image detection, pose and object tracking over WebSocket

     Upgrades to a WebSocket and sends session.ready with normalized options and max_frame_bytes. Send
    optional session.configure JSON options patches and receive session.configured. Binary messages
    contain one PNG/JPEG image up to 16 MiB, 16384 pixels per side and 40 million pixels total; each
    returns frame.result with increasing frame_id, processing_ms and the existing typed detection result
    including optional pose keypoints. Text controls are limited to 32 KiB. Errors contain type, status,
    optional frame_id and error code/message. One frame executes at a time with at most one pending
    message; overload closes the session. Inference timeout 60 seconds, idle timeout 90 seconds, session
    limit 30 minutes. Browser cookies require a configured allowed Origin; native clients use Bearer API
    keys. account_id is membership-resolved for user credentials and cannot override an account API key.
    Query credentials are not accepted.
    Opt in with session.configure options.tracking=true for ByteTrack. Detections include optional
    positive track_id integers scoped to this connection. Tracking pins frames to the same replica;
    changing inference options resets identities, an empty patch preserves them. Disconnect/reconnect
    starts a new identity space. Tracking state expires after 90 seconds without a processed frame;
    unavailable state or inference errors close the tracking connection after an error event. Still-
    image requests remain stateless.

    Args:
        model (str):
        account_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DetectionStreamEvent | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            model=model,
            account_id=account_id,
        )
    ).parsed
