from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_instance_usage_range import GetInstanceUsageRange
from ...models.instance_usage_response import InstanceUsageResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    instance_id: str,
    *,
    range_: GetInstanceUsageRange | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_range_: str | Unset = UNSET
    if not isinstance(range_, Unset):
        json_range_ = range_.value

    params["range"] = json_range_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/instances/{instance_id}/usage".format(
            instance_id=quote(str(instance_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | InstanceUsageResponse | str | None:
    if response.status_code == 200:
        response_200 = InstanceUsageResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = cast(str, response.json())
        return response_401

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | InstanceUsageResponse | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    instance_id: str,
    *,
    client: AuthenticatedClient,
    range_: GetInstanceUsageRange | Unset = UNSET,
) -> Response[ErrorResponse | InstanceUsageResponse | str]:
    """Get an inference instance usage and cost breakdown

    Args:
        instance_id (str):
        range_ (GetInstanceUsageRange | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | InstanceUsageResponse | str]
    """

    kwargs = _get_kwargs(
        instance_id=instance_id,
        range_=range_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    instance_id: str,
    *,
    client: AuthenticatedClient,
    range_: GetInstanceUsageRange | Unset = UNSET,
) -> ErrorResponse | InstanceUsageResponse | str | None:
    """Get an inference instance usage and cost breakdown

    Args:
        instance_id (str):
        range_ (GetInstanceUsageRange | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | InstanceUsageResponse | str
    """

    return sync_detailed(
        instance_id=instance_id,
        client=client,
        range_=range_,
    ).parsed


async def asyncio_detailed(
    instance_id: str,
    *,
    client: AuthenticatedClient,
    range_: GetInstanceUsageRange | Unset = UNSET,
) -> Response[ErrorResponse | InstanceUsageResponse | str]:
    """Get an inference instance usage and cost breakdown

    Args:
        instance_id (str):
        range_ (GetInstanceUsageRange | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | InstanceUsageResponse | str]
    """

    kwargs = _get_kwargs(
        instance_id=instance_id,
        range_=range_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    instance_id: str,
    *,
    client: AuthenticatedClient,
    range_: GetInstanceUsageRange | Unset = UNSET,
) -> ErrorResponse | InstanceUsageResponse | str | None:
    """Get an inference instance usage and cost breakdown

    Args:
        instance_id (str):
        range_ (GetInstanceUsageRange | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | InstanceUsageResponse | str
    """

    return (
        await asyncio_detailed(
            instance_id=instance_id,
            client=client,
            range_=range_,
        )
    ).parsed
