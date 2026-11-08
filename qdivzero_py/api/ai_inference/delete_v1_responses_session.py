from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_v1_responses_session_response_200 import DeleteV1ResponsesSessionResponse200
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    response_id: str,
    *,
    conversation: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["conversation"] = conversation

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/responses/sessions/{response_id}".format(
            response_id=quote(str(response_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeleteV1ResponsesSessionResponse200 | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = DeleteV1ResponsesSessionResponse200.from_dict(response.json())

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
) -> Response[DeleteV1ResponsesSessionResponse200 | ErrorResponse]:
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
    conversation: str | Unset = UNSET,
) -> Response[DeleteV1ResponsesSessionResponse200 | ErrorResponse]:
    r"""Delete a saved response or whole conversation

     Deletes one snapshot, or the full conversation chain when \"conversation\": true.

    Args:
        response_id (str):
        conversation (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteV1ResponsesSessionResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        response_id=response_id,
        conversation=conversation,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    response_id: str,
    *,
    client: AuthenticatedClient,
    conversation: str | Unset = UNSET,
) -> DeleteV1ResponsesSessionResponse200 | ErrorResponse | None:
    r"""Delete a saved response or whole conversation

     Deletes one snapshot, or the full conversation chain when \"conversation\": true.

    Args:
        response_id (str):
        conversation (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteV1ResponsesSessionResponse200 | ErrorResponse
    """

    return sync_detailed(
        response_id=response_id,
        client=client,
        conversation=conversation,
    ).parsed


async def asyncio_detailed(
    response_id: str,
    *,
    client: AuthenticatedClient,
    conversation: str | Unset = UNSET,
) -> Response[DeleteV1ResponsesSessionResponse200 | ErrorResponse]:
    r"""Delete a saved response or whole conversation

     Deletes one snapshot, or the full conversation chain when \"conversation\": true.

    Args:
        response_id (str):
        conversation (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteV1ResponsesSessionResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        response_id=response_id,
        conversation=conversation,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    response_id: str,
    *,
    client: AuthenticatedClient,
    conversation: str | Unset = UNSET,
) -> DeleteV1ResponsesSessionResponse200 | ErrorResponse | None:
    r"""Delete a saved response or whole conversation

     Deletes one snapshot, or the full conversation chain when \"conversation\": true.

    Args:
        response_id (str):
        conversation (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteV1ResponsesSessionResponse200 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            response_id=response_id,
            client=client,
            conversation=conversation,
        )
    ).parsed
