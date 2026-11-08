from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReplicaSetResponse")


@_attrs_define
class ReplicaSetResponse:
    """
    Attributes:
        account_id (str | Unset):
        created_at (str | Unset):
        desired_replicas (int | Unset):
        gguf_model_path (str | Unset):
        id (str | Unset):
        min_replicas (int | Unset):
        model_ref (str | Unset):
        name (str | Unset):
        runtime_config_snapshot (str | Unset):
        scheduling_mode (str | Unset):
        serving_endpoint_id (str | Unset):
        serving_name (str | Unset):
        smart_allow_community (bool | Unset):
        smart_allow_spot (bool | Unset):
        smart_max_price_per_hour_usd (float | Unset):
        smart_min_gpu_class (str | Unset):
        smart_min_total_tflops (float | Unset):
        smart_provider_filter_mode (str | Unset):
        smart_provider_preference (str | Unset):
        smart_region (str | Unset):
        smart_regions (list[str] | Unset):
        smart_selection_label (str | Unset):
        status (str | Unset):
        supported_protocols (list[str] | Unset):
        target_group_id (str | Unset):
        updated_at (str | Unset):
        workload_kind (str | Unset):
    """

    account_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    desired_replicas: int | Unset = UNSET
    gguf_model_path: str | Unset = UNSET
    id: str | Unset = UNSET
    min_replicas: int | Unset = UNSET
    model_ref: str | Unset = UNSET
    name: str | Unset = UNSET
    runtime_config_snapshot: str | Unset = UNSET
    scheduling_mode: str | Unset = UNSET
    serving_endpoint_id: str | Unset = UNSET
    serving_name: str | Unset = UNSET
    smart_allow_community: bool | Unset = UNSET
    smart_allow_spot: bool | Unset = UNSET
    smart_max_price_per_hour_usd: float | Unset = UNSET
    smart_min_gpu_class: str | Unset = UNSET
    smart_min_total_tflops: float | Unset = UNSET
    smart_provider_filter_mode: str | Unset = UNSET
    smart_provider_preference: str | Unset = UNSET
    smart_region: str | Unset = UNSET
    smart_regions: list[str] | Unset = UNSET
    smart_selection_label: str | Unset = UNSET
    status: str | Unset = UNSET
    supported_protocols: list[str] | Unset = UNSET
    target_group_id: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    workload_kind: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        created_at = self.created_at

        desired_replicas = self.desired_replicas

        gguf_model_path = self.gguf_model_path

        id = self.id

        min_replicas = self.min_replicas

        model_ref = self.model_ref

        name = self.name

        runtime_config_snapshot = self.runtime_config_snapshot

        scheduling_mode = self.scheduling_mode

        serving_endpoint_id = self.serving_endpoint_id

        serving_name = self.serving_name

        smart_allow_community = self.smart_allow_community

        smart_allow_spot = self.smart_allow_spot

        smart_max_price_per_hour_usd = self.smart_max_price_per_hour_usd

        smart_min_gpu_class = self.smart_min_gpu_class

        smart_min_total_tflops = self.smart_min_total_tflops

        smart_provider_filter_mode = self.smart_provider_filter_mode

        smart_provider_preference = self.smart_provider_preference

        smart_region = self.smart_region

        smart_regions: list[str] | Unset = UNSET
        if not isinstance(self.smart_regions, Unset):
            smart_regions = self.smart_regions

        smart_selection_label = self.smart_selection_label

        status = self.status

        supported_protocols: list[str] | Unset = UNSET
        if not isinstance(self.supported_protocols, Unset):
            supported_protocols = self.supported_protocols

        target_group_id = self.target_group_id

        updated_at = self.updated_at

        workload_kind = self.workload_kind

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if desired_replicas is not UNSET:
            field_dict["desired_replicas"] = desired_replicas
        if gguf_model_path is not UNSET:
            field_dict["gguf_model_path"] = gguf_model_path
        if id is not UNSET:
            field_dict["id"] = id
        if min_replicas is not UNSET:
            field_dict["min_replicas"] = min_replicas
        if model_ref is not UNSET:
            field_dict["model_ref"] = model_ref
        if name is not UNSET:
            field_dict["name"] = name
        if runtime_config_snapshot is not UNSET:
            field_dict["runtime_config_snapshot"] = runtime_config_snapshot
        if scheduling_mode is not UNSET:
            field_dict["scheduling_mode"] = scheduling_mode
        if serving_endpoint_id is not UNSET:
            field_dict["serving_endpoint_id"] = serving_endpoint_id
        if serving_name is not UNSET:
            field_dict["serving_name"] = serving_name
        if smart_allow_community is not UNSET:
            field_dict["smart_allow_community"] = smart_allow_community
        if smart_allow_spot is not UNSET:
            field_dict["smart_allow_spot"] = smart_allow_spot
        if smart_max_price_per_hour_usd is not UNSET:
            field_dict["smart_max_price_per_hour_usd"] = smart_max_price_per_hour_usd
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
        if status is not UNSET:
            field_dict["status"] = status
        if supported_protocols is not UNSET:
            field_dict["supported_protocols"] = supported_protocols
        if target_group_id is not UNSET:
            field_dict["target_group_id"] = target_group_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if workload_kind is not UNSET:
            field_dict["workload_kind"] = workload_kind

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        desired_replicas = d.pop("desired_replicas", UNSET)

        gguf_model_path = d.pop("gguf_model_path", UNSET)

        id = d.pop("id", UNSET)

        min_replicas = d.pop("min_replicas", UNSET)

        model_ref = d.pop("model_ref", UNSET)

        name = d.pop("name", UNSET)

        runtime_config_snapshot = d.pop("runtime_config_snapshot", UNSET)

        scheduling_mode = d.pop("scheduling_mode", UNSET)

        serving_endpoint_id = d.pop("serving_endpoint_id", UNSET)

        serving_name = d.pop("serving_name", UNSET)

        smart_allow_community = d.pop("smart_allow_community", UNSET)

        smart_allow_spot = d.pop("smart_allow_spot", UNSET)

        smart_max_price_per_hour_usd = d.pop("smart_max_price_per_hour_usd", UNSET)

        smart_min_gpu_class = d.pop("smart_min_gpu_class", UNSET)

        smart_min_total_tflops = d.pop("smart_min_total_tflops", UNSET)

        smart_provider_filter_mode = d.pop("smart_provider_filter_mode", UNSET)

        smart_provider_preference = d.pop("smart_provider_preference", UNSET)

        smart_region = d.pop("smart_region", UNSET)

        smart_regions = cast(list[str], d.pop("smart_regions", UNSET))

        smart_selection_label = d.pop("smart_selection_label", UNSET)

        status = d.pop("status", UNSET)

        supported_protocols = cast(list[str], d.pop("supported_protocols", UNSET))

        target_group_id = d.pop("target_group_id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        workload_kind = d.pop("workload_kind", UNSET)

        replica_set_response = cls(
            account_id=account_id,
            created_at=created_at,
            desired_replicas=desired_replicas,
            gguf_model_path=gguf_model_path,
            id=id,
            min_replicas=min_replicas,
            model_ref=model_ref,
            name=name,
            runtime_config_snapshot=runtime_config_snapshot,
            scheduling_mode=scheduling_mode,
            serving_endpoint_id=serving_endpoint_id,
            serving_name=serving_name,
            smart_allow_community=smart_allow_community,
            smart_allow_spot=smart_allow_spot,
            smart_max_price_per_hour_usd=smart_max_price_per_hour_usd,
            smart_min_gpu_class=smart_min_gpu_class,
            smart_min_total_tflops=smart_min_total_tflops,
            smart_provider_filter_mode=smart_provider_filter_mode,
            smart_provider_preference=smart_provider_preference,
            smart_region=smart_region,
            smart_regions=smart_regions,
            smart_selection_label=smart_selection_label,
            status=status,
            supported_protocols=supported_protocols,
            target_group_id=target_group_id,
            updated_at=updated_at,
            workload_kind=workload_kind,
        )

        replica_set_response.additional_properties = d
        return replica_set_response

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
