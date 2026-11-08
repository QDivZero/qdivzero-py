from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    deployment_id: str,
    *,
    body: Any,
    x_valendra_git_hub_oidc_token: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["X-Valendra-GitHub-OIDC-Token"] = x_valendra_git_hub_oidc_token

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/tool-deployments/{deployment_id}/finalize".format(
            deployment_id=quote(str(deployment_id), safe=""),
        ),
    }

    _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if response.status_code == 401:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    deployment_id: str,
    *,
    client: AuthenticatedClient,
    body: Any,
    x_valendra_git_hub_oidc_token: str,
) -> Response[Any]:
    """Finalize tool deployment

     Verify, discover, provision, and publish an immutable tool deployment.

    Args:
        deployment_id (str):
        x_valendra_git_hub_oidc_token (str):
        body (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        deployment_id=deployment_id,
        body=body,
        x_valendra_git_hub_oidc_token=x_valendra_git_hub_oidc_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    deployment_id: str,
    *,
    client: AuthenticatedClient,
    body: Any,
    x_valendra_git_hub_oidc_token: str,
) -> Response[Any]:
    """Finalize tool deployment

     Verify, discover, provision, and publish an immutable tool deployment.

    Args:
        deployment_id (str):
        x_valendra_git_hub_oidc_token (str):
        body (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        deployment_id=deployment_id,
        body=body,
        x_valendra_git_hub_oidc_token=x_valendra_git_hub_oidc_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
