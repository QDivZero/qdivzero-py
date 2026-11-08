from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DetectionStreamOptions")


@_attrs_define
class DetectionStreamOptions:
    """
    Attributes:
        classes (list[int] | Unset):
        confidence (float | Unset):
        image_size (int | Unset):
        iou (float | Unset):
        max_detections (int | Unset):
        tracking (bool | Unset):
    """

    classes: list[int] | Unset = UNSET
    confidence: float | Unset = UNSET
    image_size: int | Unset = UNSET
    iou: float | Unset = UNSET
    max_detections: int | Unset = UNSET
    tracking: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        classes: list[int] | Unset = UNSET
        if not isinstance(self.classes, Unset):
            classes = self.classes

        confidence = self.confidence

        image_size = self.image_size

        iou = self.iou

        max_detections = self.max_detections

        tracking = self.tracking

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if classes is not UNSET:
            field_dict["classes"] = classes
        if confidence is not UNSET:
            field_dict["confidence"] = confidence
        if image_size is not UNSET:
            field_dict["image_size"] = image_size
        if iou is not UNSET:
            field_dict["iou"] = iou
        if max_detections is not UNSET:
            field_dict["max_detections"] = max_detections
        if tracking is not UNSET:
            field_dict["tracking"] = tracking

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        classes = cast(list[int], d.pop("classes", UNSET))

        confidence = d.pop("confidence", UNSET)

        image_size = d.pop("image_size", UNSET)

        iou = d.pop("iou", UNSET)

        max_detections = d.pop("max_detections", UNSET)

        tracking = d.pop("tracking", UNSET)

        detection_stream_options = cls(
            classes=classes,
            confidence=confidence,
            image_size=image_size,
            iou=iou,
            max_detections=max_detections,
            tracking=tracking,
        )

        detection_stream_options.additional_properties = d
        return detection_stream_options

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
