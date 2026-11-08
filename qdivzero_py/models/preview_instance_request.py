from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.preview_instance_request_workload_kind import PreviewInstanceRequestWorkloadKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.runtime_config_request import RuntimeConfigRequest


T = TypeVar("T", bound="PreviewInstanceRequest")


@_attrs_define
class PreviewInstanceRequest:
    """
    Attributes:
        download_size_bytes (int | Unset):
        gguf_model_path (str | Unset):
        huggingface_repo_id (str | Unset):
        runtime_config (RuntimeConfigRequest | Unset):
        runtime_preset (str | Unset):
        scheduling_mode (str | Unset):
        smart_allow_community (bool | Unset):
        smart_allow_spot (bool | Unset):
        smart_max_price_per_hour_eur (float | Unset):
        smart_min_gpu_class (str | Unset):
        smart_min_total_tflops (float | Unset):
        smart_provider_filter_mode (str | Unset):
        smart_provider_preference (str | Unset):
        smart_region (str | Unset):
        smart_regions (list[str] | Unset):
        smart_selection_label (str | Unset):
        workload_kind (PreviewInstanceRequestWorkloadKind | Unset):
    """

    download_size_bytes: int | Unset = UNSET
    gguf_model_path: str | Unset = UNSET
    huggingface_repo_id: str | Unset = UNSET
    runtime_config: RuntimeConfigRequest | Unset = UNSET
    runtime_preset: str | Unset = UNSET
    scheduling_mode: str | Unset = UNSET
    smart_allow_community: bool | Unset = UNSET
    smart_allow_spot: bool | Unset = UNSET
    smart_max_price_per_hour_eur: float | Unset = UNSET
    smart_min_gpu_class: str | Unset = UNSET
    smart_min_total_tflops: float | Unset = UNSET
    smart_provider_filter_mode: str | Unset = UNSET
    smart_provider_preference: str | Unset = UNSET
    smart_region: str | Unset = UNSET
    smart_regions: list[str] | Unset = UNSET
    smart_selection_label: str | Unset = UNSET
    workload_kind: PreviewInstanceRequestWorkloadKind | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        download_size_bytes = self.download_size_bytes

        gguf_model_path = self.gguf_model_path

        huggingface_repo_id = self.huggingface_repo_id

        runtime_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.runtime_config, Unset):
            runtime_config = self.runtime_config.to_dict()

        runtime_preset = self.runtime_preset

        scheduling_mode = self.scheduling_mode

        smart_allow_community = self.smart_allow_community

        smart_allow_spot = self.smart_allow_spot

        smart_max_price_per_hour_eur = self.smart_max_price_per_hour_eur

        smart_min_gpu_class = self.smart_min_gpu_class

        smart_min_total_tflops = self.smart_min_total_tflops

        smart_provider_filter_mode = self.smart_provider_filter_mode

        smart_provider_preference = self.smart_provider_preference

        smart_region = self.smart_region

        smart_regions: list[str] | Unset = UNSET
        if not isinstance(self.smart_regions, Unset):
            smart_regions = self.smart_regions

        smart_selection_label = self.smart_selection_label

        workload_kind: str | Unset = UNSET
        if not isinstance(self.workload_kind, Unset):
            workload_kind = self.workload_kind.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if download_size_bytes is not UNSET:
            field_dict["download_size_bytes"] = download_size_bytes
        if gguf_model_path is not UNSET:
            field_dict["gguf_model_path"] = gguf_model_path
        if huggingface_repo_id is not UNSET:
            field_dict["huggingface_repo_id"] = huggingface_repo_id
        if runtime_config is not UNSET:
            field_dict["runtime_config"] = runtime_config
        if runtime_preset is not UNSET:
            field_dict["runtime_preset"] = runtime_preset
        if scheduling_mode is not UNSET:
            field_dict["scheduling_mode"] = scheduling_mode
        if smart_allow_community is not UNSET:
            field_dict["smart_allow_community"] = smart_allow_community
        if smart_allow_spot is not UNSET:
            field_dict["smart_allow_spot"] = smart_allow_spot
        if smart_max_price_per_hour_eur is not UNSET:
            field_dict["smart_max_price_per_hour_eur"] = smart_max_price_per_hour_eur
        if smart_min_gpu_class is not UNSET:
            field_dict["smart_min_gpu_class"] = smart_min_gpu_class
        if smart_min_total_tflops is not UNSET:
            field_dict["smart_min_total_tflops"] = smart_min_total_tflops
        if smart_provider_filter_mode is not UNSET:
            field_dict["smart_provider_filter_mode"] = smart_provider_filter_mode
        if smart_provider_preference is not UNSET:
            field_dict["smart_provider_preference"] = smart_provider_preference
        if smart_region is not UNSET:
            field_dict["smart_region"] = smart_region
        if smart_regions is not UNSET:
            field_dict["smart_regions"] = smart_regions
        if smart_selection_label is not UNSET:
            field_dict["smart_selection_label"] = smart_selection_label
        if workload_kind is not UNSET:
            field_dict["workload_kind"] = workload_kind

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.runtime_config_request import RuntimeConfigRequest

        d = dict(src_dict)
        download_size_bytes = d.pop("download_size_bytes", UNSET)

        gguf_model_path = d.pop("gguf_model_path", UNSET)

        huggingface_repo_id = d.pop("huggingface_repo_id", UNSET)

        _runtime_config = d.pop("runtime_config", UNSET)
        runtime_config: RuntimeConfigRequest | Unset
        if isinstance(_runtime_config, Unset):
            runtime_config = UNSET
        else:
            runtime_config = RuntimeConfigRequest.from_dict(_runtime_config)

        runtime_preset = d.pop("runtime_preset", UNSET)

        scheduling_mode = d.pop("scheduling_mode", UNSET)

        smart_allow_community = d.pop("smart_allow_community", UNSET)

        smart_allow_spot = d.pop("smart_allow_spot", UNSET)

        smart_max_price_per_hour_eur = d.pop("smart_max_price_per_hour_eur", UNSET)

        smart_min_gpu_class = d.pop("smart_min_gpu_class", UNSET)

        smart_min_total_tflops = d.pop("smart_min_total_tflops", UNSET)

        smart_provider_filter_mode = d.pop("smart_provider_filter_mode", UNSET)

        smart_provider_preference = d.pop("smart_provider_preference", UNSET)

        smart_region = d.pop("smart_region", UNSET)

        smart_regions = cast(list[str], d.pop("smart_regions", UNSET))

        smart_selection_label = d.pop("smart_selection_label", UNSET)

        _workload_kind = d.pop("workload_kind", UNSET)
        workload_kind: PreviewInstanceRequestWorkloadKind | Unset
        if isinstance(_workload_kind, Unset):
            workload_kind = UNSET
        else:
            workload_kind = PreviewInstanceRequestWorkloadKind(_workload_kind)

        preview_instance_request = cls(
            download_size_bytes=download_size_bytes,
            gguf_model_path=gguf_model_path,
            huggingface_repo_id=huggingface_repo_id,
            runtime_config=runtime_config,
            runtime_preset=runtime_preset,
            scheduling_mode=scheduling_mode,
            smart_allow_community=smart_allow_community,
            smart_allow_spot=smart_allow_spot,
            smart_max_price_per_hour_eur=smart_max_price_per_hour_eur,
            smart_min_gpu_class=smart_min_gpu_class,
            smart_min_total_tflops=smart_min_total_tflops,
            smart_provider_filter_mode=smart_provider_filter_mode,
            smart_provider_preference=smart_provider_preference,
            smart_region=smart_region,
            smart_regions=smart_regions,
            smart_selection_label=smart_selection_label,
            workload_kind=workload_kind,
        )

        preview_instance_request.additional_properties = d
        return preview_instance_request

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
