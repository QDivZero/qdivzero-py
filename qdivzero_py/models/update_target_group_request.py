from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.target_group_member_request import TargetGroupMemberRequest


T = TypeVar("T", bound="UpdateTargetGroupRequest")


@_attrs_define
class UpdateTargetGroupRequest:
    """
    Attributes:
        description (str | Unset):
        display_name (str | Unset):
        enabled (bool | Unset):
        members (list[TargetGroupMemberRequest] | Unset):
        selection_policy (str | Unset):
    """

    description: str | Unset = UNSET
    display_name: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    members: list[TargetGroupMemberRequest] | Unset = UNSET
    selection_policy: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        display_name = self.display_name

        enabled = self.enabled

        members: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.members, Unset):
            members = []
            for members_item_data in self.members:
                members_item = members_item_data.to_dict()
                members.append(members_item)

        selection_policy = self.selection_policy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if members is not UNSET:
            field_dict["members"] = members
        if selection_policy is not UNSET:
            field_dict["selection_policy"] = selection_policy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.target_group_member_request import TargetGroupMemberRequest

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        display_name = d.pop("display_name", UNSET)

        enabled = d.pop("enabled", UNSET)

        _members = d.pop("members", UNSET)
        members: list[TargetGroupMemberRequest] | Unset = UNSET
        if _members is not UNSET:
            members = []
            for members_item_data in _members:
                members_item = TargetGroupMemberRequest.from_dict(members_item_data)

                members.append(members_item)

        selection_policy = d.pop("selection_policy", UNSET)

        update_target_group_request = cls(
            description=description,
            display_name=display_name,
            enabled=enabled,
            members=members,
            selection_policy=selection_policy,
        )

        update_target_group_request.additional_properties = d
        return update_target_group_request

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
