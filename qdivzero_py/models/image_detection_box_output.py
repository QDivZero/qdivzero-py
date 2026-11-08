from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImageDetectionBoxOutput")


@_attrs_define
class ImageDetectionBoxOutput:
    """
    Attributes:
        x1 (float | Unset):
        x2 (float | Unset):
        y1 (float | Unset):
        y2 (float | Unset):
    """

    x1: float | Unset = UNSET
    x2: float | Unset = UNSET
    y1: float | Unset = UNSET
    y2: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        x1 = self.x1

        x2 = self.x2

        y1 = self.y1

        y2 = self.y2

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if x1 is not UNSET:
            field_dict["x1"] = x1
        if x2 is not UNSET:
            field_dict["x2"] = x2
        if y1 is not UNSET:
            field_dict["y1"] = y1
        if y2 is not UNSET:
            field_dict["y2"] = y2

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        x1 = d.pop("x1", UNSET)

        x2 = d.pop("x2", UNSET)

        y1 = d.pop("y1", UNSET)

        y2 = d.pop("y2", UNSET)

        image_detection_box_output = cls(
            x1=x1,
            x2=x2,
            y1=y1,
            y2=y2,
        )

        image_detection_box_output.additional_properties = d
        return image_detection_box_output

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
