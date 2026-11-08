from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.post_v1_image_edits_body import PostV1ImageEditsBody
from ...models.post_v1_image_edits_response_200 import PostV1ImageEditsResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: PostV1ImageEditsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/images/edits",
    }

    _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | PostV1ImageEditsResponse200 | None:
    if response.status_code == 200:
        response_200 = PostV1ImageEditsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 502:
        response_502 = ErrorResponse.from_dict(response.json())

        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | PostV1ImageEditsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostV1ImageEditsBody,
) -> Response[ErrorResponse | PostV1ImageEditsResponse200]:
    """OpenAI-compatible image edits

     Edits an uploaded image using a prompt and optional mask. Accepts Bearer access tokens or API keys.

    Args:
        body (PostV1ImageEditsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PostV1ImageEditsResponse200]
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
    body: PostV1ImageEditsBody,
) -> ErrorResponse | PostV1ImageEditsResponse200 | None:
    """OpenAI-compatible image edits

     Edits an uploaded image using a prompt and optional mask. Accepts Bearer access tokens or API keys.

    Args:
        body (PostV1ImageEditsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PostV1ImageEditsResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostV1ImageEditsBody,
) -> Response[ErrorResponse | PostV1ImageEditsResponse200]:
    """OpenAI-compatible image edits

     Edits an uploaded image using a prompt and optional mask. Accepts Bearer access tokens or API keys.

    Args:
        body (PostV1ImageEditsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PostV1ImageEditsResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostV1ImageEditsBody,
) -> ErrorResponse | PostV1ImageEditsResponse200 | None:
    """OpenAI-compatible image edits

     Edits an uploaded image using a prompt and optional mask. Accepts Bearer access tokens or API keys.

    Args:
        body (PostV1ImageEditsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PostV1ImageEditsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
