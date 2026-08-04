from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PreviewInstanceUpdateRequest")



@_attrs_define
class PreviewInstanceUpdateRequest:
    """ 
        Attributes:
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
     """

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
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
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


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
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

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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

        preview_instance_update_request = cls(
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
        )


        preview_instance_update_request.additional_properties = d
        return preview_instance_update_request

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
