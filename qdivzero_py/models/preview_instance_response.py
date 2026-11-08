from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_gpu_response import CatalogGPUResponse
    from ..models.runtime_config_response import RuntimeConfigResponse
    from ..models.runtime_memory_estimate_response import RuntimeMemoryEstimateResponse


T = TypeVar("T", bound="PreviewInstanceResponse")


@_attrs_define
class PreviewInstanceResponse:
    """
    Attributes:
        capacity_tier (str | Unset):
        compatible_gpus (list[CatalogGPUResponse] | Unset):
        estimate (RuntimeMemoryEstimateResponse | Unset):
        huggingface_repo_id (str | Unset):
        max_context_size (int | Unset):
        recommended_gpu (CatalogGPUResponse | Unset):
        runtime_config (RuntimeConfigResponse | Unset):
        runtime_preset (str | Unset):
        scheduling_mode (str | Unset):
        smart_allow_community (bool | Unset):
        smart_allow_spot (bool | Unset):
        smart_current_gpu (CatalogGPUResponse | Unset):
        smart_current_price_per_hour_eur (float | Unset):
        smart_max_price_per_hour_eur (float | Unset):
        smart_min_gpu_class (str | Unset):
        smart_min_total_tflops (float | Unset):
        smart_provider_filter_mode (str | Unset):
        smart_provider_preference (str | Unset):
        smart_recommended_max_price_per_hour_eur (float | Unset):
        smart_region (str | Unset):
        smart_regions (list[str] | Unset):
        smart_selection_label (str | Unset):
        warnings (list[str] | Unset):
        workload_kind (str | Unset):
    """

    capacity_tier: str | Unset = UNSET
    compatible_gpus: list[CatalogGPUResponse] | Unset = UNSET
    estimate: RuntimeMemoryEstimateResponse | Unset = UNSET
    huggingface_repo_id: str | Unset = UNSET
    max_context_size: int | Unset = UNSET
    recommended_gpu: CatalogGPUResponse | Unset = UNSET
    runtime_config: RuntimeConfigResponse | Unset = UNSET
    runtime_preset: str | Unset = UNSET
    scheduling_mode: str | Unset = UNSET
    smart_allow_community: bool | Unset = UNSET
    smart_allow_spot: bool | Unset = UNSET
    smart_current_gpu: CatalogGPUResponse | Unset = UNSET
    smart_current_price_per_hour_eur: float | Unset = UNSET
    smart_max_price_per_hour_eur: float | Unset = UNSET
    smart_min_gpu_class: str | Unset = UNSET
    smart_min_total_tflops: float | Unset = UNSET
    smart_provider_filter_mode: str | Unset = UNSET
    smart_provider_preference: str | Unset = UNSET
    smart_recommended_max_price_per_hour_eur: float | Unset = UNSET
    smart_region: str | Unset = UNSET
    smart_regions: list[str] | Unset = UNSET
    smart_selection_label: str | Unset = UNSET
    warnings: list[str] | Unset = UNSET
    workload_kind: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        capacity_tier = self.capacity_tier

        compatible_gpus: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.compatible_gpus, Unset):
            compatible_gpus = []
            for compatible_gpus_item_data in self.compatible_gpus:
                compatible_gpus_item = compatible_gpus_item_data.to_dict()
                compatible_gpus.append(compatible_gpus_item)

        estimate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimate, Unset):
            estimate = self.estimate.to_dict()

        huggingface_repo_id = self.huggingface_repo_id

        max_context_size = self.max_context_size

        recommended_gpu: dict[str, Any] | Unset = UNSET
        if not isinstance(self.recommended_gpu, Unset):
            recommended_gpu = self.recommended_gpu.to_dict()

        runtime_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.runtime_config, Unset):
            runtime_config = self.runtime_config.to_dict()

        runtime_preset = self.runtime_preset

        scheduling_mode = self.scheduling_mode

        smart_allow_community = self.smart_allow_community

        smart_allow_spot = self.smart_allow_spot

        smart_current_gpu: dict[str, Any] | Unset = UNSET
        if not isinstance(self.smart_current_gpu, Unset):
            smart_current_gpu = self.smart_current_gpu.to_dict()

        smart_current_price_per_hour_eur = self.smart_current_price_per_hour_eur

        smart_max_price_per_hour_eur = self.smart_max_price_per_hour_eur

        smart_min_gpu_class = self.smart_min_gpu_class

        smart_min_total_tflops = self.smart_min_total_tflops

        smart_provider_filter_mode = self.smart_provider_filter_mode

        smart_provider_preference = self.smart_provider_preference

        smart_recommended_max_price_per_hour_eur = self.smart_recommended_max_price_per_hour_eur

        smart_region = self.smart_region

        smart_regions: list[str] | Unset = UNSET
        if not isinstance(self.smart_regions, Unset):
            smart_regions = self.smart_regions

        smart_selection_label = self.smart_selection_label

        warnings: list[str] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        workload_kind = self.workload_kind

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if capacity_tier is not UNSET:
            field_dict["capacity_tier"] = capacity_tier
        if compatible_gpus is not UNSET:
            field_dict["compatible_gpus"] = compatible_gpus
        if estimate is not UNSET:
            field_dict["estimate"] = estimate
        if huggingface_repo_id is not UNSET:
            field_dict["huggingface_repo_id"] = huggingface_repo_id
        if max_context_size is not UNSET:
            field_dict["max_context_size"] = max_context_size
        if recommended_gpu is not UNSET:
            field_dict["recommended_gpu"] = recommended_gpu
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
        if smart_current_gpu is not UNSET:
            field_dict["smart_current_gpu"] = smart_current_gpu
        if smart_current_price_per_hour_eur is not UNSET:
            field_dict["smart_current_price_per_hour_eur"] = smart_current_price_per_hour_eur
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
        if smart_recommended_max_price_per_hour_eur is not UNSET:
            field_dict["smart_recommended_max_price_per_hour_eur"] = smart_recommended_max_price_per_hour_eur
        if smart_region is not UNSET:
            field_dict["smart_region"] = smart_region
        if smart_regions is not UNSET:
            field_dict["smart_regions"] = smart_regions
        if smart_selection_label is not UNSET:
            field_dict["smart_selection_label"] = smart_selection_label
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if workload_kind is not UNSET:
            field_dict["workload_kind"] = workload_kind

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.catalog_gpu_response import CatalogGPUResponse
        from ..models.runtime_config_response import RuntimeConfigResponse
        from ..models.runtime_memory_estimate_response import RuntimeMemoryEstimateResponse

        d = dict(src_dict)
        capacity_tier = d.pop("capacity_tier", UNSET)

        _compatible_gpus = d.pop("compatible_gpus", UNSET)
        compatible_gpus: list[CatalogGPUResponse] | Unset = UNSET
        if _compatible_gpus is not UNSET:
            compatible_gpus = []
            for compatible_gpus_item_data in _compatible_gpus:
                compatible_gpus_item = CatalogGPUResponse.from_dict(compatible_gpus_item_data)

                compatible_gpus.append(compatible_gpus_item)

        _estimate = d.pop("estimate", UNSET)
        estimate: RuntimeMemoryEstimateResponse | Unset
        if isinstance(_estimate, Unset):
            estimate = UNSET
        else:
            estimate = RuntimeMemoryEstimateResponse.from_dict(_estimate)

        huggingface_repo_id = d.pop("huggingface_repo_id", UNSET)

        max_context_size = d.pop("max_context_size", UNSET)

        _recommended_gpu = d.pop("recommended_gpu", UNSET)
        recommended_gpu: CatalogGPUResponse | Unset
        if isinstance(_recommended_gpu, Unset):
            recommended_gpu = UNSET
        else:
            recommended_gpu = CatalogGPUResponse.from_dict(_recommended_gpu)

        _runtime_config = d.pop("runtime_config", UNSET)
        runtime_config: RuntimeConfigResponse | Unset
        if isinstance(_runtime_config, Unset):
            runtime_config = UNSET
        else:
            runtime_config = RuntimeConfigResponse.from_dict(_runtime_config)

        runtime_preset = d.pop("runtime_preset", UNSET)

        scheduling_mode = d.pop("scheduling_mode", UNSET)

        smart_allow_community = d.pop("smart_allow_community", UNSET)

        smart_allow_spot = d.pop("smart_allow_spot", UNSET)

        _smart_current_gpu = d.pop("smart_current_gpu", UNSET)
        smart_current_gpu: CatalogGPUResponse | Unset
        if isinstance(_smart_current_gpu, Unset):
            smart_current_gpu = UNSET
        else:
            smart_current_gpu = CatalogGPUResponse.from_dict(_smart_current_gpu)

        smart_current_price_per_hour_eur = d.pop("smart_current_price_per_hour_eur", UNSET)

        smart_max_price_per_hour_eur = d.pop("smart_max_price_per_hour_eur", UNSET)

        smart_min_gpu_class = d.pop("smart_min_gpu_class", UNSET)

        smart_min_total_tflops = d.pop("smart_min_total_tflops", UNSET)

        smart_provider_filter_mode = d.pop("smart_provider_filter_mode", UNSET)

        smart_provider_preference = d.pop("smart_provider_preference", UNSET)

        smart_recommended_max_price_per_hour_eur = d.pop("smart_recommended_max_price_per_hour_eur", UNSET)

        smart_region = d.pop("smart_region", UNSET)

        smart_regions = cast(list[str], d.pop("smart_regions", UNSET))

        smart_selection_label = d.pop("smart_selection_label", UNSET)

        warnings = cast(list[str], d.pop("warnings", UNSET))

        workload_kind = d.pop("workload_kind", UNSET)

        preview_instance_response = cls(
            capacity_tier=capacity_tier,
            compatible_gpus=compatible_gpus,
            estimate=estimate,
            huggingface_repo_id=huggingface_repo_id,
            max_context_size=max_context_size,
            recommended_gpu=recommended_gpu,
            runtime_config=runtime_config,
            runtime_preset=runtime_preset,
            scheduling_mode=scheduling_mode,
            smart_allow_community=smart_allow_community,
            smart_allow_spot=smart_allow_spot,
            smart_current_gpu=smart_current_gpu,
            smart_current_price_per_hour_eur=smart_current_price_per_hour_eur,
            smart_max_price_per_hour_eur=smart_max_price_per_hour_eur,
            smart_min_gpu_class=smart_min_gpu_class,
            smart_min_total_tflops=smart_min_total_tflops,
            smart_provider_filter_mode=smart_provider_filter_mode,
            smart_provider_preference=smart_provider_preference,
            smart_recommended_max_price_per_hour_eur=smart_recommended_max_price_per_hour_eur,
            smart_region=smart_region,
            smart_regions=smart_regions,
            smart_selection_label=smart_selection_label,
            warnings=warnings,
            workload_kind=workload_kind,
        )

        preview_instance_response.additional_properties = d
        return preview_instance_response

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
