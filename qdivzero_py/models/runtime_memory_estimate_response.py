from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RuntimeMemoryEstimateResponse")


@_attrs_define
class RuntimeMemoryEstimateResponse:
    """
    Attributes:
        active_parameter_count (int | Unset):
        download_size_bytes (int | Unset):
        gpu_memory_utilization (float | Unset):
        kv_cache_vram_gb (float | Unset):
        model_vram_gb (float | Unset):
        parameter_count (int | Unset):
        per_gpu_required_vram_gb (float | Unset):
        required_vram_gb (float | Unset):
        tensor_parallel_size (int | Unset):
    """

    active_parameter_count: int | Unset = UNSET
    download_size_bytes: int | Unset = UNSET
    gpu_memory_utilization: float | Unset = UNSET
    kv_cache_vram_gb: float | Unset = UNSET
    model_vram_gb: float | Unset = UNSET
    parameter_count: int | Unset = UNSET
    per_gpu_required_vram_gb: float | Unset = UNSET
    required_vram_gb: float | Unset = UNSET
    tensor_parallel_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active_parameter_count = self.active_parameter_count

        download_size_bytes = self.download_size_bytes

        gpu_memory_utilization = self.gpu_memory_utilization

        kv_cache_vram_gb = self.kv_cache_vram_gb

        model_vram_gb = self.model_vram_gb

        parameter_count = self.parameter_count

        per_gpu_required_vram_gb = self.per_gpu_required_vram_gb

        required_vram_gb = self.required_vram_gb

        tensor_parallel_size = self.tensor_parallel_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active_parameter_count is not UNSET:
            field_dict["active_parameter_count"] = active_parameter_count
        if download_size_bytes is not UNSET:
            field_dict["download_size_bytes"] = download_size_bytes
        if gpu_memory_utilization is not UNSET:
            field_dict["gpu_memory_utilization"] = gpu_memory_utilization
        if kv_cache_vram_gb is not UNSET:
            field_dict["kv_cache_vram_gb"] = kv_cache_vram_gb
        if model_vram_gb is not UNSET:
            field_dict["model_vram_gb"] = model_vram_gb
        if parameter_count is not UNSET:
            field_dict["parameter_count"] = parameter_count
        if per_gpu_required_vram_gb is not UNSET:
            field_dict["per_gpu_required_vram_gb"] = per_gpu_required_vram_gb
        if required_vram_gb is not UNSET:
            field_dict["required_vram_gb"] = required_vram_gb
        if tensor_parallel_size is not UNSET:
            field_dict["tensor_parallel_size"] = tensor_parallel_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active_parameter_count = d.pop("active_parameter_count", UNSET)

        download_size_bytes = d.pop("download_size_bytes", UNSET)

        gpu_memory_utilization = d.pop("gpu_memory_utilization", UNSET)

        kv_cache_vram_gb = d.pop("kv_cache_vram_gb", UNSET)

        model_vram_gb = d.pop("model_vram_gb", UNSET)

        parameter_count = d.pop("parameter_count", UNSET)

        per_gpu_required_vram_gb = d.pop("per_gpu_required_vram_gb", UNSET)

        required_vram_gb = d.pop("required_vram_gb", UNSET)

        tensor_parallel_size = d.pop("tensor_parallel_size", UNSET)

        runtime_memory_estimate_response = cls(
            active_parameter_count=active_parameter_count,
            download_size_bytes=download_size_bytes,
            gpu_memory_utilization=gpu_memory_utilization,
            kv_cache_vram_gb=kv_cache_vram_gb,
            model_vram_gb=model_vram_gb,
            parameter_count=parameter_count,
            per_gpu_required_vram_gb=per_gpu_required_vram_gb,
            required_vram_gb=required_vram_gb,
            tensor_parallel_size=tensor_parallel_size,
        )

        runtime_memory_estimate_response.additional_properties = d
        return runtime_memory_estimate_response

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
