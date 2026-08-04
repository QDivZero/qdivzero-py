from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.gpu_preference_response import GpuPreferenceResponse





T = TypeVar("T", bound="InstanceResponse")



@_attrs_define
class InstanceResponse:
    """ 
        Attributes:
            account_id (str | Unset):
            capacity_tier (str | Unset):
            created_at (str | Unset):
            description (str | Unset):
            estimated_required_vram_gb (float | Unset):
            failure_reason (str | Unset):
            gpu_count (int | Unset):
            gpu_preferences (list[GpuPreferenceResponse] | Unset):
            huggingface_repo_id (str | Unset):
            id (str | Unset):
            idle_timeout_seconds (int | Unset):
            last_request_at (str | Unset):
            name (str | Unset):
            public_gpu_id (str | Unset):
            public_price_per_hour_eur (float | Unset):
            replica_set_id (str | Unset):
            runtime_config_snapshot (str | Unset):
            runtime_preset (str | Unset):
            scheduling_mode (str | Unset):
            serverless_enabled (bool | Unset):
            serving_name (str | Unset):
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
            started_at (str | Unset):
            state (str | Unset):
            stopped_at (str | Unset):
            workload_kind (str | Unset):
     """

    account_id: str | Unset = UNSET
    capacity_tier: str | Unset = UNSET
    created_at: str | Unset = UNSET
    description: str | Unset = UNSET
    estimated_required_vram_gb: float | Unset = UNSET
    failure_reason: str | Unset = UNSET
    gpu_count: int | Unset = UNSET
    gpu_preferences: list[GpuPreferenceResponse] | Unset = UNSET
    huggingface_repo_id: str | Unset = UNSET
    id: str | Unset = UNSET
    idle_timeout_seconds: int | Unset = UNSET
    last_request_at: str | Unset = UNSET
    name: str | Unset = UNSET
    public_gpu_id: str | Unset = UNSET
    public_price_per_hour_eur: float | Unset = UNSET
    replica_set_id: str | Unset = UNSET
    runtime_config_snapshot: str | Unset = UNSET
    runtime_preset: str | Unset = UNSET
    scheduling_mode: str | Unset = UNSET
    serverless_enabled: bool | Unset = UNSET
    serving_name: str | Unset = UNSET
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
    started_at: str | Unset = UNSET
    state: str | Unset = UNSET
    stopped_at: str | Unset = UNSET
    workload_kind: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        capacity_tier = self.capacity_tier

        created_at = self.created_at

        description = self.description

        estimated_required_vram_gb = self.estimated_required_vram_gb

        failure_reason = self.failure_reason

        gpu_count = self.gpu_count

        gpu_preferences: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.gpu_preferences, Unset):
            gpu_preferences = []
            for gpu_preferences_item_data in self.gpu_preferences:
                gpu_preferences_item = gpu_preferences_item_data.to_dict()
                gpu_preferences.append(gpu_preferences_item)



        huggingface_repo_id = self.huggingface_repo_id

        id = self.id

        idle_timeout_seconds = self.idle_timeout_seconds

        last_request_at = self.last_request_at

        name = self.name

        public_gpu_id = self.public_gpu_id

        public_price_per_hour_eur = self.public_price_per_hour_eur

        replica_set_id = self.replica_set_id

        runtime_config_snapshot = self.runtime_config_snapshot

        runtime_preset = self.runtime_preset

        scheduling_mode = self.scheduling_mode

        serverless_enabled = self.serverless_enabled

        serving_name = self.serving_name

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

        started_at = self.started_at

        state = self.state

        stopped_at = self.stopped_at

        workload_kind = self.workload_kind


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if capacity_tier is not UNSET:
            field_dict["capacity_tier"] = capacity_tier
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if estimated_required_vram_gb is not UNSET:
            field_dict["estimated_required_vram_gb"] = estimated_required_vram_gb
        if failure_reason is not UNSET:
            field_dict["failure_reason"] = failure_reason
        if gpu_count is not UNSET:
            field_dict["gpu_count"] = gpu_count
        if gpu_preferences is not UNSET:
            field_dict["gpu_preferences"] = gpu_preferences
        if huggingface_repo_id is not UNSET:
            field_dict["huggingface_repo_id"] = huggingface_repo_id
        if id is not UNSET:
            field_dict["id"] = id
        if idle_timeout_seconds is not UNSET:
            field_dict["idle_timeout_seconds"] = idle_timeout_seconds
        if last_request_at is not UNSET:
            field_dict["last_request_at"] = last_request_at
        if name is not UNSET:
            field_dict["name"] = name
        if public_gpu_id is not UNSET:
            field_dict["public_gpu_id"] = public_gpu_id
        if public_price_per_hour_eur is not UNSET:
            field_dict["public_price_per_hour_eur"] = public_price_per_hour_eur
        if replica_set_id is not UNSET:
            field_dict["replica_set_id"] = replica_set_id
        if runtime_config_snapshot is not UNSET:
            field_dict["runtime_config_snapshot"] = runtime_config_snapshot
        if runtime_preset is not UNSET:
            field_dict["runtime_preset"] = runtime_preset
        if scheduling_mode is not UNSET:
            field_dict["scheduling_mode"] = scheduling_mode
        if serverless_enabled is not UNSET:
            field_dict["serverless_enabled"] = serverless_enabled
        if serving_name is not UNSET:
            field_dict["serving_name"] = serving_name
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
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if state is not UNSET:
            field_dict["state"] = state
        if stopped_at is not UNSET:
            field_dict["stopped_at"] = stopped_at
        if workload_kind is not UNSET:
            field_dict["workload_kind"] = workload_kind

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gpu_preference_response import GpuPreferenceResponse
        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        capacity_tier = d.pop("capacity_tier", UNSET)

        created_at = d.pop("created_at", UNSET)

        description = d.pop("description", UNSET)

        estimated_required_vram_gb = d.pop("estimated_required_vram_gb", UNSET)

        failure_reason = d.pop("failure_reason", UNSET)

        gpu_count = d.pop("gpu_count", UNSET)

        _gpu_preferences = d.pop("gpu_preferences", UNSET)
        gpu_preferences: list[GpuPreferenceResponse] | Unset = UNSET
        if _gpu_preferences is not UNSET:
            gpu_preferences = []
            for gpu_preferences_item_data in _gpu_preferences:
                gpu_preferences_item = GpuPreferenceResponse.from_dict(gpu_preferences_item_data)



                gpu_preferences.append(gpu_preferences_item)


        huggingface_repo_id = d.pop("huggingface_repo_id", UNSET)

        id = d.pop("id", UNSET)

        idle_timeout_seconds = d.pop("idle_timeout_seconds", UNSET)

        last_request_at = d.pop("last_request_at", UNSET)

        name = d.pop("name", UNSET)

        public_gpu_id = d.pop("public_gpu_id", UNSET)

        public_price_per_hour_eur = d.pop("public_price_per_hour_eur", UNSET)

        replica_set_id = d.pop("replica_set_id", UNSET)

        runtime_config_snapshot = d.pop("runtime_config_snapshot", UNSET)

        runtime_preset = d.pop("runtime_preset", UNSET)

        scheduling_mode = d.pop("scheduling_mode", UNSET)

        serverless_enabled = d.pop("serverless_enabled", UNSET)

        serving_name = d.pop("serving_name", UNSET)

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

        started_at = d.pop("started_at", UNSET)

        state = d.pop("state", UNSET)

        stopped_at = d.pop("stopped_at", UNSET)

        workload_kind = d.pop("workload_kind", UNSET)

        instance_response = cls(
            account_id=account_id,
            capacity_tier=capacity_tier,
            created_at=created_at,
            description=description,
            estimated_required_vram_gb=estimated_required_vram_gb,
            failure_reason=failure_reason,
            gpu_count=gpu_count,
            gpu_preferences=gpu_preferences,
            huggingface_repo_id=huggingface_repo_id,
            id=id,
            idle_timeout_seconds=idle_timeout_seconds,
            last_request_at=last_request_at,
            name=name,
            public_gpu_id=public_gpu_id,
            public_price_per_hour_eur=public_price_per_hour_eur,
            replica_set_id=replica_set_id,
            runtime_config_snapshot=runtime_config_snapshot,
            runtime_preset=runtime_preset,
            scheduling_mode=scheduling_mode,
            serverless_enabled=serverless_enabled,
            serving_name=serving_name,
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
            started_at=started_at,
            state=state,
            stopped_at=stopped_at,
            workload_kind=workload_kind,
        )


        instance_response.additional_properties = d
        return instance_response

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
