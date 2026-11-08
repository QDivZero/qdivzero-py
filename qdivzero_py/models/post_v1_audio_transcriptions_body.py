from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="PostV1AudioTranscriptionsBody")


@_attrs_define
class PostV1AudioTranscriptionsBody:
    """
    Attributes:
        file (File): Audio file
        model (str): Model ID
        language (str | Unset): Source language
        response_format (str | Unset): Response format: json, verbose_json, or diarized_json
        timestamp_granularities (str | Unset): Timestamp granularity (word or segment); requires verbose_json
    """

    file: File
    model: str
    language: str | Unset = UNSET
    response_format: str | Unset = UNSET
    timestamp_granularities: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file.to_tuple()

        model = self.model

        language = self.language

        response_format = self.response_format

        timestamp_granularities = self.timestamp_granularities

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
                "model": model,
            }
        )
        if language is not UNSET:
            field_dict["language"] = language
        if response_format is not UNSET:
            field_dict["response_format"] = response_format
        if timestamp_granularities is not UNSET:
            field_dict["timestamp_granularities[]"] = timestamp_granularities

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("file", self.file.to_tuple()))

        files.append(("model", (None, str(self.model).encode(), "text/plain")))

        if not isinstance(self.language, Unset):
            files.append(("language", (None, str(self.language).encode(), "text/plain")))

        if not isinstance(self.response_format, Unset):
            files.append(("response_format", (None, str(self.response_format).encode(), "text/plain")))

        if not isinstance(self.timestamp_granularities, Unset):
            files.append(
                ("timestamp_granularities[]", (None, str(self.timestamp_granularities).encode(), "text/plain"))
            )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file = File(payload=BytesIO(d.pop("file")))

        model = d.pop("model")

        language = d.pop("language", UNSET)

        response_format = d.pop("response_format", UNSET)

        timestamp_granularities = d.pop("timestamp_granularities[]", UNSET)

        post_v1_audio_transcriptions_body = cls(
            file=file,
            model=model,
            language=language,
            response_format=response_format,
            timestamp_granularities=timestamp_granularities,
        )

        post_v1_audio_transcriptions_body.additional_properties = d
        return post_v1_audio_transcriptions_body

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
