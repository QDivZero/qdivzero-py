from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.replica_set_response import ReplicaSetResponse
from ...types import Response


def _get_kwargs(
    replica_set_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/replica-sets/{replica_set_id}".format(
            replica_set_id=quote(str(replica_set_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ReplicaSetResponse | str | None:
    if response.status_code == 200:
        response_200 = ReplicaSetResponse.from_dict(response.json())

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

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | ReplicaSetResponse | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    replica_set_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | ReplicaSetResponse | str]:
    """Get a replica set

    Args:
        replica_set_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ReplicaSetResponse | str]
    """

    kwargs = _get_kwargs(
        replica_set_id=replica_set_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    replica_set_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | ReplicaSetResponse | str | None:
    """Get a replica set

    Args:
        replica_set_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ReplicaSetResponse | str
    """

    return sync_detailed(
        replica_set_id=replica_set_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    replica_set_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | ReplicaSetResponse | str]:
    """Get a replica set

    Args:
        replica_set_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ReplicaSetResponse | str]
    """

    kwargs = _get_kwargs(
        replica_set_id=replica_set_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    replica_set_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | ReplicaSetResponse | str | None:
    """Get a replica set

    Args:
        replica_set_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ReplicaSetResponse | str
    """

    return (
        await asyncio_detailed(
            replica_set_id=replica_set_id,
            client=client,
        )
    ).parsed
