from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="PostV1ImageDetectionsBody")


@_attrs_define
class PostV1ImageDetectionsBody:
    """
    Attributes:
        image (File): PNG or JPEG image (maximum 16 MiB)
        model (str): Serving name or instance UUID
        classes (str | Unset): Comma-separated nonnegative class IDs
        confidence (float | Unset): Confidence threshold (0-1, default 0.25)
        image_size (int | Unset): Inference image size (32-2048, divisible by 32, default 640)
        iou (float | Unset): IoU threshold (0-1, default 0.7)
        max_detections (int | Unset): Maximum detections (1-1000, default 300)
    """

    image: File
    model: str
    classes: str | Unset = UNSET
    confidence: float | Unset = UNSET
    image_size: int | Unset = UNSET
    iou: float | Unset = UNSET
    max_detections: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image = self.image.to_tuple()

        model = self.model

        classes = self.classes

        confidence = self.confidence

        image_size = self.image_size

        iou = self.iou

        max_detections = self.max_detections

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "image": image,
                "model": model,
            }
        )
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

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("image", self.image.to_tuple()))

        files.append(("model", (None, str(self.model).encode(), "text/plain")))

        if not isinstance(self.classes, Unset):
            files.append(("classes", (None, str(self.classes).encode(), "text/plain")))

        if not isinstance(self.confidence, Unset):
            files.append(("confidence", (None, str(self.confidence).encode(), "text/plain")))

        if not isinstance(self.image_size, Unset):
            files.append(("image_size", (None, str(self.image_size).encode(), "text/plain")))

        if not isinstance(self.iou, Unset):
            files.append(("iou", (None, str(self.iou).encode(), "text/plain")))

        if not isinstance(self.max_detections, Unset):
            files.append(("max_detections", (None, str(self.max_detections).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        image = File(payload=BytesIO(d.pop("image")))

        model = d.pop("model")

        classes = d.pop("classes", UNSET)

        confidence = d.pop("confidence", UNSET)

        image_size = d.pop("image_size", UNSET)

        iou = d.pop("iou", UNSET)

        max_detections = d.pop("max_detections", UNSET)

        post_v1_image_detections_body = cls(
            image=image,
            model=model,
            classes=classes,
            confidence=confidence,
            image_size=image_size,
            iou=iou,
            max_detections=max_detections,
        )

        post_v1_image_detections_body.additional_properties = d
        return post_v1_image_detections_body

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
