from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_detection_result_output import ImageDetectionResultOutput


T = TypeVar("T", bound="ImageDetectionOutput")


@_attrs_define
class ImageDetectionOutput:
    """
    Attributes:
        detections (list[ImageDetectionResultOutput] | Unset):
        height (int | Unset):
        model (str | Unset):
        width (int | Unset):
    """

    detections: list[ImageDetectionResultOutput] | Unset = UNSET
    height: int | Unset = UNSET
    model: str | Unset = UNSET
    width: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        detections: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.detections, Unset):
            detections = []
            for detections_item_data in self.detections:
                detections_item = detections_item_data.to_dict()
                detections.append(detections_item)

        height = self.height

        model = self.model

        width = self.width

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if detections is not UNSET:
            field_dict["detections"] = detections
        if height is not UNSET:
            field_dict["height"] = height
        if model is not UNSET:
            field_dict["model"] = model
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_detection_result_output import ImageDetectionResultOutput

        d = dict(src_dict)
        _detections = d.pop("detections", UNSET)
        detections: list[ImageDetectionResultOutput] | Unset = UNSET
        if _detections is not UNSET:
            detections = []
            for detections_item_data in _detections:
                detections_item = ImageDetectionResultOutput.from_dict(detections_item_data)

                detections.append(detections_item)

        height = d.pop("height", UNSET)

        model = d.pop("model", UNSET)

        width = d.pop("width", UNSET)

        image_detection_output = cls(
            detections=detections,
            height=height,
            model=model,
            width=width,
        )

        image_detection_output.additional_properties = d
        return image_detection_output

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
