from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.list_documents_response import ListDocumentsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    database_id: str,
    *,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/flexible-vector-databases/{database_id}/documents".format(database_id=quote(str(database_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorResponse | ListDocumentsResponse | None:
    if response.status_code == 200:
        response_200 = ListDocumentsResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorResponse | ListDocumentsResponse]:
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
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> Response[ErrorResponse | ListDocumentsResponse]:
    """ List documents in a vector database

     Returns documents stored in a vector database with optional pagination.

    Args:
        database_id (str):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ListDocumentsResponse]
     """


    kwargs = _get_kwargs(
        database_id=database_id,
limit=limit,
cursor=cursor,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    database_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> ErrorResponse | ListDocumentsResponse | None:
    """ List documents in a vector database

     Returns documents stored in a vector database with optional pagination.

    Args:
        database_id (str):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ListDocumentsResponse
     """


    return sync_detailed(
        database_id=database_id,
client=client,
limit=limit,
cursor=cursor,

    ).parsed

async def asyncio_detailed(
    database_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> Response[ErrorResponse | ListDocumentsResponse]:
    """ List documents in a vector database

     Returns documents stored in a vector database with optional pagination.

    Args:
        database_id (str):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ListDocumentsResponse]
     """


    kwargs = _get_kwargs(
        database_id=database_id,
limit=limit,
cursor=cursor,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    database_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> ErrorResponse | ListDocumentsResponse | None:
    """ List documents in a vector database

     Returns documents stored in a vector database with optional pagination.

    Args:
        database_id (str):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ListDocumentsResponse
     """


    return (await asyncio_detailed(
        database_id=database_id,
client=client,
limit=limit,
cursor=cursor,

    )).parsed
