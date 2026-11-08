from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.shared_capacity_instance_response import SharedCapacityInstanceResponse


T = TypeVar("T", bound="SharedCapacityMembershipResponse")


@_attrs_define
class SharedCapacityMembershipResponse:
    """
    Attributes:
        accepted_at (str | Unset):
        accepted_terms_hash (str | Unset):
        accepted_terms_version (str | Unset):
        active_member_count (int | Unset):
        amount_microcents (int | Unset):
        base_price_eur_per_hour (float | Unset):
        base_price_microcents_per_hour (int | Unset):
        base_price_microcents_per_second (int | Unset):
        created_at (str | Unset):
        current_member_price_eur_per_hour (float | Unset):
        current_member_price_microcents_per_hour (int | Unset):
        effective_from (str | Unset):
        group_id (str | Unset):
        instance (SharedCapacityInstanceResponse | Unset):
        leave_effective_at (str | Unset):
        left_at (str | Unset):
        max_members (int | Unset):
        member_price_microcents_per_second (int | Unset):
        membership_id (str | Unset):
        reservation_attached (bool | Unset):
        reservation_state (str | Unset):
        role (str | Unset):
        serving_alias_id (str | Unset):
        status (str | Unset):
        suspended_at (str | Unset):
        updated_at (str | Unset):
    """

    accepted_at: str | Unset = UNSET
    accepted_terms_hash: str | Unset = UNSET
    accepted_terms_version: str | Unset = UNSET
    active_member_count: int | Unset = UNSET
    amount_microcents: int | Unset = UNSET
    base_price_eur_per_hour: float | Unset = UNSET
    base_price_microcents_per_hour: int | Unset = UNSET
    base_price_microcents_per_second: int | Unset = UNSET
    created_at: str | Unset = UNSET
    current_member_price_eur_per_hour: float | Unset = UNSET
    current_member_price_microcents_per_hour: int | Unset = UNSET
    effective_from: str | Unset = UNSET
    group_id: str | Unset = UNSET
    instance: SharedCapacityInstanceResponse | Unset = UNSET
    leave_effective_at: str | Unset = UNSET
    left_at: str | Unset = UNSET
    max_members: int | Unset = UNSET
    member_price_microcents_per_second: int | Unset = UNSET
    membership_id: str | Unset = UNSET
    reservation_attached: bool | Unset = UNSET
    reservation_state: str | Unset = UNSET
    role: str | Unset = UNSET
    serving_alias_id: str | Unset = UNSET
    status: str | Unset = UNSET
    suspended_at: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accepted_at = self.accepted_at

        accepted_terms_hash = self.accepted_terms_hash

        accepted_terms_version = self.accepted_terms_version

        active_member_count = self.active_member_count

        amount_microcents = self.amount_microcents

        base_price_eur_per_hour = self.base_price_eur_per_hour

        base_price_microcents_per_hour = self.base_price_microcents_per_hour

        base_price_microcents_per_second = self.base_price_microcents_per_second

        created_at = self.created_at

        current_member_price_eur_per_hour = self.current_member_price_eur_per_hour

        current_member_price_microcents_per_hour = self.current_member_price_microcents_per_hour

        effective_from = self.effective_from

        group_id = self.group_id

        instance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.instance, Unset):
            instance = self.instance.to_dict()

        leave_effective_at = self.leave_effective_at

        left_at = self.left_at

        max_members = self.max_members

        member_price_microcents_per_second = self.member_price_microcents_per_second

        membership_id = self.membership_id

        reservation_attached = self.reservation_attached

        reservation_state = self.reservation_state

        role = self.role

        serving_alias_id = self.serving_alias_id

        status = self.status

        suspended_at = self.suspended_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accepted_at is not UNSET:
            field_dict["accepted_at"] = accepted_at
        if accepted_terms_hash is not UNSET:
            field_dict["accepted_terms_hash"] = accepted_terms_hash
        if accepted_terms_version is not UNSET:
            field_dict["accepted_terms_version"] = accepted_terms_version
        if active_member_count is not UNSET:
            field_dict["active_member_count"] = active_member_count
        if amount_microcents is not UNSET:
            field_dict["amount_microcents"] = amount_microcents
        if base_price_eur_per_hour is not UNSET:
            field_dict["base_price_eur_per_hour"] = base_price_eur_per_hour
        if base_price_microcents_per_hour is not UNSET:
            field_dict["base_price_microcents_per_hour"] = base_price_microcents_per_hour
        if base_price_microcents_per_second is not UNSET:
            field_dict["base_price_microcents_per_second"] = base_price_microcents_per_second
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if current_member_price_eur_per_hour is not UNSET:
            field_dict["current_member_price_eur_per_hour"] = current_member_price_eur_per_hour
        if current_member_price_microcents_per_hour is not UNSET:
            field_dict["current_member_price_microcents_per_hour"] = current_member_price_microcents_per_hour
        if effective_from is not UNSET:
            field_dict["effective_from"] = effective_from
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if instance is not UNSET:
            field_dict["instance"] = instance
        if leave_effective_at is not UNSET:
            field_dict["leave_effective_at"] = leave_effective_at
        if left_at is not UNSET:
            field_dict["left_at"] = left_at
        if max_members is not UNSET:
            field_dict["max_members"] = max_members
        if member_price_microcents_per_second is not UNSET:
            field_dict["member_price_microcents_per_second"] = member_price_microcents_per_second
        if membership_id is not UNSET:
            field_dict["membership_id"] = membership_id
        if reservation_attached is not UNSET:
            field_dict["reservation_attached"] = reservation_attached
        if reservation_state is not UNSET:
            field_dict["reservation_state"] = reservation_state
        if role is not UNSET:
            field_dict["role"] = role
        if serving_alias_id is not UNSET:
            field_dict["serving_alias_id"] = serving_alias_id
        if status is not UNSET:
            field_dict["status"] = status
        if suspended_at is not UNSET:
            field_dict["suspended_at"] = suspended_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.shared_capacity_instance_response import SharedCapacityInstanceResponse

        d = dict(src_dict)
        accepted_at = d.pop("accepted_at", UNSET)

        accepted_terms_hash = d.pop("accepted_terms_hash", UNSET)

        accepted_terms_version = d.pop("accepted_terms_version", UNSET)

        active_member_count = d.pop("active_member_count", UNSET)

        amount_microcents = d.pop("amount_microcents", UNSET)

        base_price_eur_per_hour = d.pop("base_price_eur_per_hour", UNSET)

        base_price_microcents_per_hour = d.pop("base_price_microcents_per_hour", UNSET)

        base_price_microcents_per_second = d.pop("base_price_microcents_per_second", UNSET)

        created_at = d.pop("created_at", UNSET)

        current_member_price_eur_per_hour = d.pop("current_member_price_eur_per_hour", UNSET)

        current_member_price_microcents_per_hour = d.pop("current_member_price_microcents_per_hour", UNSET)

        effective_from = d.pop("effective_from", UNSET)

        group_id = d.pop("group_id", UNSET)

        _instance = d.pop("instance", UNSET)
        instance: SharedCapacityInstanceResponse | Unset
        if isinstance(_instance, Unset):
            instance = UNSET
        else:
            instance = SharedCapacityInstanceResponse.from_dict(_instance)

        leave_effective_at = d.pop("leave_effective_at", UNSET)

        left_at = d.pop("left_at", UNSET)

        max_members = d.pop("max_members", UNSET)

        member_price_microcents_per_second = d.pop("member_price_microcents_per_second", UNSET)

        membership_id = d.pop("membership_id", UNSET)

        reservation_attached = d.pop("reservation_attached", UNSET)

        reservation_state = d.pop("reservation_state", UNSET)

        role = d.pop("role", UNSET)

        serving_alias_id = d.pop("serving_alias_id", UNSET)

        status = d.pop("status", UNSET)

        suspended_at = d.pop("suspended_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        shared_capacity_membership_response = cls(
            accepted_at=accepted_at,
            accepted_terms_hash=accepted_terms_hash,
            accepted_terms_version=accepted_terms_version,
            active_member_count=active_member_count,
            amount_microcents=amount_microcents,
            base_price_eur_per_hour=base_price_eur_per_hour,
            base_price_microcents_per_hour=base_price_microcents_per_hour,
            base_price_microcents_per_second=base_price_microcents_per_second,
            created_at=created_at,
            current_member_price_eur_per_hour=current_member_price_eur_per_hour,
            current_member_price_microcents_per_hour=current_member_price_microcents_per_hour,
            effective_from=effective_from,
            group_id=group_id,
            instance=instance,
            leave_effective_at=leave_effective_at,
            left_at=left_at,
            max_members=max_members,
            member_price_microcents_per_second=member_price_microcents_per_second,
            membership_id=membership_id,
            reservation_attached=reservation_attached,
            reservation_state=reservation_state,
            role=role,
            serving_alias_id=serving_alias_id,
            status=status,
            suspended_at=suspended_at,
            updated_at=updated_at,
        )

        shared_capacity_membership_response.additional_properties = d
        return shared_capacity_membership_response

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
