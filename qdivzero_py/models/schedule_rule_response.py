from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScheduleRuleResponse")


@_attrs_define
class ScheduleRuleResponse:
    """
    Attributes:
        action (str | Unset):
        created_at (str | Unset):
        cron (str | Unset):
        desired_replicas (int | Unset):
        enabled (bool | Unset):
        id (str | Unset):
        instance_id (str | Unset):
        last_error (str | Unset):
        last_run_at (str | Unset):
        next_run_at (str | Unset):
        replica_set_id (str | Unset):
        timezone (str | Unset):
        updated_at (str | Unset):
    """

    action: str | Unset = UNSET
    created_at: str | Unset = UNSET
    cron: str | Unset = UNSET
    desired_replicas: int | Unset = UNSET
    enabled: bool | Unset = UNSET
    id: str | Unset = UNSET
    instance_id: str | Unset = UNSET
    last_error: str | Unset = UNSET
    last_run_at: str | Unset = UNSET
    next_run_at: str | Unset = UNSET
    replica_set_id: str | Unset = UNSET
    timezone: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        created_at = self.created_at

        cron = self.cron

        desired_replicas = self.desired_replicas

        enabled = self.enabled

        id = self.id

        instance_id = self.instance_id

        last_error = self.last_error

        last_run_at = self.last_run_at

        next_run_at = self.next_run_at

        replica_set_id = self.replica_set_id

        timezone = self.timezone

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if cron is not UNSET:
            field_dict["cron"] = cron
        if desired_replicas is not UNSET:
            field_dict["desired_replicas"] = desired_replicas
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if id is not UNSET:
            field_dict["id"] = id
        if instance_id is not UNSET:
            field_dict["instance_id"] = instance_id
        if last_error is not UNSET:
            field_dict["last_error"] = last_error
        if last_run_at is not UNSET:
            field_dict["last_run_at"] = last_run_at
        if next_run_at is not UNSET:
            field_dict["next_run_at"] = next_run_at
        if replica_set_id is not UNSET:
            field_dict["replica_set_id"] = replica_set_id
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = d.pop("action", UNSET)

        created_at = d.pop("created_at", UNSET)

        cron = d.pop("cron", UNSET)

        desired_replicas = d.pop("desired_replicas", UNSET)

        enabled = d.pop("enabled", UNSET)

        id = d.pop("id", UNSET)

        instance_id = d.pop("instance_id", UNSET)

        last_error = d.pop("last_error", UNSET)

        last_run_at = d.pop("last_run_at", UNSET)

        next_run_at = d.pop("next_run_at", UNSET)

        replica_set_id = d.pop("replica_set_id", UNSET)

        timezone = d.pop("timezone", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        schedule_rule_response = cls(
            action=action,
            created_at=created_at,
            cron=cron,
            desired_replicas=desired_replicas,
            enabled=enabled,
            id=id,
            instance_id=instance_id,
            last_error=last_error,
            last_run_at=last_run_at,
            next_run_at=next_run_at,
            replica_set_id=replica_set_id,
            timezone=timezone,
            updated_at=updated_at,
        )

        schedule_rule_response.additional_properties = d
        return schedule_rule_response

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
