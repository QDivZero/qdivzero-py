from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvitationResponse")


@_attrs_define
class InvitationResponse:
    """
    Attributes:
        accepted_at_unix (int | Unset):
        accepted_by (str | Unset):
        account_description (str | Unset):
        account_id (str | Unset):
        account_name (str | Unset):
        created_at_unix (int | Unset):
        email (str | Unset):
        expires_at_unix (int | Unset):
        id (str | Unset):
        invited_by (str | Unset):
        role (str | Unset):
        status (str | Unset):
        token (str | Unset):
    """

    accepted_at_unix: int | Unset = UNSET
    accepted_by: str | Unset = UNSET
    account_description: str | Unset = UNSET
    account_id: str | Unset = UNSET
    account_name: str | Unset = UNSET
    created_at_unix: int | Unset = UNSET
    email: str | Unset = UNSET
    expires_at_unix: int | Unset = UNSET
    id: str | Unset = UNSET
    invited_by: str | Unset = UNSET
    role: str | Unset = UNSET
    status: str | Unset = UNSET
    token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accepted_at_unix = self.accepted_at_unix

        accepted_by = self.accepted_by

        account_description = self.account_description

        account_id = self.account_id

        account_name = self.account_name

        created_at_unix = self.created_at_unix

        email = self.email

        expires_at_unix = self.expires_at_unix

        id = self.id

        invited_by = self.invited_by

        role = self.role

        status = self.status

        token = self.token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accepted_at_unix is not UNSET:
            field_dict["accepted_at_unix"] = accepted_at_unix
        if accepted_by is not UNSET:
            field_dict["accepted_by"] = accepted_by
        if account_description is not UNSET:
            field_dict["account_description"] = account_description
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if account_name is not UNSET:
            field_dict["account_name"] = account_name
        if created_at_unix is not UNSET:
            field_dict["created_at_unix"] = created_at_unix
        if email is not UNSET:
            field_dict["email"] = email
        if expires_at_unix is not UNSET:
            field_dict["expires_at_unix"] = expires_at_unix
        if id is not UNSET:
            field_dict["id"] = id
        if invited_by is not UNSET:
            field_dict["invited_by"] = invited_by
        if role is not UNSET:
            field_dict["role"] = role
        if status is not UNSET:
            field_dict["status"] = status
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accepted_at_unix = d.pop("accepted_at_unix", UNSET)

        accepted_by = d.pop("accepted_by", UNSET)

        account_description = d.pop("account_description", UNSET)

        account_id = d.pop("account_id", UNSET)

        account_name = d.pop("account_name", UNSET)

        created_at_unix = d.pop("created_at_unix", UNSET)

        email = d.pop("email", UNSET)

        expires_at_unix = d.pop("expires_at_unix", UNSET)

        id = d.pop("id", UNSET)

        invited_by = d.pop("invited_by", UNSET)

        role = d.pop("role", UNSET)

        status = d.pop("status", UNSET)

        token = d.pop("token", UNSET)

        invitation_response = cls(
            accepted_at_unix=accepted_at_unix,
            accepted_by=accepted_by,
            account_description=account_description,
            account_id=account_id,
            account_name=account_name,
            created_at_unix=created_at_unix,
            email=email,
            expires_at_unix=expires_at_unix,
            id=id,
            invited_by=invited_by,
            role=role,
            status=status,
            token=token,
        )

        invitation_response.additional_properties = d
        return invitation_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
