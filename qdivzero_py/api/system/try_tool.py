from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.try_tool_body import TryToolBody
from ...models.try_tool_response_200 import TryToolResponse200
from ...types import Response


def _get_kwargs(
    tool_type: str,
    *,
    body: TryToolBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/tools/{tool_type}/try".format(
            tool_type=quote(str(tool_type), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | TryToolResponse200 | None:
    if response.status_code == 200:
        response_200 = TryToolResponse200.from_dict(response.json())

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


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | TryToolResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tool_type: str,
    *,
    client: AuthenticatedClient,
    body: TryToolBody,
) -> Response[ErrorResponse | TryToolResponse200]:
    """Try a tool

     Runs a single platform tool with the given configuration and returns the raw tool output.

    Args:
        tool_type (str):
        body (TryToolBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | TryToolResponse200]
    """

    kwargs = _get_kwargs(
        tool_type=tool_type,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tool_type: str,
    *,
    client: AuthenticatedClient,
    body: TryToolBody,
) -> ErrorResponse | TryToolResponse200 | None:
    """Try a tool

     Runs a single platform tool with the given configuration and returns the raw tool output.

    Args:
        tool_type (str):
        body (TryToolBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | TryToolResponse200
    """

    return sync_detailed(
        tool_type=tool_type,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    tool_type: str,
    *,
    client: AuthenticatedClient,
    body: TryToolBody,
) -> Response[ErrorResponse | TryToolResponse200]:
    """Try a tool

     Runs a single platform tool with the given configuration and returns the raw tool output.

    Args:
        tool_type (str):
        body (TryToolBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | TryToolResponse200]
    """

    kwargs = _get_kwargs(
        tool_type=tool_type,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tool_type: str,
    *,
    client: AuthenticatedClient,
    body: TryToolBody,
) -> ErrorResponse | TryToolResponse200 | None:
    """Try a tool

     Runs a single platform tool with the given configuration and returns the raw tool output.

    Args:
        tool_type (str):
        body (TryToolBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | TryToolResponse200
    """

    return (
        await asyncio_detailed(
            tool_type=tool_type,
            client=client,
            body=body,
        )
    ).parsed
