from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicPricingAvailability")



@_attrs_define
class PublicPricingAvailability:
    """ 
        Attributes:
            count (int | Unset):
            status (str | Unset):
            total (int | Unset):
     """

    count: int | Unset = UNSET
    status: str | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        count = self.count

        status = self.status

        total = self.total


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if count is not UNSET:
            field_dict["count"] = count
        if status is not UNSET:
            field_dict["status"] = status
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count", UNSET)

        status = d.pop("status", UNSET)

        total = d.pop("total", UNSET)

        public_pricing_availability = cls(
            count=count,
            status=status,
            total=total,
        )


        public_pricing_availability.additional_properties = d
        return public_pricing_availability

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
