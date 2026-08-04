from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.account_member_response import AccountMemberResponse
from ...models.add_account_member_request import AddAccountMemberRequest
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    body: AddAccountMemberRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/accounts/current/members",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AccountMemberResponse | ErrorResponse | str | None:
    if response.status_code == 200:
        response_200 = AccountMemberResponse.from_dict(response.json())



        return response_200

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

    if response.status_code == 412:
        response_412 = ErrorResponse.from_dict(response.json())



        return response_412

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AccountMemberResponse | ErrorResponse | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AddAccountMemberRequest,

) -> Response[AccountMemberResponse | ErrorResponse | str]:
    """ Add a member to the selected account

     Adds a registered user to the active account context or updates their role if they already belong to
    it.

    Args:
        body (AddAccountMemberRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountMemberResponse | ErrorResponse | str]
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
    body: AddAccountMemberRequest,

) -> AccountMemberResponse | ErrorResponse | str | None:
    """ Add a member to the selected account

     Adds a registered user to the active account context or updates their role if they already belong to
    it.

    Args:
        body (AddAccountMemberRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountMemberResponse | ErrorResponse | str
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AddAccountMemberRequest,

) -> Response[AccountMemberResponse | ErrorResponse | str]:
    """ Add a member to the selected account

     Adds a registered user to the active account context or updates their role if they already belong to
    it.

    Args:
        body (AddAccountMemberRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountMemberResponse | ErrorResponse | str]
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
    body: AddAccountMemberRequest,

) -> AccountMemberResponse | ErrorResponse | str | None:
    """ Add a member to the selected account

     Adds a registered user to the active account context or updates their role if they already belong to
    it.

    Args:
        body (AddAccountMemberRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountMemberResponse | ErrorResponse | str
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
