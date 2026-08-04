from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_vector_database_request import CreateVectorDatabaseRequest
from ...models.error_response import ErrorResponse
from ...models.vector_database_response import VectorDatabaseResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CreateVectorDatabaseRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/flexible-vector-databases",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorResponse | VectorDatabaseResponse | None:
    if response.status_code == 201:
        response_201 = VectorDatabaseResponse.from_dict(response.json())



        return response_201

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorResponse | VectorDatabaseResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateVectorDatabaseRequest,

) -> Response[ErrorResponse | VectorDatabaseResponse]:
    """ Create a vector database

     Creates a new vector database for the authenticated account.

    Args:
        body (CreateVectorDatabaseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | VectorDatabaseResponse]
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
    body: CreateVectorDatabaseRequest,

) -> ErrorResponse | VectorDatabaseResponse | None:
    """ Create a vector database

     Creates a new vector database for the authenticated account.

    Args:
        body (CreateVectorDatabaseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | VectorDatabaseResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateVectorDatabaseRequest,

) -> Response[ErrorResponse | VectorDatabaseResponse]:
    """ Create a vector database

     Creates a new vector database for the authenticated account.

    Args:
        body (CreateVectorDatabaseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | VectorDatabaseResponse]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateVectorDatabaseRequest,

) -> ErrorResponse | VectorDatabaseResponse | None:
    """ Create a vector database

     Creates a new vector database for the authenticated account.

    Args:
        body (CreateVectorDatabaseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | VectorDatabaseResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
