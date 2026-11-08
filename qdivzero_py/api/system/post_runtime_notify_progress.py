from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.post_runtime_notify_progress_response_200 import PostRuntimeNotifyProgressResponse200
from ...models.runtime_progress_request import RuntimeProgressRequest
from ...types import Response


def _get_kwargs(
    *,
    body: RuntimeProgressRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/runtime/notify/progress",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | PostRuntimeNotifyProgressResponse200 | None:
    if response.status_code == 200:
        response_200 = PostRuntimeNotifyProgressResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponse | PostRuntimeNotifyProgressResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RuntimeProgressRequest,
) -> Response[Any | ErrorResponse | PostRuntimeNotifyProgressResponse200]:
    """Report runtime startup progress

     Authenticated runtime-only endpoint. Send attempt_id and phase to advance startup (204). Once per
    launcher boot, send launch_id and phase=preparing_runtime to resolve the current attempt, including
    resumed containers (200). Unknown or stale attempts cannot advance progress. Readiness is verified
    independently.

    Args:
        body (RuntimeProgressRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | PostRuntimeNotifyProgressResponse200]
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
    body: RuntimeProgressRequest,
) -> Any | ErrorResponse | PostRuntimeNotifyProgressResponse200 | None:
    """Report runtime startup progress

     Authenticated runtime-only endpoint. Send attempt_id and phase to advance startup (204). Once per
    launcher boot, send launch_id and phase=preparing_runtime to resolve the current attempt, including
    resumed containers (200). Unknown or stale attempts cannot advance progress. Readiness is verified
    independently.

    Args:
        body (RuntimeProgressRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | PostRuntimeNotifyProgressResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RuntimeProgressRequest,
) -> Response[Any | ErrorResponse | PostRuntimeNotifyProgressResponse200]:
    """Report runtime startup progress

     Authenticated runtime-only endpoint. Send attempt_id and phase to advance startup (204). Once per
    launcher boot, send launch_id and phase=preparing_runtime to resolve the current attempt, including
    resumed containers (200). Unknown or stale attempts cannot advance progress. Readiness is verified
    independently.

    Args:
        body (RuntimeProgressRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | PostRuntimeNotifyProgressResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RuntimeProgressRequest,
) -> Any | ErrorResponse | PostRuntimeNotifyProgressResponse200 | None:
    """Report runtime startup progress

     Authenticated runtime-only endpoint. Send attempt_id and phase to advance startup (204). Once per
    launcher boot, send launch_id and phase=preparing_runtime to resolve the current attempt, including
    resumed containers (200). Unknown or stale attempts cannot advance progress. Readiness is verified
    independently.

    Args:
        body (RuntimeProgressRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | PostRuntimeNotifyProgressResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
