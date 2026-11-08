from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateTutorialProgressRequest")


@_attrs_define
class UpdateTutorialProgressRequest:
    """
    Attributes:
        completed_step_ids (list[str] | Unset):
        content_version (int | Unset):
        state (str | Unset):
    """

    completed_step_ids: list[str] | Unset = UNSET
    content_version: int | Unset = UNSET
    state: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        completed_step_ids: list[str] | Unset = UNSET
        if not isinstance(self.completed_step_ids, Unset):
            completed_step_ids = self.completed_step_ids

        content_version = self.content_version

        state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if completed_step_ids is not UNSET:
            field_dict["completed_step_ids"] = completed_step_ids
        if content_version is not UNSET:
            field_dict["content_version"] = content_version
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        completed_step_ids = cast(list[str], d.pop("completed_step_ids", UNSET))

        content_version = d.pop("content_version", UNSET)

        state = d.pop("state", UNSET)

        update_tutorial_progress_request = cls(
            completed_step_ids=completed_step_ids,
            content_version=content_version,
            state=state,
        )

        update_tutorial_progress_request.additional_properties = d
        return update_tutorial_progress_request

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
