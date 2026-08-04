from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    target_group_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/target-groups/{target_group_id}".format(target_group_id=quote(str(target_group_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ErrorResponse | str | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ErrorResponse | str]:
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

) -> Response[Any | ErrorResponse | str]:
    """ Delete a target group

    Args:
        target_group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | str]
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

) -> Any | ErrorResponse | str | None:
    """ Delete a target group

    Args:
        target_group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | str
     """


    return sync_detailed(
        target_group_id=target_group_id,
client=client,

    ).parsed

async def asyncio_detailed(
    target_group_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | ErrorResponse | str]:
    """ Delete a target group

    Args:
        target_group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | str]
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

) -> Any | ErrorResponse | str | None:
    """ Delete a target group

    Args:
        target_group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | str
     """


    return (await asyncio_detailed(
        target_group_id=target_group_id,
client=client,

    )).parsed
