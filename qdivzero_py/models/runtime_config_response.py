from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.runtime_config_response_storage_mounts_item import RuntimeConfigResponseStorageMountsItem


T = TypeVar("T", bound="RuntimeConfigResponse")


@_attrs_define
class RuntimeConfigResponse:
    """
    Attributes:
        context_size (int | Unset):
        dtype (str | Unset):
        duplex (bool | Unset):
        enable_chunked_prefill (bool | Unset):
        enable_prefix_caching (bool | Unset):
        gpu_memory_utilization (float | Unset):
        kv_cache_dtype (str | Unset):
        max_num_batched_tokens (int | Unset):
        max_num_seqs (int | Unset):
        profile (str | Unset):
        quantization (str | Unset):
        storage_mounts (list[RuntimeConfigResponseStorageMountsItem] | Unset):
        task_type (str | Unset):
        tensor_parallel_size (int | Unset):
        yolo_model_file (str | Unset):
    """

    context_size: int | Unset = UNSET
    dtype: str | Unset = UNSET
    duplex: bool | Unset = UNSET
    enable_chunked_prefill: bool | Unset = UNSET
    enable_prefix_caching: bool | Unset = UNSET
    gpu_memory_utilization: float | Unset = UNSET
    kv_cache_dtype: str | Unset = UNSET
    max_num_batched_tokens: int | Unset = UNSET
    max_num_seqs: int | Unset = UNSET
    profile: str | Unset = UNSET
    quantization: str | Unset = UNSET
    storage_mounts: list[RuntimeConfigResponseStorageMountsItem] | Unset = UNSET
    task_type: str | Unset = UNSET
    tensor_parallel_size: int | Unset = UNSET
    yolo_model_file: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        context_size = self.context_size

        dtype = self.dtype

        duplex = self.duplex

        enable_chunked_prefill = self.enable_chunked_prefill

        enable_prefix_caching = self.enable_prefix_caching

        gpu_memory_utilization = self.gpu_memory_utilization

        kv_cache_dtype = self.kv_cache_dtype

        max_num_batched_tokens = self.max_num_batched_tokens

        max_num_seqs = self.max_num_seqs

        profile = self.profile

        quantization = self.quantization

        storage_mounts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.storage_mounts, Unset):
            storage_mounts = []
            for storage_mounts_item_data in self.storage_mounts:
                storage_mounts_item = storage_mounts_item_data.to_dict()
                storage_mounts.append(storage_mounts_item)

        task_type = self.task_type

        tensor_parallel_size = self.tensor_parallel_size

        yolo_model_file = self.yolo_model_file

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if context_size is not UNSET:
            field_dict["context_size"] = context_size
        if dtype is not UNSET:
            field_dict["dtype"] = dtype
        if duplex is not UNSET:
            field_dict["duplex"] = duplex
        if enable_chunked_prefill is not UNSET:
            field_dict["enable_chunked_prefill"] = enable_chunked_prefill
        if enable_prefix_caching is not UNSET:
            field_dict["enable_prefix_caching"] = enable_prefix_caching
        if gpu_memory_utilization is not UNSET:
            field_dict["gpu_memory_utilization"] = gpu_memory_utilization
        if kv_cache_dtype is not UNSET:
            field_dict["kv_cache_dtype"] = kv_cache_dtype
        if max_num_batched_tokens is not UNSET:
            field_dict["max_num_batched_tokens"] = max_num_batched_tokens
        if max_num_seqs is not UNSET:
            field_dict["max_num_seqs"] = max_num_seqs
        if profile is not UNSET:
            field_dict["profile"] = profile
        if quantization is not UNSET:
            field_dict["quantization"] = quantization
        if storage_mounts is not UNSET:
            field_dict["storage_mounts"] = storage_mounts
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if tensor_parallel_size is not UNSET:
            field_dict["tensor_parallel_size"] = tensor_parallel_size
        if yolo_model_file is not UNSET:
            field_dict["yolo_model_file"] = yolo_model_file

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.runtime_config_response_storage_mounts_item import RuntimeConfigResponseStorageMountsItem

        d = dict(src_dict)
        context_size = d.pop("context_size", UNSET)

        dtype = d.pop("dtype", UNSET)

        duplex = d.pop("duplex", UNSET)

        enable_chunked_prefill = d.pop("enable_chunked_prefill", UNSET)

        enable_prefix_caching = d.pop("enable_prefix_caching", UNSET)

        gpu_memory_utilization = d.pop("gpu_memory_utilization", UNSET)

        kv_cache_dtype = d.pop("kv_cache_dtype", UNSET)

        max_num_batched_tokens = d.pop("max_num_batched_tokens", UNSET)

        max_num_seqs = d.pop("max_num_seqs", UNSET)

        profile = d.pop("profile", UNSET)

        quantization = d.pop("quantization", UNSET)

        _storage_mounts = d.pop("storage_mounts", UNSET)
        storage_mounts: list[RuntimeConfigResponseStorageMountsItem] | Unset = UNSET
        if _storage_mounts is not UNSET:
            storage_mounts = []
            for storage_mounts_item_data in _storage_mounts:
                storage_mounts_item = RuntimeConfigResponseStorageMountsItem.from_dict(storage_mounts_item_data)

                storage_mounts.append(storage_mounts_item)

        task_type = d.pop("task_type", UNSET)

        tensor_parallel_size = d.pop("tensor_parallel_size", UNSET)

        yolo_model_file = d.pop("yolo_model_file", UNSET)

        runtime_config_response = cls(
            context_size=context_size,
            dtype=dtype,
            duplex=duplex,
            enable_chunked_prefill=enable_chunked_prefill,
            enable_prefix_caching=enable_prefix_caching,
            gpu_memory_utilization=gpu_memory_utilization,
            kv_cache_dtype=kv_cache_dtype,
            max_num_batched_tokens=max_num_batched_tokens,
            max_num_seqs=max_num_seqs,
            profile=profile,
            quantization=quantization,
            storage_mounts=storage_mounts,
            task_type=task_type,
            tensor_parallel_size=tensor_parallel_size,
            yolo_model_file=yolo_model_file,
        )

        runtime_config_response.additional_properties = d
        return runtime_config_response

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
