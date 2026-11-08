from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateReplicaSetRequest")


@_attrs_define
class UpdateReplicaSetRequest:
    """
    Attributes:
        desired_replicas (int | Unset):
        name (str | Unset):
        scheduling_mode (str | Unset):
        serving_name (str | Unset):
        smart_allow_community (bool | Unset):
        smart_allow_spot (bool | Unset):
        smart_max_price_per_hour_usd (float | Unset):
        smart_min_gpu_class (str | Unset):
        smart_min_total_tflops (float | Unset):
        smart_provider_filter_mode (str | Unset):
        smart_provider_preference (str | Unset):
        smart_regions (list[str] | Unset):
    """

    desired_replicas: int | Unset = UNSET
    name: str | Unset = UNSET
    scheduling_mode: str | Unset = UNSET
    serving_name: str | Unset = UNSET
    smart_allow_community: bool | Unset = UNSET
    smart_allow_spot: bool | Unset = UNSET
    smart_max_price_per_hour_usd: float | Unset = UNSET
    smart_min_gpu_class: str | Unset = UNSET
    smart_min_total_tflops: float | Unset = UNSET
    smart_provider_filter_mode: str | Unset = UNSET
    smart_provider_preference: str | Unset = UNSET
    smart_regions: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        desired_replicas = self.desired_replicas

        name = self.name

        scheduling_mode = self.scheduling_mode

        serving_name = self.serving_name

        smart_allow_community = self.smart_allow_community

        smart_allow_spot = self.smart_allow_spot

        smart_max_price_per_hour_usd = self.smart_max_price_per_hour_usd

        smart_min_gpu_class = self.smart_min_gpu_class

        smart_min_total_tflops = self.smart_min_total_tflops

        smart_provider_filter_mode = self.smart_provider_filter_mode

        smart_provider_preference = self.smart_provider_preference

        smart_regions: list[str] | Unset = UNSET
        if not isinstance(self.smart_regions, Unset):
            smart_regions = self.smart_regions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if desired_replicas is not UNSET:
            field_dict["desired_replicas"] = desired_replicas
        if name is not UNSET:
            field_dict["name"] = name
        if scheduling_mode is not UNSET:
            field_dict["scheduling_mode"] = scheduling_mode
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
        if smart_regions is not UNSET:
            field_dict["smart_regions"] = smart_regions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        desired_replicas = d.pop("desired_replicas", UNSET)

        name = d.pop("name", UNSET)

        scheduling_mode = d.pop("scheduling_mode", UNSET)

        serving_name = d.pop("serving_name", UNSET)

        smart_allow_community = d.pop("smart_allow_community", UNSET)

        smart_allow_spot = d.pop("smart_allow_spot", UNSET)

        smart_max_price_per_hour_usd = d.pop("smart_max_price_per_hour_usd", UNSET)

        smart_min_gpu_class = d.pop("smart_min_gpu_class", UNSET)

        smart_min_total_tflops = d.pop("smart_min_total_tflops", UNSET)

        smart_provider_filter_mode = d.pop("smart_provider_filter_mode", UNSET)

        smart_provider_preference = d.pop("smart_provider_preference", UNSET)

        smart_regions = cast(list[str], d.pop("smart_regions", UNSET))

        update_replica_set_request = cls(
            desired_replicas=desired_replicas,
            name=name,
            scheduling_mode=scheduling_mode,
            serving_name=serving_name,
            smart_allow_community=smart_allow_community,
            smart_allow_spot=smart_allow_spot,
            smart_max_price_per_hour_usd=smart_max_price_per_hour_usd,
            smart_min_gpu_class=smart_min_gpu_class,
            smart_min_total_tflops=smart_min_total_tflops,
            smart_provider_filter_mode=smart_provider_filter_mode,
            smart_provider_preference=smart_provider_preference,
            smart_regions=smart_regions,
        )

        update_replica_set_request.additional_properties = d
        return update_replica_set_request

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
