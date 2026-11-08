from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    model: str,
    mode: str | Unset = UNSET,
    duplex: str | Unset = UNSET,
    session_id: str | Unset = UNSET,
    autostart: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["model"] = model

    params["mode"] = mode

    params["duplex"] = duplex

    params["session_id"] = session_id

    params["autostart"] = autostart

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/realtime",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorResponse | str | None:
    if response.status_code == 101:
        response_101 = cast(str, response.json())
        return response_101

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorResponse | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    model: str,
    mode: str | Unset = UNSET,
    duplex: str | Unset = UNSET,
    session_id: str | Unset = UNSET,
    autostart: str | Unset = UNSET,
) -> Response[ErrorResponse | str]:
    """Realtime WebSocket proxy

     Proxies a turn-based or native-duplex Omni session, or a realtime ASR transcription session, to the
    selected model. The legacy duplex=1 alias selects duplex mode. ASR transcription uses incremental
    PCM audio events and returns transcription.delta events. Accepts Bearer access tokens or API keys.

    Args:
        model (str):
        mode (str | Unset):
        duplex (str | Unset):
        session_id (str | Unset):
        autostart (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | str]
    """

    kwargs = _get_kwargs(
        model=model,
        mode=mode,
        duplex=duplex,
        session_id=session_id,
        autostart=autostart,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    model: str,
    mode: str | Unset = UNSET,
    duplex: str | Unset = UNSET,
    session_id: str | Unset = UNSET,
    autostart: str | Unset = UNSET,
) -> ErrorResponse | str | None:
    """Realtime WebSocket proxy

     Proxies a turn-based or native-duplex Omni session, or a realtime ASR transcription session, to the
    selected model. The legacy duplex=1 alias selects duplex mode. ASR transcription uses incremental
    PCM audio events and returns transcription.delta events. Accepts Bearer access tokens or API keys.

    Args:
        model (str):
        mode (str | Unset):
        duplex (str | Unset):
        session_id (str | Unset):
        autostart (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | str
    """

    return sync_detailed(
        client=client,
        model=model,
        mode=mode,
        duplex=duplex,
        session_id=session_id,
        autostart=autostart,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    model: str,
    mode: str | Unset = UNSET,
    duplex: str | Unset = UNSET,
    session_id: str | Unset = UNSET,
    autostart: str | Unset = UNSET,
) -> Response[ErrorResponse | str]:
    """Realtime WebSocket proxy

     Proxies a turn-based or native-duplex Omni session, or a realtime ASR transcription session, to the
    selected model. The legacy duplex=1 alias selects duplex mode. ASR transcription uses incremental
    PCM audio events and returns transcription.delta events. Accepts Bearer access tokens or API keys.

    Args:
        model (str):
        mode (str | Unset):
        duplex (str | Unset):
        session_id (str | Unset):
        autostart (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | str]
    """

    kwargs = _get_kwargs(
        model=model,
        mode=mode,
        duplex=duplex,
        session_id=session_id,
        autostart=autostart,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    model: str,
    mode: str | Unset = UNSET,
    duplex: str | Unset = UNSET,
    session_id: str | Unset = UNSET,
    autostart: str | Unset = UNSET,
) -> ErrorResponse | str | None:
    """Realtime WebSocket proxy

     Proxies a turn-based or native-duplex Omni session, or a realtime ASR transcription session, to the
    selected model. The legacy duplex=1 alias selects duplex mode. ASR transcription uses incremental
    PCM audio events and returns transcription.delta events. Accepts Bearer access tokens or API keys.

    Args:
        model (str):
        mode (str | Unset):
        duplex (str | Unset):
        session_id (str | Unset):
        autostart (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | str
    """

    return (
        await asyncio_detailed(
            client=client,
            model=model,
            mode=mode,
            duplex=duplex,
            session_id=session_id,
            autostart=autostart,
        )
    ).parsed
