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
            model (str):
            file (File):
            language (str | Unset):
            response_format (str | Unset):
     """

    model: str
    file: File
    language: str | Unset = UNSET
    response_format: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        model = self.model

        file = self.file.to_tuple()


        language = self.language

        response_format = self.response_format


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "model": model,
            "file": file,
        })
        if language is not UNSET:
            field_dict["language"] = language
        if response_format is not UNSET:
            field_dict["response_format"] = response_format

        return field_dict


    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("model", (None, str(self.model).encode(), "text/plain")))



        files.append(("file", self.file.to_tuple()))



        if not isinstance(self.language, Unset):
            files.append(("language", (None, str(self.language).encode(), "text/plain")))



        if not isinstance(self.response_format, Unset):
            files.append(("response_format", (None, str(self.response_format).encode(), "text/plain")))




        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))



        return files


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model = d.pop("model")

        file = File(
             payload = BytesIO(d.pop("file"))
        )




        language = d.pop("language", UNSET)

        response_format = d.pop("response_format", UNSET)

        post_v1_audio_transcriptions_body = cls(
            model=model,
            file=file,
            language=language,
            response_format=response_format,
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
