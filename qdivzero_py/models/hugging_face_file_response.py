from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HuggingFaceFileResponse")


@_attrs_define
class HuggingFaceFileResponse:
    """
    Attributes:
        filename (str | Unset):
        quantization (str | Unset):
        size_bytes (int | Unset):
    """

    filename: str | Unset = UNSET
    quantization: str | Unset = UNSET
    size_bytes: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filename = self.filename

        quantization = self.quantization

        size_bytes = self.size_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filename is not UNSET:
            field_dict["filename"] = filename
        if quantization is not UNSET:
            field_dict["quantization"] = quantization
        if size_bytes is not UNSET:
            field_dict["size_bytes"] = size_bytes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        filename = d.pop("filename", UNSET)

        quantization = d.pop("quantization", UNSET)

        size_bytes = d.pop("size_bytes", UNSET)

        hugging_face_file_response = cls(
            filename=filename,
            quantization=quantization,
            size_bytes=size_bytes,
        )

        hugging_face_file_response.additional_properties = d
        return hugging_face_file_response

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
