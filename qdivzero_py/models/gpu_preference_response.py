from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GpuPreferenceResponse")


@_attrs_define
class GpuPreferenceResponse:
    """
    Attributes:
        count (int | Unset):
        provider_codename (str | Unset):
        public_gpu_id (str | Unset):
    """

    count: int | Unset = UNSET
    provider_codename: str | Unset = UNSET
    public_gpu_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        provider_codename = self.provider_codename

        public_gpu_id = self.public_gpu_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if provider_codename is not UNSET:
            field_dict["provider_codename"] = provider_codename
        if public_gpu_id is not UNSET:
            field_dict["public_gpu_id"] = public_gpu_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count", UNSET)

        provider_codename = d.pop("provider_codename", UNSET)

        public_gpu_id = d.pop("public_gpu_id", UNSET)

        gpu_preference_response = cls(
            count=count,
            provider_codename=provider_codename,
            public_gpu_id=public_gpu_id,
        )

        gpu_preference_response.additional_properties = d
        return gpu_preference_response

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
