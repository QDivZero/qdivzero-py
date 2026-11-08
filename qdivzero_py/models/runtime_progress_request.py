from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RuntimeProgressRequest")


@_attrs_define
class RuntimeProgressRequest:
    """
    Attributes:
        attempt_id (str | Unset): Current observation attempt for ordinary phase notifications.
        launch_id (str | Unset): Retained launch identity, sent only once per boot to resolve attempt_id.
        phase (str | Unset):
    """

    attempt_id: str | Unset = UNSET
    launch_id: str | Unset = UNSET
    phase: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attempt_id = self.attempt_id

        launch_id = self.launch_id

        phase = self.phase

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attempt_id is not UNSET:
            field_dict["attempt_id"] = attempt_id
        if launch_id is not UNSET:
            field_dict["launch_id"] = launch_id
        if phase is not UNSET:
            field_dict["phase"] = phase

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attempt_id = d.pop("attempt_id", UNSET)

        launch_id = d.pop("launch_id", UNSET)

        phase = d.pop("phase", UNSET)

        runtime_progress_request = cls(
            attempt_id=attempt_id,
            launch_id=launch_id,
            phase=phase,
        )

        runtime_progress_request.additional_properties = d
        return runtime_progress_request

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
