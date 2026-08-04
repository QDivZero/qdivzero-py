from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.target_group_response import TargetGroupResponse
from ...types import Response


def _get_kwargs(
    target_group_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/target-groups/{target_group_id}".format(target_group_id=quote(str(target_group_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorResponse | TargetGroupResponse | str | None:
    if response.status_code == 200:
        response_200 = TargetGroupResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorResponse | TargetGroupResponse | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    target_group_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[ErrorResponse | TargetGroupResponse | str]:
    """ Get a target group

    Args:
        target_group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | TargetGroupResponse | str]
     """


    kwargs = _get_kwargs(
        target_group_id=target_group_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    target_group_id: str,
    *,
    client: AuthenticatedClient,

) -> ErrorResponse | TargetGroupResponse | str | None:
    """ Get a target group

    Args:
        target_group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | TargetGroupResponse | str
     """


    return sync_detailed(
        target_group_id=target_group_id,
client=client,

    ).parsed

async def asyncio_detailed(
    target_group_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[ErrorResponse | TargetGroupResponse | str]:
    """ Get a target group

    Args:
        target_group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | TargetGroupResponse | str]
     """


    kwargs = _get_kwargs(
        target_group_id=target_group_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    target_group_id: str,
    *,
    client: AuthenticatedClient,

) -> ErrorResponse | TargetGroupResponse | str | None:
    """ Get a target group

    Args:
        target_group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | TargetGroupResponse | str
     """


    return (await asyncio_detailed(
        target_group_id=target_group_id,
client=client,

    )).parsed
