from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.target_group_member_response import TargetGroupMemberResponse


T = TypeVar("T", bound="TargetGroupResponse")


@_attrs_define
class TargetGroupResponse:
    """
    Attributes:
        created_at (str | Unset):
        description (str | Unset):
        display_name (str | Unset):
        enabled (bool | Unset):
        id (str | Unset):
        members (list[TargetGroupMemberResponse] | Unset):
        name (str | Unset):
        selection_policy (str | Unset):
        updated_at (str | Unset):
        workload_kind (str | Unset):
    """

    created_at: str | Unset = UNSET
    description: str | Unset = UNSET
    display_name: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    id: str | Unset = UNSET
    members: list[TargetGroupMemberResponse] | Unset = UNSET
    name: str | Unset = UNSET
    selection_policy: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    workload_kind: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        description = self.description

        display_name = self.display_name

        enabled = self.enabled

        id = self.id

        members: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.members, Unset):
            members = []
            for members_item_data in self.members:
                members_item = members_item_data.to_dict()
                members.append(members_item)

        name = self.name

        selection_policy = self.selection_policy

        updated_at = self.updated_at

        workload_kind = self.workload_kind

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if id is not UNSET:
            field_dict["id"] = id
        if members is not UNSET:
            field_dict["members"] = members
        if name is not UNSET:
            field_dict["name"] = name
        if selection_policy is not UNSET:
            field_dict["selection_policy"] = selection_policy
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if workload_kind is not UNSET:
            field_dict["workload_kind"] = workload_kind

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.target_group_member_response import TargetGroupMemberResponse

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        description = d.pop("description", UNSET)

        display_name = d.pop("display_name", UNSET)

        enabled = d.pop("enabled", UNSET)

        id = d.pop("id", UNSET)

        _members = d.pop("members", UNSET)
        members: list[TargetGroupMemberResponse] | Unset = UNSET
        if _members is not UNSET:
            members = []
            for members_item_data in _members:
                members_item = TargetGroupMemberResponse.from_dict(members_item_data)

                members.append(members_item)

        name = d.pop("name", UNSET)

        selection_policy = d.pop("selection_policy", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        workload_kind = d.pop("workload_kind", UNSET)

        target_group_response = cls(
            created_at=created_at,
            description=description,
            display_name=display_name,
            enabled=enabled,
            id=id,
            members=members,
            name=name,
            selection_policy=selection_policy,
            updated_at=updated_at,
            workload_kind=workload_kind,
        )

        target_group_response.additional_properties = d
        return target_group_response

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
