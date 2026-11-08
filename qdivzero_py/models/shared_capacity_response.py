from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.shared_capacity_instance_response import SharedCapacityInstanceResponse
    from ..models.shared_capacity_membership_response import SharedCapacityMembershipResponse


T = TypeVar("T", bound="SharedCapacityResponse")


@_attrs_define
class SharedCapacityResponse:
    """
    Attributes:
        active_member_count (int | Unset):
        backing_instance_id (str | Unset):
        base_price_eur_per_hour (float | Unset):
        base_price_microcents_per_hour (int | Unset):
        base_price_microcents_per_second (int | Unset):
        close_reason (str | Unset):
        current_member_price_eur_per_hour (float | Unset):
        current_member_price_microcents_per_hour (int | Unset):
        group_id (str | Unset):
        instance (SharedCapacityInstanceResponse | Unset):
        max_members (int | Unset):
        member_price_microcents_per_second (int | Unset):
        members (list[SharedCapacityMembershipResponse] | Unset):
        membership (SharedCapacityMembershipResponse | Unset):
        public_slug (str | Unset):
        status (str | Unset):
        terms_hash (str | Unset):
        terms_version (str | Unset):
        visibility (str | Unset):
    """

    active_member_count: int | Unset = UNSET
    backing_instance_id: str | Unset = UNSET
    base_price_eur_per_hour: float | Unset = UNSET
    base_price_microcents_per_hour: int | Unset = UNSET
    base_price_microcents_per_second: int | Unset = UNSET
    close_reason: str | Unset = UNSET
    current_member_price_eur_per_hour: float | Unset = UNSET
    current_member_price_microcents_per_hour: int | Unset = UNSET
    group_id: str | Unset = UNSET
    instance: SharedCapacityInstanceResponse | Unset = UNSET
    max_members: int | Unset = UNSET
    member_price_microcents_per_second: int | Unset = UNSET
    members: list[SharedCapacityMembershipResponse] | Unset = UNSET
    membership: SharedCapacityMembershipResponse | Unset = UNSET
    public_slug: str | Unset = UNSET
    status: str | Unset = UNSET
    terms_hash: str | Unset = UNSET
    terms_version: str | Unset = UNSET
    visibility: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active_member_count = self.active_member_count

        backing_instance_id = self.backing_instance_id

        base_price_eur_per_hour = self.base_price_eur_per_hour

        base_price_microcents_per_hour = self.base_price_microcents_per_hour

        base_price_microcents_per_second = self.base_price_microcents_per_second

        close_reason = self.close_reason

        current_member_price_eur_per_hour = self.current_member_price_eur_per_hour

        current_member_price_microcents_per_hour = self.current_member_price_microcents_per_hour

        group_id = self.group_id

        instance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.instance, Unset):
            instance = self.instance.to_dict()

        max_members = self.max_members

        member_price_microcents_per_second = self.member_price_microcents_per_second

        members: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.members, Unset):
            members = []
            for members_item_data in self.members:
                members_item = members_item_data.to_dict()
                members.append(members_item)

        membership: dict[str, Any] | Unset = UNSET
        if not isinstance(self.membership, Unset):
            membership = self.membership.to_dict()

        public_slug = self.public_slug

        status = self.status

        terms_hash = self.terms_hash

        terms_version = self.terms_version

        visibility = self.visibility

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active_member_count is not UNSET:
            field_dict["active_member_count"] = active_member_count
        if backing_instance_id is not UNSET:
            field_dict["backing_instance_id"] = backing_instance_id
        if base_price_eur_per_hour is not UNSET:
            field_dict["base_price_eur_per_hour"] = base_price_eur_per_hour
        if base_price_microcents_per_hour is not UNSET:
            field_dict["base_price_microcents_per_hour"] = base_price_microcents_per_hour
        if base_price_microcents_per_second is not UNSET:
            field_dict["base_price_microcents_per_second"] = base_price_microcents_per_second
        if close_reason is not UNSET:
            field_dict["close_reason"] = close_reason
        if current_member_price_eur_per_hour is not UNSET:
            field_dict["current_member_price_eur_per_hour"] = current_member_price_eur_per_hour
        if current_member_price_microcents_per_hour is not UNSET:
            field_dict["current_member_price_microcents_per_hour"] = current_member_price_microcents_per_hour
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if instance is not UNSET:
            field_dict["instance"] = instance
        if max_members is not UNSET:
            field_dict["max_members"] = max_members
        if member_price_microcents_per_second is not UNSET:
            field_dict["member_price_microcents_per_second"] = member_price_microcents_per_second
        if members is not UNSET:
            field_dict["members"] = members
        if membership is not UNSET:
            field_dict["membership"] = membership
        if public_slug is not UNSET:
            field_dict["public_slug"] = public_slug
        if status is not UNSET:
            field_dict["status"] = status
        if terms_hash is not UNSET:
            field_dict["terms_hash"] = terms_hash
        if terms_version is not UNSET:
            field_dict["terms_version"] = terms_version
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.shared_capacity_instance_response import SharedCapacityInstanceResponse
        from ..models.shared_capacity_membership_response import SharedCapacityMembershipResponse

        d = dict(src_dict)
        active_member_count = d.pop("active_member_count", UNSET)

        backing_instance_id = d.pop("backing_instance_id", UNSET)

        base_price_eur_per_hour = d.pop("base_price_eur_per_hour", UNSET)

        base_price_microcents_per_hour = d.pop("base_price_microcents_per_hour", UNSET)

        base_price_microcents_per_second = d.pop("base_price_microcents_per_second", UNSET)

        close_reason = d.pop("close_reason", UNSET)

        current_member_price_eur_per_hour = d.pop("current_member_price_eur_per_hour", UNSET)

        current_member_price_microcents_per_hour = d.pop("current_member_price_microcents_per_hour", UNSET)

        group_id = d.pop("group_id", UNSET)

        _instance = d.pop("instance", UNSET)
        instance: SharedCapacityInstanceResponse | Unset
        if isinstance(_instance, Unset):
            instance = UNSET
        else:
            instance = SharedCapacityInstanceResponse.from_dict(_instance)

        max_members = d.pop("max_members", UNSET)

        member_price_microcents_per_second = d.pop("member_price_microcents_per_second", UNSET)

        _members = d.pop("members", UNSET)
        members: list[SharedCapacityMembershipResponse] | Unset = UNSET
        if _members is not UNSET:
            members = []
            for members_item_data in _members:
                members_item = SharedCapacityMembershipResponse.from_dict(members_item_data)

                members.append(members_item)

        _membership = d.pop("membership", UNSET)
        membership: SharedCapacityMembershipResponse | Unset
        if isinstance(_membership, Unset):
            membership = UNSET
        else:
            membership = SharedCapacityMembershipResponse.from_dict(_membership)

        public_slug = d.pop("public_slug", UNSET)

        status = d.pop("status", UNSET)

        terms_hash = d.pop("terms_hash", UNSET)

        terms_version = d.pop("terms_version", UNSET)

        visibility = d.pop("visibility", UNSET)

        shared_capacity_response = cls(
            active_member_count=active_member_count,
            backing_instance_id=backing_instance_id,
            base_price_eur_per_hour=base_price_eur_per_hour,
            base_price_microcents_per_hour=base_price_microcents_per_hour,
            base_price_microcents_per_second=base_price_microcents_per_second,
            close_reason=close_reason,
            current_member_price_eur_per_hour=current_member_price_eur_per_hour,
            current_member_price_microcents_per_hour=current_member_price_microcents_per_hour,
            group_id=group_id,
            instance=instance,
            max_members=max_members,
            member_price_microcents_per_second=member_price_microcents_per_second,
            members=members,
            membership=membership,
            public_slug=public_slug,
            status=status,
            terms_hash=terms_hash,
            terms_version=terms_version,
            visibility=visibility,
        )

        shared_capacity_response.additional_properties = d
        return shared_capacity_response

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
