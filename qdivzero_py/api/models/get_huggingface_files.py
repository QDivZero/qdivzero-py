from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.hugging_face_files_response import HuggingFaceFilesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    repo: str,
    format_: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["repo"] = repo

    params["format"] = format_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/huggingface/files",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HuggingFaceFilesResponse | None:
    if response.status_code == 200:
        response_200 = HuggingFaceFilesResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | HuggingFaceFilesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    repo: str,
    format_: str | Unset = UNSET,
) -> Response[ErrorResponse | HuggingFaceFilesResponse]:
    """Get Hugging Face file sizes

     Returns GGUF files by default, or compatible YOLO .pt checkpoints when format=yolo. Repository
    revisions are supported.

    Args:
        repo (str):
        format_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HuggingFaceFilesResponse]
    """

    kwargs = _get_kwargs(
        repo=repo,
        format_=format_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    repo: str,
    format_: str | Unset = UNSET,
) -> ErrorResponse | HuggingFaceFilesResponse | None:
    """Get Hugging Face file sizes

     Returns GGUF files by default, or compatible YOLO .pt checkpoints when format=yolo. Repository
    revisions are supported.

    Args:
        repo (str):
        format_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HuggingFaceFilesResponse
    """

    return sync_detailed(
        client=client,
        repo=repo,
        format_=format_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    repo: str,
    format_: str | Unset = UNSET,
) -> Response[ErrorResponse | HuggingFaceFilesResponse]:
    """Get Hugging Face file sizes

     Returns GGUF files by default, or compatible YOLO .pt checkpoints when format=yolo. Repository
    revisions are supported.

    Args:
        repo (str):
        format_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HuggingFaceFilesResponse]
    """

    kwargs = _get_kwargs(
        repo=repo,
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    repo: str,
    format_: str | Unset = UNSET,
) -> ErrorResponse | HuggingFaceFilesResponse | None:
    """Get Hugging Face file sizes

     Returns GGUF files by default, or compatible YOLO .pt checkpoints when format=yolo. Repository
    revisions are supported.

    Args:
        repo (str):
        format_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HuggingFaceFilesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            repo=repo,
            format_=format_,
        )
    ).parsed
