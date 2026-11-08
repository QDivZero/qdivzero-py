from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_v1_responses_session_detail_response_200 import GetV1ResponsesSessionDetailResponse200
from ...types import Response


def _get_kwargs(
    response_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/responses/sessions/{response_id}".format(
            response_id=quote(str(response_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | GetV1ResponsesSessionDetailResponse200 | None:
    if response.status_code == 200:
        response_200 = GetV1ResponsesSessionDetailResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 502:
        response_502 = ErrorResponse.from_dict(response.json())

        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | GetV1ResponsesSessionDetailResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    response_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | GetV1ResponsesSessionDetailResponse200]:
    """Get a saved Responses conversation

    Args:
        response_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetV1ResponsesSessionDetailResponse200]
    """

    kwargs = _get_kwargs(
        response_id=response_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    response_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | GetV1ResponsesSessionDetailResponse200 | None:
    """Get a saved Responses conversation

    Args:
        response_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetV1ResponsesSessionDetailResponse200
    """

    return sync_detailed(
        response_id=response_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    response_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | GetV1ResponsesSessionDetailResponse200]:
    """Get a saved Responses conversation

    Args:
        response_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetV1ResponsesSessionDetailResponse200]
    """

    kwargs = _get_kwargs(
        response_id=response_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    response_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | GetV1ResponsesSessionDetailResponse200 | None:
    """Get a saved Responses conversation

    Args:
        response_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetV1ResponsesSessionDetailResponse200
    """

    return (
        await asyncio_detailed(
            response_id=response_id,
            client=client,
        )
    ).parsed
