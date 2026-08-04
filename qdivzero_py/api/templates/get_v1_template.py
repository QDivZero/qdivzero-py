from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_user_variant_response import GetUserVariantResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    locale: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["locale"] = locale


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/templates/{id}".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorResponse | GetUserVariantResponse | None:
    if response.status_code == 200:
        response_200 = GetUserVariantResponse.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())



        return response_404

    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())



        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorResponse | GetUserVariantResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    locale: str | Unset = UNSET,

) -> Response[ErrorResponse | GetUserVariantResponse]:
    """ Get a template variant

     Returns a single template variant by ID for the authenticated user.

    Args:
        id (str):
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetUserVariantResponse]
     """


    kwargs = _get_kwargs(
        id=id,
locale=locale,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    locale: str | Unset = UNSET,

) -> ErrorResponse | GetUserVariantResponse | None:
    """ Get a template variant

     Returns a single template variant by ID for the authenticated user.

    Args:
        id (str):
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetUserVariantResponse
     """


    return sync_detailed(
        id=id,
client=client,
locale=locale,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    locale: str | Unset = UNSET,

) -> Response[ErrorResponse | GetUserVariantResponse]:
    """ Get a template variant

     Returns a single template variant by ID for the authenticated user.

    Args:
        id (str):
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetUserVariantResponse]
     """


    kwargs = _get_kwargs(
        id=id,
locale=locale,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    locale: str | Unset = UNSET,

) -> ErrorResponse | GetUserVariantResponse | None:
    """ Get a template variant

     Returns a single template variant by ID for the authenticated user.

    Args:
        id (str):
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetUserVariantResponse
     """


    return (await asyncio_detailed(
        id=id,
client=client,
locale=locale,

    )).parsed
