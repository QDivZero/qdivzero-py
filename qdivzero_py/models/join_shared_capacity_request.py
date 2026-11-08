from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JoinSharedCapacityRequest")


@_attrs_define
class JoinSharedCapacityRequest:
    """
    Attributes:
        group_id (str | Unset):
        public_slug (str | Unset):
        referral_token (str | Unset):
        terms_hash (str | Unset):
        terms_version (str | Unset):
    """

    group_id: str | Unset = UNSET
    public_slug: str | Unset = UNSET
    referral_token: str | Unset = UNSET
    terms_hash: str | Unset = UNSET
    terms_version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_id = self.group_id

        public_slug = self.public_slug

        referral_token = self.referral_token

        terms_hash = self.terms_hash

        terms_version = self.terms_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if public_slug is not UNSET:
            field_dict["public_slug"] = public_slug
        if referral_token is not UNSET:
            field_dict["referral_token"] = referral_token
        if terms_hash is not UNSET:
            field_dict["terms_hash"] = terms_hash
        if terms_version is not UNSET:
            field_dict["terms_version"] = terms_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group_id = d.pop("group_id", UNSET)

        public_slug = d.pop("public_slug", UNSET)

        referral_token = d.pop("referral_token", UNSET)

        terms_hash = d.pop("terms_hash", UNSET)

        terms_version = d.pop("terms_version", UNSET)

        join_shared_capacity_request = cls(
            group_id=group_id,
            public_slug=public_slug,
            referral_token=referral_token,
            terms_hash=terms_hash,
            terms_version=terms_version,
        )

        join_shared_capacity_request.additional_properties = d
        return join_shared_capacity_request

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
