from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResourceMetricSnapshot")



@_attrs_define
class ResourceMetricSnapshot:
    """ 
        Attributes:
            cpu_utilization_percent (float | Unset):
            disk_utilization_percent (float | Unset):
            gpu_memory_utilization_percent (float | Unset):
            gpu_power_watts (float | Unset):
            gpu_temperature_celsius (float | Unset):
            gpu_utilization_percent (float | Unset):
            memory_utilization_percent (float | Unset):
            sampled_at (str | Unset):
     """

    cpu_utilization_percent: float | Unset = UNSET
    disk_utilization_percent: float | Unset = UNSET
    gpu_memory_utilization_percent: float | Unset = UNSET
    gpu_power_watts: float | Unset = UNSET
    gpu_temperature_celsius: float | Unset = UNSET
    gpu_utilization_percent: float | Unset = UNSET
    memory_utilization_percent: float | Unset = UNSET
    sampled_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        cpu_utilization_percent = self.cpu_utilization_percent

        disk_utilization_percent = self.disk_utilization_percent

        gpu_memory_utilization_percent = self.gpu_memory_utilization_percent

        gpu_power_watts = self.gpu_power_watts

        gpu_temperature_celsius = self.gpu_temperature_celsius

        gpu_utilization_percent = self.gpu_utilization_percent

        memory_utilization_percent = self.memory_utilization_percent

        sampled_at = self.sampled_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if cpu_utilization_percent is not UNSET:
            field_dict["cpu_utilization_percent"] = cpu_utilization_percent
        if disk_utilization_percent is not UNSET:
            field_dict["disk_utilization_percent"] = disk_utilization_percent
        if gpu_memory_utilization_percent is not UNSET:
            field_dict["gpu_memory_utilization_percent"] = gpu_memory_utilization_percent
        if gpu_power_watts is not UNSET:
            field_dict["gpu_power_watts"] = gpu_power_watts
        if gpu_temperature_celsius is not UNSET:
            field_dict["gpu_temperature_celsius"] = gpu_temperature_celsius
        if gpu_utilization_percent is not UNSET:
            field_dict["gpu_utilization_percent"] = gpu_utilization_percent
        if memory_utilization_percent is not UNSET:
            field_dict["memory_utilization_percent"] = memory_utilization_percent
        if sampled_at is not UNSET:
            field_dict["sampled_at"] = sampled_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cpu_utilization_percent = d.pop("cpu_utilization_percent", UNSET)

        disk_utilization_percent = d.pop("disk_utilization_percent", UNSET)

        gpu_memory_utilization_percent = d.pop("gpu_memory_utilization_percent", UNSET)

        gpu_power_watts = d.pop("gpu_power_watts", UNSET)

        gpu_temperature_celsius = d.pop("gpu_temperature_celsius", UNSET)

        gpu_utilization_percent = d.pop("gpu_utilization_percent", UNSET)

        memory_utilization_percent = d.pop("memory_utilization_percent", UNSET)

        sampled_at = d.pop("sampled_at", UNSET)

        resource_metric_snapshot = cls(
            cpu_utilization_percent=cpu_utilization_percent,
            disk_utilization_percent=disk_utilization_percent,
            gpu_memory_utilization_percent=gpu_memory_utilization_percent,
            gpu_power_watts=gpu_power_watts,
            gpu_temperature_celsius=gpu_temperature_celsius,
            gpu_utilization_percent=gpu_utilization_percent,
            memory_utilization_percent=memory_utilization_percent,
            sampled_at=sampled_at,
        )


        resource_metric_snapshot.additional_properties = d
        return resource_metric_snapshot

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
