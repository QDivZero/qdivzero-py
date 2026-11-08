from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SharedCapacityInstanceResponse")


@_attrs_define
class SharedCapacityInstanceResponse:
    """
    Attributes:
        capacity_tier (str | Unset):
        created_at (str | Unset):
        gpu (str | Unset):
        gpu_count (int | Unset):
        model_ref (str | Unset):
        public_price_per_hour_microcents (int | Unset):
        started_at (str | Unset):
        state (str | Unset):
        storage_price_per_hour_microcents (int | Unset):
        workload_kind (str | Unset):
    """

    capacity_tier: str | Unset = UNSET
    created_at: str | Unset = UNSET
    gpu: str | Unset = UNSET
    gpu_count: int | Unset = UNSET
    model_ref: str | Unset = UNSET
    public_price_per_hour_microcents: int | Unset = UNSET
    started_at: str | Unset = UNSET
    state: str | Unset = UNSET
    storage_price_per_hour_microcents: int | Unset = UNSET
    workload_kind: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        capacity_tier = self.capacity_tier

        created_at = self.created_at

        gpu = self.gpu

        gpu_count = self.gpu_count

        model_ref = self.model_ref

        public_price_per_hour_microcents = self.public_price_per_hour_microcents

        started_at = self.started_at

        state = self.state

        storage_price_per_hour_microcents = self.storage_price_per_hour_microcents

        workload_kind = self.workload_kind

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if capacity_tier is not UNSET:
            field_dict["capacity_tier"] = capacity_tier
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if gpu is not UNSET:
            field_dict["gpu"] = gpu
        if gpu_count is not UNSET:
            field_dict["gpu_count"] = gpu_count
        if model_ref is not UNSET:
            field_dict["model_ref"] = model_ref
        if public_price_per_hour_microcents is not UNSET:
            field_dict["public_price_per_hour_microcents"] = public_price_per_hour_microcents
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if state is not UNSET:
            field_dict["state"] = state
        if storage_price_per_hour_microcents is not UNSET:
            field_dict["storage_price_per_hour_microcents"] = storage_price_per_hour_microcents
        if workload_kind is not UNSET:
            field_dict["workload_kind"] = workload_kind

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        capacity_tier = d.pop("capacity_tier", UNSET)

        created_at = d.pop("created_at", UNSET)

        gpu = d.pop("gpu", UNSET)

        gpu_count = d.pop("gpu_count", UNSET)

        model_ref = d.pop("model_ref", UNSET)

        public_price_per_hour_microcents = d.pop("public_price_per_hour_microcents", UNSET)

        started_at = d.pop("started_at", UNSET)

        state = d.pop("state", UNSET)

        storage_price_per_hour_microcents = d.pop("storage_price_per_hour_microcents", UNSET)

        workload_kind = d.pop("workload_kind", UNSET)

        shared_capacity_instance_response = cls(
            capacity_tier=capacity_tier,
            created_at=created_at,
            gpu=gpu,
            gpu_count=gpu_count,
            model_ref=model_ref,
            public_price_per_hour_microcents=public_price_per_hour_microcents,
            started_at=started_at,
            state=state,
            storage_price_per_hour_microcents=storage_price_per_hour_microcents,
            workload_kind=workload_kind,
        )

        shared_capacity_instance_response.additional_properties = d
        return shared_capacity_instance_response

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
