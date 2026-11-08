from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.list_notifications_response import ListNotificationsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    since: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    kind: str | Unset = UNSET,
    severity: str | Unset = UNSET,
    include_read: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["since"] = since

    params["limit"] = limit

    params["kind"] = kind

    params["severity"] = severity

    params["include_read"] = include_read

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/notifications",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ListNotificationsResponse | None:
    if response.status_code == 200:
        response_200 = ListNotificationsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | ListNotificationsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    since: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    kind: str | Unset = UNSET,
    severity: str | Unset = UNSET,
    include_read: bool | Unset = UNSET,
) -> Response[ErrorResponse | ListNotificationsResponse]:
    """List notifications

     Returns notifications for the authenticated account, newest first.

    Args:
        since (str | Unset):
        limit (int | Unset):
        kind (str | Unset):
        severity (str | Unset):
        include_read (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ListNotificationsResponse]
    """

    kwargs = _get_kwargs(
        since=since,
        limit=limit,
        kind=kind,
        severity=severity,
        include_read=include_read,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    since: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    kind: str | Unset = UNSET,
    severity: str | Unset = UNSET,
    include_read: bool | Unset = UNSET,
) -> ErrorResponse | ListNotificationsResponse | None:
    """List notifications

     Returns notifications for the authenticated account, newest first.

    Args:
        since (str | Unset):
        limit (int | Unset):
        kind (str | Unset):
        severity (str | Unset):
        include_read (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ListNotificationsResponse
    """

    return sync_detailed(
        client=client,
        since=since,
        limit=limit,
        kind=kind,
        severity=severity,
        include_read=include_read,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    since: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    kind: str | Unset = UNSET,
    severity: str | Unset = UNSET,
    include_read: bool | Unset = UNSET,
) -> Response[ErrorResponse | ListNotificationsResponse]:
    """List notifications

     Returns notifications for the authenticated account, newest first.

    Args:
        since (str | Unset):
        limit (int | Unset):
        kind (str | Unset):
        severity (str | Unset):
        include_read (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ListNotificationsResponse]
    """

    kwargs = _get_kwargs(
        since=since,
        limit=limit,
        kind=kind,
        severity=severity,
        include_read=include_read,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    since: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    kind: str | Unset = UNSET,
    severity: str | Unset = UNSET,
    include_read: bool | Unset = UNSET,
) -> ErrorResponse | ListNotificationsResponse | None:
    """List notifications

     Returns notifications for the authenticated account, newest first.

    Args:
        since (str | Unset):
        limit (int | Unset):
        kind (str | Unset):
        severity (str | Unset):
        include_read (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ListNotificationsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            since=since,
            limit=limit,
            kind=kind,
            severity=severity,
            include_read=include_read,
        )
    ).parsed
