from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.hugging_face_models_response import HuggingFaceModelsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["limit"] = limit

    params["sort"] = sort

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/huggingface/models",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HuggingFaceModelsResponse | None:
    if response.status_code == 200:
        response_200 = HuggingFaceModelsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 412:
        response_412 = ErrorResponse.from_dict(response.json())

        return response_412

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | HuggingFaceModelsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[ErrorResponse | HuggingFaceModelsResponse]:
    """Search Hugging Face models

     Searches Hugging Face for compatible models matching the query.

    Args:
        q (str | Unset):
        limit (int | Unset):
        sort (str | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HuggingFaceModelsResponse]
    """

    kwargs = _get_kwargs(
        q=q,
        limit=limit,
        sort=sort,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> ErrorResponse | HuggingFaceModelsResponse | None:
    """Search Hugging Face models

     Searches Hugging Face for compatible models matching the query.

    Args:
        q (str | Unset):
        limit (int | Unset):
        sort (str | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HuggingFaceModelsResponse
    """

    return sync_detailed(
        client=client,
        q=q,
        limit=limit,
        sort=sort,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[ErrorResponse | HuggingFaceModelsResponse]:
    """Search Hugging Face models

     Searches Hugging Face for compatible models matching the query.

    Args:
        q (str | Unset):
        limit (int | Unset):
        sort (str | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HuggingFaceModelsResponse]
    """

    kwargs = _get_kwargs(
        q=q,
        limit=limit,
        sort=sort,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> ErrorResponse | HuggingFaceModelsResponse | None:
    """Search Hugging Face models

     Searches Hugging Face for compatible models matching the query.

    Args:
        q (str | Unset):
        limit (int | Unset):
        sort (str | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HuggingFaceModelsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            limit=limit,
            sort=sort,
            cursor=cursor,
        )
    ).parsed
