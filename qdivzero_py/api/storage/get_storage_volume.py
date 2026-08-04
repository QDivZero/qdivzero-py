from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.storage_volume_response import StorageVolumeResponse
from ...types import Response


def _get_kwargs(
    volume_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/storage/volumes/{volume_id}".format(volume_id=quote(str(volume_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorResponse | StorageVolumeResponse | None:
    if response.status_code == 200:
        response_200 = StorageVolumeResponse.from_dict(response.json())



        return response_200

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorResponse | StorageVolumeResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    volume_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[ErrorResponse | StorageVolumeResponse]:
    """ Get a storage volume

     Returns details for a specific persistent storage volume.

    Args:
        volume_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | StorageVolumeResponse]
     """


    kwargs = _get_kwargs(
        volume_id=volume_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    volume_id: str,
    *,
    client: AuthenticatedClient,

) -> ErrorResponse | StorageVolumeResponse | None:
    """ Get a storage volume

     Returns details for a specific persistent storage volume.

    Args:
        volume_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | StorageVolumeResponse
     """


    return sync_detailed(
        volume_id=volume_id,
client=client,

    ).parsed

async def asyncio_detailed(
    volume_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[ErrorResponse | StorageVolumeResponse]:
    """ Get a storage volume

     Returns details for a specific persistent storage volume.

    Args:
        volume_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | StorageVolumeResponse]
     """


    kwargs = _get_kwargs(
        volume_id=volume_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    volume_id: str,
    *,
    client: AuthenticatedClient,

) -> ErrorResponse | StorageVolumeResponse | None:
    """ Get a storage volume

     Returns details for a specific persistent storage volume.

    Args:
        volume_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | StorageVolumeResponse
     """


    return (await asyncio_detailed(
        volume_id=volume_id,
client=client,

    )).parsed
