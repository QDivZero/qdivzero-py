from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_public_token_usage_response_200 import GetV1PublicTokenUsageResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    timezone: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["from"] = from_

    params["to"] = to

    params["timezone"] = timezone

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/public/token-usage",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetV1PublicTokenUsageResponse200 | None:
    if response.status_code == 200:
        response_200 = GetV1PublicTokenUsageResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetV1PublicTokenUsageResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    timezone: str | Unset = UNSET,
) -> Response[Any | GetV1PublicTokenUsageResponse200]:
    """Public platform token usage

     Public aggregate token totals, daily counts and top_models as an ordered name-only list. No
    authentication required. totals covers all recorded usage; period_totals, days and top_models cover
    [from,to) in the IANA timezone (UTC by default). Dates default to the last 30 calendar days
    including today, with a maximum of 366 days. Token figures apply APIGW_PUBLIC_TOKEN_USAGE_MULTIPLIER
    (default 1); decimals round to the nearest token, halves up. The model list ranks up to ten approved
    public names by total recorded tokens, independent of the display multiplier; anonymous legacy
    events and private/custom names are excluded from the ranking. measured_since is the first recorded
    invocation, or null when empty. Today's count is partial; pre-instrumentation, unreported provider
    usage and non-token workloads are unavailable.

    Args:
        from_ (str | Unset):
        to (str | Unset):
        timezone (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetV1PublicTokenUsageResponse200]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        timezone=timezone,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    timezone: str | Unset = UNSET,
) -> Any | GetV1PublicTokenUsageResponse200 | None:
    """Public platform token usage

     Public aggregate token totals, daily counts and top_models as an ordered name-only list. No
    authentication required. totals covers all recorded usage; period_totals, days and top_models cover
    [from,to) in the IANA timezone (UTC by default). Dates default to the last 30 calendar days
    including today, with a maximum of 366 days. Token figures apply APIGW_PUBLIC_TOKEN_USAGE_MULTIPLIER
    (default 1); decimals round to the nearest token, halves up. The model list ranks up to ten approved
    public names by total recorded tokens, independent of the display multiplier; anonymous legacy
    events and private/custom names are excluded from the ranking. measured_since is the first recorded
    invocation, or null when empty. Today's count is partial; pre-instrumentation, unreported provider
    usage and non-token workloads are unavailable.

    Args:
        from_ (str | Unset):
        to (str | Unset):
        timezone (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetV1PublicTokenUsageResponse200
    """

    return sync_detailed(
        client=client,
        from_=from_,
        to=to,
        timezone=timezone,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    timezone: str | Unset = UNSET,
) -> Response[Any | GetV1PublicTokenUsageResponse200]:
    """Public platform token usage

     Public aggregate token totals, daily counts and top_models as an ordered name-only list. No
    authentication required. totals covers all recorded usage; period_totals, days and top_models cover
    [from,to) in the IANA timezone (UTC by default). Dates default to the last 30 calendar days
    including today, with a maximum of 366 days. Token figures apply APIGW_PUBLIC_TOKEN_USAGE_MULTIPLIER
    (default 1); decimals round to the nearest token, halves up. The model list ranks up to ten approved
    public names by total recorded tokens, independent of the display multiplier; anonymous legacy
    events and private/custom names are excluded from the ranking. measured_since is the first recorded
    invocation, or null when empty. Today's count is partial; pre-instrumentation, unreported provider
    usage and non-token workloads are unavailable.

    Args:
        from_ (str | Unset):
        to (str | Unset):
        timezone (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetV1PublicTokenUsageResponse200]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        timezone=timezone,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    timezone: str | Unset = UNSET,
) -> Any | GetV1PublicTokenUsageResponse200 | None:
    """Public platform token usage

     Public aggregate token totals, daily counts and top_models as an ordered name-only list. No
    authentication required. totals covers all recorded usage; period_totals, days and top_models cover
    [from,to) in the IANA timezone (UTC by default). Dates default to the last 30 calendar days
    including today, with a maximum of 366 days. Token figures apply APIGW_PUBLIC_TOKEN_USAGE_MULTIPLIER
    (default 1); decimals round to the nearest token, halves up. The model list ranks up to ten approved
    public names by total recorded tokens, independent of the display multiplier; anonymous legacy
    events and private/custom names are excluded from the ranking. measured_since is the first recorded
    invocation, or null when empty. Today's count is partial; pre-instrumentation, unreported provider
    usage and non-token workloads are unavailable.

    Args:
        from_ (str | Unset):
        to (str | Unset):
        timezone (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetV1PublicTokenUsageResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            from_=from_,
            to=to,
            timezone=timezone,
        )
    ).parsed
