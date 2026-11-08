from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BiomolecularCapabilities")


@_attrs_define
class BiomolecularCapabilities:
    """
    Attributes:
        checked_at (str | Unset):
        msa_status (str | Unset):
    """

    checked_at: str | Unset = UNSET
    msa_status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        checked_at = self.checked_at

        msa_status = self.msa_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if checked_at is not UNSET:
            field_dict["checked_at"] = checked_at
        if msa_status is not UNSET:
            field_dict["msa_status"] = msa_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        checked_at = d.pop("checked_at", UNSET)

        msa_status = d.pop("msa_status", UNSET)

        biomolecular_capabilities = cls(
            checked_at=checked_at,
            msa_status=msa_status,
        )

        biomolecular_capabilities.additional_properties = d
        return biomolecular_capabilities

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
