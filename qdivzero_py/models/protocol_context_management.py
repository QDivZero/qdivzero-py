from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtocolContextManagement")


@_attrs_define
class ProtocolContextManagement:
    """
    Attributes:
        compact_threshold (int | Unset):
        type_ (str | Unset):
    """

    compact_threshold: int | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        compact_threshold = self.compact_threshold

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if compact_threshold is not UNSET:
            field_dict["compact_threshold"] = compact_threshold
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        compact_threshold = d.pop("compact_threshold", UNSET)

        type_ = d.pop("type", UNSET)

        protocol_context_management = cls(
            compact_threshold=compact_threshold,
            type_=type_,
        )

        protocol_context_management.additional_properties = d
        return protocol_context_management

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
