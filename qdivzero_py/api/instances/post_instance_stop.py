from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.instance_response import InstanceResponse
from ...types import Response


def _get_kwargs(
    instance_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/instances/{instance_id}/stop".format(instance_id=quote(str(instance_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorResponse | InstanceResponse | str | None:
    if response.status_code == 200:
        response_200 = InstanceResponse.from_dict(response.json())



        return response_200

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorResponse | InstanceResponse | str]:
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

) -> Response[ErrorResponse | InstanceResponse | str]:
    """ Stop an inference instance

    Args:
        instance_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | InstanceResponse | str]
     """


    kwargs = _get_kwargs(
        instance_id=instance_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    instance_id: str,
    *,
    client: AuthenticatedClient,

) -> ErrorResponse | InstanceResponse | str | None:
    """ Stop an inference instance

    Args:
        instance_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | InstanceResponse | str
     """


    return sync_detailed(
        instance_id=instance_id,
client=client,

    ).parsed

async def asyncio_detailed(
    instance_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[ErrorResponse | InstanceResponse | str]:
    """ Stop an inference instance

    Args:
        instance_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | InstanceResponse | str]
     """


    kwargs = _get_kwargs(
        instance_id=instance_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    instance_id: str,
    *,
    client: AuthenticatedClient,

) -> ErrorResponse | InstanceResponse | str | None:
    """ Stop an inference instance

    Args:
        instance_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | InstanceResponse | str
     """


    return (await asyncio_detailed(
        instance_id=instance_id,
client=client,

    )).parsed
