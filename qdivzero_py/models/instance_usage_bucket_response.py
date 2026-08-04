from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InstanceUsageBucketResponse")



@_attrs_define
class InstanceUsageBucketResponse:
    """ 
        Attributes:
            billable_seconds (int | Unset):
            cost_eur (float | Unset):
            end_at (str | Unset):
            start_at (str | Unset):
     """

    billable_seconds: int | Unset = UNSET
    cost_eur: float | Unset = UNSET
    end_at: str | Unset = UNSET
    start_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        billable_seconds = self.billable_seconds

        cost_eur = self.cost_eur

        end_at = self.end_at

        start_at = self.start_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if billable_seconds is not UNSET:
            field_dict["billable_seconds"] = billable_seconds
        if cost_eur is not UNSET:
            field_dict["cost_eur"] = cost_eur
        if end_at is not UNSET:
            field_dict["end_at"] = end_at
        if start_at is not UNSET:
            field_dict["start_at"] = start_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        billable_seconds = d.pop("billable_seconds", UNSET)

        cost_eur = d.pop("cost_eur", UNSET)

        end_at = d.pop("end_at", UNSET)

        start_at = d.pop("start_at", UNSET)

        instance_usage_bucket_response = cls(
            billable_seconds=billable_seconds,
            cost_eur=cost_eur,
            end_at=end_at,
            start_at=start_at,
        )


        instance_usage_bucket_response.additional_properties = d
        return instance_usage_bucket_response

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
