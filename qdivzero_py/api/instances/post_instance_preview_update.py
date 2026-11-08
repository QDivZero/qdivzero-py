from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.preview_instance_response import PreviewInstanceResponse
from ...models.preview_instance_update_request import PreviewInstanceUpdateRequest
from ...types import Response


def _get_kwargs(
    instance_id: str,
    *,
    body: PreviewInstanceUpdateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/instances/{instance_id}/preview".format(
            instance_id=quote(str(instance_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | PreviewInstanceResponse | str | None:
    if response.status_code == 200:
        response_200 = PreviewInstanceResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | PreviewInstanceResponse | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    instance_id: str,
    *,
    client: AuthenticatedClient,
    body: PreviewInstanceUpdateRequest,
) -> Response[ErrorResponse | PreviewInstanceResponse | str]:
    """Preview smart selection for an existing instance update

     Previews the compatibility and smart selection for an existing instance while applying smart-setting
    overrides from the request body. Lets the instance settings page fetch the same backend-filtered GPU
    list used at launch time instead of reimplementing compatibility filtering in the UI.

    Args:
        instance_id (str):
        body (PreviewInstanceUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PreviewInstanceResponse | str]
    """

    kwargs = _get_kwargs(
        instance_id=instance_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    instance_id: str,
    *,
    client: AuthenticatedClient,
    body: PreviewInstanceUpdateRequest,
) -> ErrorResponse | PreviewInstanceResponse | str | None:
    """Preview smart selection for an existing instance update

     Previews the compatibility and smart selection for an existing instance while applying smart-setting
    overrides from the request body. Lets the instance settings page fetch the same backend-filtered GPU
    list used at launch time instead of reimplementing compatibility filtering in the UI.

    Args:
        instance_id (str):
        body (PreviewInstanceUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PreviewInstanceResponse | str
    """

    return sync_detailed(
        instance_id=instance_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    instance_id: str,
    *,
    client: AuthenticatedClient,
    body: PreviewInstanceUpdateRequest,
) -> Response[ErrorResponse | PreviewInstanceResponse | str]:
    """Preview smart selection for an existing instance update

     Previews the compatibility and smart selection for an existing instance while applying smart-setting
    overrides from the request body. Lets the instance settings page fetch the same backend-filtered GPU
    list used at launch time instead of reimplementing compatibility filtering in the UI.

    Args:
        instance_id (str):
        body (PreviewInstanceUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PreviewInstanceResponse | str]
    """

    kwargs = _get_kwargs(
        instance_id=instance_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    instance_id: str,
    *,
    client: AuthenticatedClient,
    body: PreviewInstanceUpdateRequest,
) -> ErrorResponse | PreviewInstanceResponse | str | None:
    """Preview smart selection for an existing instance update

     Previews the compatibility and smart selection for an existing instance while applying smart-setting
    overrides from the request body. Lets the instance settings page fetch the same backend-filtered GPU
    list used at launch time instead of reimplementing compatibility filtering in the UI.

    Args:
        instance_id (str):
        body (PreviewInstanceUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PreviewInstanceResponse | str
    """

    return (
        await asyncio_detailed(
            instance_id=instance_id,
            client=client,
            body=body,
        )
    ).parsed
