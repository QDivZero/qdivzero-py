from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.index_documents_request import IndexDocumentsRequest
from ...models.post_vector_database_index_direct_response_200 import PostVectorDatabaseIndexDirectResponse200
from ...types import Response


def _get_kwargs(
    database_id: str,
    *,
    body: IndexDocumentsRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/flexible-vector-databases/{database_id}/index-direct".format(database_id=quote(str(database_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorResponse | PostVectorDatabaseIndexDirectResponse200 | None:
    if response.status_code == 200:
        response_200 = PostVectorDatabaseIndexDirectResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorResponse | PostVectorDatabaseIndexDirectResponse200]:
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
    body: IndexDocumentsRequest,

) -> Response[ErrorResponse | PostVectorDatabaseIndexDirectResponse200]:
    """ Index documents directly

     Indexes documents into a vector database synchronously.

    Args:
        database_id (str):
        body (IndexDocumentsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PostVectorDatabaseIndexDirectResponse200]
     """


    kwargs = _get_kwargs(
        database_id=database_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    database_id: str,
    *,
    client: AuthenticatedClient,
    body: IndexDocumentsRequest,

) -> ErrorResponse | PostVectorDatabaseIndexDirectResponse200 | None:
    """ Index documents directly

     Indexes documents into a vector database synchronously.

    Args:
        database_id (str):
        body (IndexDocumentsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PostVectorDatabaseIndexDirectResponse200
     """


    return sync_detailed(
        database_id=database_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    database_id: str,
    *,
    client: AuthenticatedClient,
    body: IndexDocumentsRequest,

) -> Response[ErrorResponse | PostVectorDatabaseIndexDirectResponse200]:
    """ Index documents directly

     Indexes documents into a vector database synchronously.

    Args:
        database_id (str):
        body (IndexDocumentsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PostVectorDatabaseIndexDirectResponse200]
     """


    kwargs = _get_kwargs(
        database_id=database_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    database_id: str,
    *,
    client: AuthenticatedClient,
    body: IndexDocumentsRequest,

) -> ErrorResponse | PostVectorDatabaseIndexDirectResponse200 | None:
    """ Index documents directly

     Indexes documents into a vector database synchronously.

    Args:
        database_id (str):
        body (IndexDocumentsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PostVectorDatabaseIndexDirectResponse200
     """


    return (await asyncio_detailed(
        database_id=database_id,
client=client,
body=body,

    )).parsed
