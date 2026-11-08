from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_instance_request import CreateInstanceRequest
from ...models.error_response import ErrorResponse
from ...models.instance_response import InstanceResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateInstanceRequest,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/instances",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | InstanceResponse | str | None:
    if response.status_code == 201:
        response_201 = InstanceResponse.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = cast(str, response.json())
        return response_401

    if response.status_code == 402:
        response_402 = ErrorResponse.from_dict(response.json())

        return response_402

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
) -> Response[ErrorResponse | InstanceResponse | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateInstanceRequest,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorResponse | InstanceResponse | str]:
    """Create an inference instance

     Workload is derived from the repository. Optional workload_kind=decision selects an approved
    decision checkpoint; Qwen/Qwen3.5-9B defaults to chat.

    Args:
        idempotency_key (str | Unset):
        body (CreateInstanceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | InstanceResponse | str]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreateInstanceRequest,
    idempotency_key: str | Unset = UNSET,
) -> ErrorResponse | InstanceResponse | str | None:
    """Create an inference instance

     Workload is derived from the repository. Optional workload_kind=decision selects an approved
    decision checkpoint; Qwen/Qwen3.5-9B defaults to chat.

    Args:
        idempotency_key (str | Unset):
        body (CreateInstanceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | InstanceResponse | str
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateInstanceRequest,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorResponse | InstanceResponse | str]:
    """Create an inference instance

     Workload is derived from the repository. Optional workload_kind=decision selects an approved
    decision checkpoint; Qwen/Qwen3.5-9B defaults to chat.

    Args:
        idempotency_key (str | Unset):
        body (CreateInstanceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | InstanceResponse | str]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateInstanceRequest,
    idempotency_key: str | Unset = UNSET,
) -> ErrorResponse | InstanceResponse | str | None:
    """Create an inference instance

     Workload is derived from the repository. Optional workload_kind=decision selects an approved
    decision checkpoint; Qwen/Qwen3.5-9B defaults to chat.

    Args:
        idempotency_key (str | Unset):
        body (CreateInstanceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | InstanceResponse | str
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
