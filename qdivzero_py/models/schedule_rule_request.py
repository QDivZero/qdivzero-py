from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScheduleRuleRequest")



@_attrs_define
class ScheduleRuleRequest:
    """ 
        Attributes:
            action (str | Unset):
            cron (str | Unset):
            desired_replicas (int | Unset):
            enabled (bool | Unset):
            replica_set_id (str | Unset):
            timezone (str | Unset):
     """

    action: str | Unset = UNSET
    cron: str | Unset = UNSET
    desired_replicas: int | Unset = UNSET
    enabled: bool | Unset = UNSET
    replica_set_id: str | Unset = UNSET
    timezone: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        action = self.action

        cron = self.cron

        desired_replicas = self.desired_replicas

        enabled = self.enabled

        replica_set_id = self.replica_set_id

        timezone = self.timezone


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if action is not UNSET:
            field_dict["action"] = action
        if cron is not UNSET:
            field_dict["cron"] = cron
        if desired_replicas is not UNSET:
            field_dict["desired_replicas"] = desired_replicas
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if replica_set_id is not UNSET:
            field_dict["replica_set_id"] = replica_set_id
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = d.pop("action", UNSET)

        cron = d.pop("cron", UNSET)

        desired_replicas = d.pop("desired_replicas", UNSET)

        enabled = d.pop("enabled", UNSET)

        replica_set_id = d.pop("replica_set_id", UNSET)

        timezone = d.pop("timezone", UNSET)

        schedule_rule_request = cls(
            action=action,
            cron=cron,
            desired_replicas=desired_replicas,
            enabled=enabled,
            replica_set_id=replica_set_id,
            timezone=timezone,
        )


        schedule_rule_request.additional_properties = d
        return schedule_rule_request

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
