from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InstanceUsageSummaryResponse")


@_attrs_define
class InstanceUsageSummaryResponse:
    """
    Attributes:
        month_billable_seconds (int | Unset):
        month_daily_average_cost_eur (float | Unset):
        month_total_cost_eur (float | Unset):
    """

    month_billable_seconds: int | Unset = UNSET
    month_daily_average_cost_eur: float | Unset = UNSET
    month_total_cost_eur: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        month_billable_seconds = self.month_billable_seconds

        month_daily_average_cost_eur = self.month_daily_average_cost_eur

        month_total_cost_eur = self.month_total_cost_eur

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if month_billable_seconds is not UNSET:
            field_dict["month_billable_seconds"] = month_billable_seconds
        if month_daily_average_cost_eur is not UNSET:
            field_dict["month_daily_average_cost_eur"] = month_daily_average_cost_eur
        if month_total_cost_eur is not UNSET:
            field_dict["month_total_cost_eur"] = month_total_cost_eur

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        month_billable_seconds = d.pop("month_billable_seconds", UNSET)

        month_daily_average_cost_eur = d.pop("month_daily_average_cost_eur", UNSET)

        month_total_cost_eur = d.pop("month_total_cost_eur", UNSET)

        instance_usage_summary_response = cls(
            month_billable_seconds=month_billable_seconds,
            month_daily_average_cost_eur=month_daily_average_cost_eur,
            month_total_cost_eur=month_total_cost_eur,
        )

        instance_usage_summary_response.additional_properties = d
        return instance_usage_summary_response

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
