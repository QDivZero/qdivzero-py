from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StartupProgress")


@_attrs_define
class StartupProgress:
    """
    Attributes:
        phase (str | Unset):
        source (str | Unset):
        updated_at (str | Unset):
    """

    phase: str | Unset = UNSET
    source: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        phase = self.phase

        source = self.source

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if phase is not UNSET:
            field_dict["phase"] = phase
        if source is not UNSET:
            field_dict["source"] = source
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        phase = d.pop("phase", UNSET)

        source = d.pop("source", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        startup_progress = cls(
            phase=phase,
            source=source,
            updated_at=updated_at,
        )

        startup_progress.additional_properties = d
        return startup_progress

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
