from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.hugging_face_org_info_response import HuggingFaceOrgInfoResponse
from ...types import Response


def _get_kwargs(
    org: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/huggingface/orgs/{org}".format(org=quote(str(org), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorResponse | HuggingFaceOrgInfoResponse | None:
    if response.status_code == 200:
        response_200 = HuggingFaceOrgInfoResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorResponse | HuggingFaceOrgInfoResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    org: str,
    *,
    client: AuthenticatedClient,

) -> Response[ErrorResponse | HuggingFaceOrgInfoResponse]:
    """ Get Hugging Face organization info

     Returns profile information for a Hugging Face organization.

    Args:
        org (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HuggingFaceOrgInfoResponse]
     """


    kwargs = _get_kwargs(
        org=org,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    org: str,
    *,
    client: AuthenticatedClient,

) -> ErrorResponse | HuggingFaceOrgInfoResponse | None:
    """ Get Hugging Face organization info

     Returns profile information for a Hugging Face organization.

    Args:
        org (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HuggingFaceOrgInfoResponse
     """


    return sync_detailed(
        org=org,
client=client,

    ).parsed

async def asyncio_detailed(
    org: str,
    *,
    client: AuthenticatedClient,

) -> Response[ErrorResponse | HuggingFaceOrgInfoResponse]:
    """ Get Hugging Face organization info

     Returns profile information for a Hugging Face organization.

    Args:
        org (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HuggingFaceOrgInfoResponse]
     """


    kwargs = _get_kwargs(
        org=org,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    org: str,
    *,
    client: AuthenticatedClient,

) -> ErrorResponse | HuggingFaceOrgInfoResponse | None:
    """ Get Hugging Face organization info

     Returns profile information for a Hugging Face organization.

    Args:
        org (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HuggingFaceOrgInfoResponse
     """


    return (await asyncio_detailed(
        org=org,
client=client,

    )).parsed
