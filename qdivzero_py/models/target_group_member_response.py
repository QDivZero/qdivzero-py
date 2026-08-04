from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TargetGroupMemberResponse")



@_attrs_define
class TargetGroupMemberResponse:
    """ 
        Attributes:
            created_at (str | Unset):
            enabled (bool | Unset):
            id (str | Unset):
            instance_id (str | Unset):
            priority (int | Unset):
            updated_at (str | Unset):
            weight (int | Unset):
     """

    created_at: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    id: str | Unset = UNSET
    instance_id: str | Unset = UNSET
    priority: int | Unset = UNSET
    updated_at: str | Unset = UNSET
    weight: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        enabled = self.enabled

        id = self.id

        instance_id = self.instance_id

        priority = self.priority

        updated_at = self.updated_at

        weight = self.weight


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if id is not UNSET:
            field_dict["id"] = id
        if instance_id is not UNSET:
            field_dict["instance_id"] = instance_id
        if priority is not UNSET:
            field_dict["priority"] = priority
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if weight is not UNSET:
            field_dict["weight"] = weight

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        enabled = d.pop("enabled", UNSET)

        id = d.pop("id", UNSET)

        instance_id = d.pop("instance_id", UNSET)

        priority = d.pop("priority", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        weight = d.pop("weight", UNSET)

        target_group_member_response = cls(
            created_at=created_at,
            enabled=enabled,
            id=id,
            instance_id=instance_id,
            priority=priority,
            updated_at=updated_at,
            weight=weight,
        )


        target_group_member_response.additional_properties = d
        return target_group_member_response

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
