from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.detection_stream_error import DetectionStreamError
    from ..models.detection_stream_options import DetectionStreamOptions
    from ..models.image_detection_output import ImageDetectionOutput


T = TypeVar("T", bound="DetectionStreamEvent")


@_attrs_define
class DetectionStreamEvent:
    """
    Attributes:
        error (DetectionStreamError | Unset):
        frame_id (int | Unset):
        max_frame_bytes (int | Unset):
        model (str | Unset):
        options (DetectionStreamOptions | Unset):
        processing_ms (float | Unset):
        result (ImageDetectionOutput | Unset):
        status (int | Unset):
        type_ (str | Unset):
    """

    error: DetectionStreamError | Unset = UNSET
    frame_id: int | Unset = UNSET
    max_frame_bytes: int | Unset = UNSET
    model: str | Unset = UNSET
    options: DetectionStreamOptions | Unset = UNSET
    processing_ms: float | Unset = UNSET
    result: ImageDetectionOutput | Unset = UNSET
    status: int | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        frame_id = self.frame_id

        max_frame_bytes = self.max_frame_bytes

        model = self.model

        options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        processing_ms = self.processing_ms

        result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        status = self.status

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error
        if frame_id is not UNSET:
            field_dict["frame_id"] = frame_id
        if max_frame_bytes is not UNSET:
            field_dict["max_frame_bytes"] = max_frame_bytes
        if model is not UNSET:
            field_dict["model"] = model
        if options is not UNSET:
            field_dict["options"] = options
        if processing_ms is not UNSET:
            field_dict["processing_ms"] = processing_ms
        if result is not UNSET:
            field_dict["result"] = result
        if status is not UNSET:
            field_dict["status"] = status
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.detection_stream_error import DetectionStreamError
        from ..models.detection_stream_options import DetectionStreamOptions
        from ..models.image_detection_output import ImageDetectionOutput

        d = dict(src_dict)
        _error = d.pop("error", UNSET)
        error: DetectionStreamError | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = DetectionStreamError.from_dict(_error)

        frame_id = d.pop("frame_id", UNSET)

        max_frame_bytes = d.pop("max_frame_bytes", UNSET)

        model = d.pop("model", UNSET)

        _options = d.pop("options", UNSET)
        options: DetectionStreamOptions | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = DetectionStreamOptions.from_dict(_options)

        processing_ms = d.pop("processing_ms", UNSET)

        _result = d.pop("result", UNSET)
        result: ImageDetectionOutput | Unset
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = ImageDetectionOutput.from_dict(_result)

        status = d.pop("status", UNSET)

        type_ = d.pop("type", UNSET)

        detection_stream_event = cls(
            error=error,
            frame_id=frame_id,
            max_frame_bytes=max_frame_bytes,
            model=model,
            options=options,
            processing_ms=processing_ms,
            result=result,
            status=status,
            type_=type_,
        )

        detection_stream_event.additional_properties = d
        return detection_stream_event

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
