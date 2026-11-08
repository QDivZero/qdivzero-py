from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SharedCapacityLinkResponse")


@_attrs_define
class SharedCapacityLinkResponse:
    """
    Attributes:
        created_by_account_id (str | Unset):
        expires_at (str | Unset):
        group_id (str | Unset):
        id (str | Unset):
        token (str | Unset):
        url (str | Unset):
    """

    created_by_account_id: str | Unset = UNSET
    expires_at: str | Unset = UNSET
    group_id: str | Unset = UNSET
    id: str | Unset = UNSET
    token: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_by_account_id = self.created_by_account_id

        expires_at = self.expires_at

        group_id = self.group_id

        id = self.id

        token = self.token

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_by_account_id is not UNSET:
            field_dict["created_by_account_id"] = created_by_account_id
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if id is not UNSET:
            field_dict["id"] = id
        if token is not UNSET:
            field_dict["token"] = token
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_by_account_id = d.pop("created_by_account_id", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        group_id = d.pop("group_id", UNSET)

        id = d.pop("id", UNSET)

        token = d.pop("token", UNSET)

        url = d.pop("url", UNSET)

        shared_capacity_link_response = cls(
            created_by_account_id=created_by_account_id,
            expires_at=expires_at,
            group_id=group_id,
            id=id,
            token=token,
            url=url,
        )

        shared_capacity_link_response.additional_properties = d
        return shared_capacity_link_response

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
