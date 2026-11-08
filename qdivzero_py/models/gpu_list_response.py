from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_gpu_response import CatalogGPUResponse


T = TypeVar("T", bound="GpuListResponse")


@_attrs_define
class GpuListResponse:
    """
    Attributes:
        gpus (list[CatalogGPUResponse] | Unset):
    """

    gpus: list[CatalogGPUResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gpus: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.gpus, Unset):
            gpus = []
            for gpus_item_data in self.gpus:
                gpus_item = gpus_item_data.to_dict()
                gpus.append(gpus_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gpus is not UNSET:
            field_dict["gpus"] = gpus

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.catalog_gpu_response import CatalogGPUResponse

        d = dict(src_dict)
        _gpus = d.pop("gpus", UNSET)
        gpus: list[CatalogGPUResponse] | Unset = UNSET
        if _gpus is not UNSET:
            gpus = []
            for gpus_item_data in _gpus:
                gpus_item = CatalogGPUResponse.from_dict(gpus_item_data)

                gpus.append(gpus_item)

        gpu_list_response = cls(
            gpus=gpus,
        )

        gpu_list_response.additional_properties = d
        return gpu_list_response

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
