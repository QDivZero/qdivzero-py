from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SharedCapacityPublicResponse")


@_attrs_define
class SharedCapacityPublicResponse:
    """
    Attributes:
        active_member_count (int | Unset):
        availability_mode (str | Unset):
        base_price_eur_per_hour (float | Unset):
        base_price_microcents_per_hour (int | Unset):
        base_price_microcents_per_second (int | Unset):
        capacity_tier (str | Unset):
        estimated_join_price_eur_per_hour (float | Unset):
        estimated_join_price_microcents_per_hour (int | Unset):
        gpu (str | Unset):
        instance_state (str | Unset):
        max_members (int | Unset):
        member_price_microcents_per_second (int | Unset):
        model_description (str | Unset):
        model_ref (str | Unset):
        selection_mode (str | Unset):
        slug (str | Unset):
        status (str | Unset):
        terms_hash (str | Unset):
        terms_version (str | Unset):
        visibility (str | Unset):
        workload_kind (str | Unset):
    """

    active_member_count: int | Unset = UNSET
    availability_mode: str | Unset = UNSET
    base_price_eur_per_hour: float | Unset = UNSET
    base_price_microcents_per_hour: int | Unset = UNSET
    base_price_microcents_per_second: int | Unset = UNSET
    capacity_tier: str | Unset = UNSET
    estimated_join_price_eur_per_hour: float | Unset = UNSET
    estimated_join_price_microcents_per_hour: int | Unset = UNSET
    gpu: str | Unset = UNSET
    instance_state: str | Unset = UNSET
    max_members: int | Unset = UNSET
    member_price_microcents_per_second: int | Unset = UNSET
    model_description: str | Unset = UNSET
    model_ref: str | Unset = UNSET
    selection_mode: str | Unset = UNSET
    slug: str | Unset = UNSET
    status: str | Unset = UNSET
    terms_hash: str | Unset = UNSET
    terms_version: str | Unset = UNSET
    visibility: str | Unset = UNSET
    workload_kind: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active_member_count = self.active_member_count

        availability_mode = self.availability_mode

        base_price_eur_per_hour = self.base_price_eur_per_hour

        base_price_microcents_per_hour = self.base_price_microcents_per_hour

        base_price_microcents_per_second = self.base_price_microcents_per_second

        capacity_tier = self.capacity_tier

        estimated_join_price_eur_per_hour = self.estimated_join_price_eur_per_hour

        estimated_join_price_microcents_per_hour = self.estimated_join_price_microcents_per_hour

        gpu = self.gpu

        instance_state = self.instance_state

        max_members = self.max_members

        member_price_microcents_per_second = self.member_price_microcents_per_second

        model_description = self.model_description

        model_ref = self.model_ref

        selection_mode = self.selection_mode

        slug = self.slug

        status = self.status

        terms_hash = self.terms_hash

        terms_version = self.terms_version

        visibility = self.visibility

        workload_kind = self.workload_kind

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active_member_count is not UNSET:
            field_dict["active_member_count"] = active_member_count
        if availability_mode is not UNSET:
            field_dict["availability_mode"] = availability_mode
        if base_price_eur_per_hour is not UNSET:
            field_dict["base_price_eur_per_hour"] = base_price_eur_per_hour
        if base_price_microcents_per_hour is not UNSET:
            field_dict["base_price_microcents_per_hour"] = base_price_microcents_per_hour
        if base_price_microcents_per_second is not UNSET:
            field_dict["base_price_microcents_per_second"] = base_price_microcents_per_second
        if capacity_tier is not UNSET:
            field_dict["capacity_tier"] = capacity_tier
        if estimated_join_price_eur_per_hour is not UNSET:
            field_dict["estimated_join_price_eur_per_hour"] = estimated_join_price_eur_per_hour
        if estimated_join_price_microcents_per_hour is not UNSET:
            field_dict["estimated_join_price_microcents_per_hour"] = estimated_join_price_microcents_per_hour
        if gpu is not UNSET:
            field_dict["gpu"] = gpu
        if instance_state is not UNSET:
            field_dict["instance_state"] = instance_state
        if max_members is not UNSET:
            field_dict["max_members"] = max_members
        if member_price_microcents_per_second is not UNSET:
            field_dict["member_price_microcents_per_second"] = member_price_microcents_per_second
        if model_description is not UNSET:
            field_dict["model_description"] = model_description
        if model_ref is not UNSET:
            field_dict["model_ref"] = model_ref
        if selection_mode is not UNSET:
            field_dict["selection_mode"] = selection_mode
        if slug is not UNSET:
            field_dict["slug"] = slug
        if status is not UNSET:
            field_dict["status"] = status
        if terms_hash is not UNSET:
            field_dict["terms_hash"] = terms_hash
        if terms_version is not UNSET:
            field_dict["terms_version"] = terms_version
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if workload_kind is not UNSET:
            field_dict["workload_kind"] = workload_kind

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active_member_count = d.pop("active_member_count", UNSET)

        availability_mode = d.pop("availability_mode", UNSET)

        base_price_eur_per_hour = d.pop("base_price_eur_per_hour", UNSET)

        base_price_microcents_per_hour = d.pop("base_price_microcents_per_hour", UNSET)

        base_price_microcents_per_second = d.pop("base_price_microcents_per_second", UNSET)

        capacity_tier = d.pop("capacity_tier", UNSET)

        estimated_join_price_eur_per_hour = d.pop("estimated_join_price_eur_per_hour", UNSET)

        estimated_join_price_microcents_per_hour = d.pop("estimated_join_price_microcents_per_hour", UNSET)

        gpu = d.pop("gpu", UNSET)

        instance_state = d.pop("instance_state", UNSET)

        max_members = d.pop("max_members", UNSET)

        member_price_microcents_per_second = d.pop("member_price_microcents_per_second", UNSET)

        model_description = d.pop("model_description", UNSET)

        model_ref = d.pop("model_ref", UNSET)

        selection_mode = d.pop("selection_mode", UNSET)

        slug = d.pop("slug", UNSET)

        status = d.pop("status", UNSET)

        terms_hash = d.pop("terms_hash", UNSET)

        terms_version = d.pop("terms_version", UNSET)

        visibility = d.pop("visibility", UNSET)

        workload_kind = d.pop("workload_kind", UNSET)

        shared_capacity_public_response = cls(
            active_member_count=active_member_count,
            availability_mode=availability_mode,
            base_price_eur_per_hour=base_price_eur_per_hour,
            base_price_microcents_per_hour=base_price_microcents_per_hour,
            base_price_microcents_per_second=base_price_microcents_per_second,
            capacity_tier=capacity_tier,
            estimated_join_price_eur_per_hour=estimated_join_price_eur_per_hour,
            estimated_join_price_microcents_per_hour=estimated_join_price_microcents_per_hour,
            gpu=gpu,
            instance_state=instance_state,
            max_members=max_members,
            member_price_microcents_per_second=member_price_microcents_per_second,
            model_description=model_description,
            model_ref=model_ref,
            selection_mode=selection_mode,
            slug=slug,
            status=status,
            terms_hash=terms_hash,
            terms_version=terms_version,
            visibility=visibility,
            workload_kind=workload_kind,
        )

        shared_capacity_public_response.additional_properties = d
        return shared_capacity_public_response

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
