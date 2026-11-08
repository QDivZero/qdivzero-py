from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_detection_box_output import ImageDetectionBoxOutput
    from ..models.image_detection_keypoint_output import ImageDetectionKeypointOutput


T = TypeVar("T", bound="ImageDetectionResultOutput")


@_attrs_define
class ImageDetectionResultOutput:
    """
    Attributes:
        box (ImageDetectionBoxOutput | Unset):
        class_id (int | Unset):
        class_name (str | Unset):
        confidence (float | Unset):
        keypoints (list[ImageDetectionKeypointOutput] | Unset):
        track_id (int | Unset):
    """

    box: ImageDetectionBoxOutput | Unset = UNSET
    class_id: int | Unset = UNSET
    class_name: str | Unset = UNSET
    confidence: float | Unset = UNSET
    keypoints: list[ImageDetectionKeypointOutput] | Unset = UNSET
    track_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        box: dict[str, Any] | Unset = UNSET
        if not isinstance(self.box, Unset):
            box = self.box.to_dict()

        class_id = self.class_id

        class_name = self.class_name

        confidence = self.confidence

        keypoints: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.keypoints, Unset):
            keypoints = []
            for keypoints_item_data in self.keypoints:
                keypoints_item = keypoints_item_data.to_dict()
                keypoints.append(keypoints_item)

        track_id = self.track_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if box is not UNSET:
            field_dict["box"] = box
        if class_id is not UNSET:
            field_dict["class_id"] = class_id
        if class_name is not UNSET:
            field_dict["class_name"] = class_name
        if confidence is not UNSET:
            field_dict["confidence"] = confidence
        if keypoints is not UNSET:
            field_dict["keypoints"] = keypoints
        if track_id is not UNSET:
            field_dict["track_id"] = track_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_detection_box_output import ImageDetectionBoxOutput
        from ..models.image_detection_keypoint_output import ImageDetectionKeypointOutput

        d = dict(src_dict)
        _box = d.pop("box", UNSET)
        box: ImageDetectionBoxOutput | Unset
        if isinstance(_box, Unset):
            box = UNSET
        else:
            box = ImageDetectionBoxOutput.from_dict(_box)

        class_id = d.pop("class_id", UNSET)

        class_name = d.pop("class_name", UNSET)

        confidence = d.pop("confidence", UNSET)

        _keypoints = d.pop("keypoints", UNSET)
        keypoints: list[ImageDetectionKeypointOutput] | Unset = UNSET
        if _keypoints is not UNSET:
            keypoints = []
            for keypoints_item_data in _keypoints:
                keypoints_item = ImageDetectionKeypointOutput.from_dict(keypoints_item_data)

                keypoints.append(keypoints_item)

        track_id = d.pop("track_id", UNSET)

        image_detection_result_output = cls(
            box=box,
            class_id=class_id,
            class_name=class_name,
            confidence=confidence,
            keypoints=keypoints,
            track_id=track_id,
        )

        image_detection_result_output.additional_properties = d
        return image_detection_result_output

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
