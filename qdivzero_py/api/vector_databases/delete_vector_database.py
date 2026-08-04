from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_vector_database_response_200 import DeleteVectorDatabaseResponse200
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    database_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/flexible-vector-databases/{database_id}".format(database_id=quote(str(database_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteVectorDatabaseResponse200 | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = DeleteVectorDatabaseResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())



        return response_401

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteVectorDatabaseResponse200 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    database_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[DeleteVectorDatabaseResponse200 | ErrorResponse]:
    """ Delete a vector database

     Removes a vector database owned by the authenticated account.

    Args:
        database_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteVectorDatabaseResponse200 | ErrorResponse]
     """


    kwargs = _get_kwargs(
        database_id=database_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    database_id: str,
    *,
    client: AuthenticatedClient,

) -> DeleteVectorDatabaseResponse200 | ErrorResponse | None:
    """ Delete a vector database

     Removes a vector database owned by the authenticated account.

    Args:
        database_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteVectorDatabaseResponse200 | ErrorResponse
     """


    return sync_detailed(
        database_id=database_id,
client=client,

    ).parsed

async def asyncio_detailed(
    database_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[DeleteVectorDatabaseResponse200 | ErrorResponse]:
    """ Delete a vector database

     Removes a vector database owned by the authenticated account.

    Args:
        database_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteVectorDatabaseResponse200 | ErrorResponse]
     """


    kwargs = _get_kwargs(
        database_id=database_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    database_id: str,
    *,
    client: AuthenticatedClient,

) -> DeleteVectorDatabaseResponse200 | ErrorResponse | None:
    """ Delete a vector database

     Removes a vector database owned by the authenticated account.

    Args:
        database_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteVectorDatabaseResponse200 | ErrorResponse
     """


    return (await asyncio_detailed(
        database_id=database_id,
client=client,

    )).parsed
