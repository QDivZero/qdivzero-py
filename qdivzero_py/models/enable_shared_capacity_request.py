from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EnableSharedCapacityRequest")


@_attrs_define
class EnableSharedCapacityRequest:
    """
    Attributes:
        terms_hash (str | Unset):
        terms_version (str | Unset):
        visibility (str | Unset):
    """

    terms_hash: str | Unset = UNSET
    terms_version: str | Unset = UNSET
    visibility: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        terms_hash = self.terms_hash

        terms_version = self.terms_version

        visibility = self.visibility

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if terms_hash is not UNSET:
            field_dict["terms_hash"] = terms_hash
        if terms_version is not UNSET:
            field_dict["terms_version"] = terms_version
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        terms_hash = d.pop("terms_hash", UNSET)

        terms_version = d.pop("terms_version", UNSET)

        visibility = d.pop("visibility", UNSET)

        enable_shared_capacity_request = cls(
            terms_hash=terms_hash,
            terms_version=terms_version,
            visibility=visibility,
        )

        enable_shared_capacity_request.additional_properties = d
        return enable_shared_capacity_request

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
