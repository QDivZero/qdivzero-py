from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RecommendedGPU")


@_attrs_define
class RecommendedGPU:
    """
    Attributes:
        availability (str | Unset):
        display_name (str | Unset):
        gpu_count (int | Unset):
        market_type (str | Unset):
        vram_gb (float | Unset):
    """

    availability: str | Unset = UNSET
    display_name: str | Unset = UNSET
    gpu_count: int | Unset = UNSET
    market_type: str | Unset = UNSET
    vram_gb: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        availability = self.availability

        display_name = self.display_name

        gpu_count = self.gpu_count

        market_type = self.market_type

        vram_gb = self.vram_gb

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if availability is not UNSET:
            field_dict["availability"] = availability
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if gpu_count is not UNSET:
            field_dict["gpu_count"] = gpu_count
        if market_type is not UNSET:
            field_dict["market_type"] = market_type
        if vram_gb is not UNSET:
            field_dict["vram_gb"] = vram_gb

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        availability = d.pop("availability", UNSET)

        display_name = d.pop("display_name", UNSET)

        gpu_count = d.pop("gpu_count", UNSET)

        market_type = d.pop("market_type", UNSET)

        vram_gb = d.pop("vram_gb", UNSET)

        recommended_gpu = cls(
            availability=availability,
            display_name=display_name,
            gpu_count=gpu_count,
            market_type=market_type,
            vram_gb=vram_gb,
        )

        recommended_gpu.additional_properties = d
        return recommended_gpu

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
