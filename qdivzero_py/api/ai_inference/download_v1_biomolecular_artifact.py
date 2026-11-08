from http import HTTPStatus
from io import BytesIO
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...types import File, Response


def _get_kwargs(
    job_id: str,
    artifact_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/biomolecular/jobs/{job_id}/artifacts/{artifact_id}".format(
            job_id=quote(str(job_id), safe=""),
            artifact_id=quote(str(artifact_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorResponse | File | None:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | File]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    job_id: str,
    artifact_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | File]:
    """Download a persisted Boltz artifact

     Bounded binary stream, available independently of the original instance for seven days after job
    completion.

    Args:
        job_id (str):
        artifact_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | File]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        artifact_id=artifact_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    job_id: str,
    artifact_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | File | None:
    """Download a persisted Boltz artifact

     Bounded binary stream, available independently of the original instance for seven days after job
    completion.

    Args:
        job_id (str):
        artifact_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | File
    """

    return sync_detailed(
        job_id=job_id,
        artifact_id=artifact_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    job_id: str,
    artifact_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | File]:
    """Download a persisted Boltz artifact

     Bounded binary stream, available independently of the original instance for seven days after job
    completion.

    Args:
        job_id (str):
        artifact_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | File]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        artifact_id=artifact_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_id: str,
    artifact_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | File | None:
    """Download a persisted Boltz artifact

     Bounded binary stream, available independently of the original instance for seven days after job
    completion.

    Args:
        job_id (str):
        artifact_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | File
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            artifact_id=artifact_id,
            client=client,
        )
    ).parsed
