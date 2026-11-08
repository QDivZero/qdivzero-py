from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.execution_system_one_request import ExecutionSystemOneRequest
from ...models.execution_system_one_response import ExecutionSystemOneResponse
from ...types import Response


def _get_kwargs(
    *,
    body: ExecutionSystemOneRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/systemone",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ExecutionSystemOneResponse | None:
    if response.status_code == 200:
        response_200 = ExecutionSystemOneResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 413:
        response_413 = ErrorResponse.from_dict(response.json())

        return response_413

    if response.status_code == 415:
        response_415 = ErrorResponse.from_dict(response.json())

        return response_415

    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())

        return response_503

    if response.status_code == 504:
        response_504 = ErrorResponse.from_dict(response.json())

        return response_504

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | ExecutionSystemOneResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ExecutionSystemOneRequest,
) -> Response[ErrorResponse | ExecutionSystemOneResponse]:
    """Answer typed questions about a text or JSON state

     Account-owned decision serving name or instance UUID, public:clef-flash, or
    subscription:cloudflare/clef-flash when configured. Up to 64 questions, choice 1..26 options, noul
    optional true/false descriptions, score 2..10 ordered levels. Request limit 32 MiB with 1 MiB of
    non-image metadata; Clef Flash requests are limited to 20 MB including the RunPod input envelope.
    Response limit 1 MiB, nesting 64. Optional images accepts up to four inline base64 PNG, JPEG or WebP
    data URLs, at most 5 MiB decoded and 16 million pixels per image. Images require Clef Flash or a
    compatible managed decision instance. Nested media and unknown fields are rejected. Question
    instructions and descriptions are strings or null. Optional global instructions are supported by
    native Qwen and DiffusionGemma; Clef and Nimble reject nonempty global instructions. Timeout two
    minutes after readiness.

    Args:
        body (ExecutionSystemOneRequest): Request up to 32 MiB and depth 64, with at most 1 MiB of
            original JSON excluding only the top-level images value; at most 64 questions. Each
            instructions/criteria value is bounded to 64 KiB of JSON. Images require Qwen3.5-9B,
            DiffusionGemma, Clef or Clef Flash; Nimble rejects images. Nested media inputs and unknown
            fields are rejected.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ExecutionSystemOneResponse]
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
    body: ExecutionSystemOneRequest,
) -> ErrorResponse | ExecutionSystemOneResponse | None:
    """Answer typed questions about a text or JSON state

     Account-owned decision serving name or instance UUID, public:clef-flash, or
    subscription:cloudflare/clef-flash when configured. Up to 64 questions, choice 1..26 options, noul
    optional true/false descriptions, score 2..10 ordered levels. Request limit 32 MiB with 1 MiB of
    non-image metadata; Clef Flash requests are limited to 20 MB including the RunPod input envelope.
    Response limit 1 MiB, nesting 64. Optional images accepts up to four inline base64 PNG, JPEG or WebP
    data URLs, at most 5 MiB decoded and 16 million pixels per image. Images require Clef Flash or a
    compatible managed decision instance. Nested media and unknown fields are rejected. Question
    instructions and descriptions are strings or null. Optional global instructions are supported by
    native Qwen and DiffusionGemma; Clef and Nimble reject nonempty global instructions. Timeout two
    minutes after readiness.

    Args:
        body (ExecutionSystemOneRequest): Request up to 32 MiB and depth 64, with at most 1 MiB of
            original JSON excluding only the top-level images value; at most 64 questions. Each
            instructions/criteria value is bounded to 64 KiB of JSON. Images require Qwen3.5-9B,
            DiffusionGemma, Clef or Clef Flash; Nimble rejects images. Nested media inputs and unknown
            fields are rejected.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ExecutionSystemOneResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ExecutionSystemOneRequest,
) -> Response[ErrorResponse | ExecutionSystemOneResponse]:
    """Answer typed questions about a text or JSON state

     Account-owned decision serving name or instance UUID, public:clef-flash, or
    subscription:cloudflare/clef-flash when configured. Up to 64 questions, choice 1..26 options, noul
    optional true/false descriptions, score 2..10 ordered levels. Request limit 32 MiB with 1 MiB of
    non-image metadata; Clef Flash requests are limited to 20 MB including the RunPod input envelope.
    Response limit 1 MiB, nesting 64. Optional images accepts up to four inline base64 PNG, JPEG or WebP
    data URLs, at most 5 MiB decoded and 16 million pixels per image. Images require Clef Flash or a
    compatible managed decision instance. Nested media and unknown fields are rejected. Question
    instructions and descriptions are strings or null. Optional global instructions are supported by
    native Qwen and DiffusionGemma; Clef and Nimble reject nonempty global instructions. Timeout two
    minutes after readiness.

    Args:
        body (ExecutionSystemOneRequest): Request up to 32 MiB and depth 64, with at most 1 MiB of
            original JSON excluding only the top-level images value; at most 64 questions. Each
            instructions/criteria value is bounded to 64 KiB of JSON. Images require Qwen3.5-9B,
            DiffusionGemma, Clef or Clef Flash; Nimble rejects images. Nested media inputs and unknown
            fields are rejected.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ExecutionSystemOneResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ExecutionSystemOneRequest,
) -> ErrorResponse | ExecutionSystemOneResponse | None:
    """Answer typed questions about a text or JSON state

     Account-owned decision serving name or instance UUID, public:clef-flash, or
    subscription:cloudflare/clef-flash when configured. Up to 64 questions, choice 1..26 options, noul
    optional true/false descriptions, score 2..10 ordered levels. Request limit 32 MiB with 1 MiB of
    non-image metadata; Clef Flash requests are limited to 20 MB including the RunPod input envelope.
    Response limit 1 MiB, nesting 64. Optional images accepts up to four inline base64 PNG, JPEG or WebP
    data URLs, at most 5 MiB decoded and 16 million pixels per image. Images require Clef Flash or a
    compatible managed decision instance. Nested media and unknown fields are rejected. Question
    instructions and descriptions are strings or null. Optional global instructions are supported by
    native Qwen and DiffusionGemma; Clef and Nimble reject nonempty global instructions. Timeout two
    minutes after readiness.

    Args:
        body (ExecutionSystemOneRequest): Request up to 32 MiB and depth 64, with at most 1 MiB of
            original JSON excluding only the top-level images value; at most 64 questions. Each
            instructions/criteria value is bounded to 64 KiB of JSON. Images require Qwen3.5-9B,
            DiffusionGemma, Clef or Clef Flash; Nimble rejects images. Nested media inputs and unknown
            fields are rejected.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ExecutionSystemOneResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
