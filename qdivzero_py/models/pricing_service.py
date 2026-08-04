from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PricingService")



@_attrs_define
class PricingService:
    """ 
        Attributes:
            currency (str | Unset):
            id (str | Unset):
            price_eur_per_gb_hour (float | Unset):
            status (str | Unset):
     """

    currency: str | Unset = UNSET
    id: str | Unset = UNSET
    price_eur_per_gb_hour: float | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        id = self.id

        price_eur_per_gb_hour = self.price_eur_per_gb_hour

        status = self.status


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if currency is not UNSET:
            field_dict["currency"] = currency
        if id is not UNSET:
            field_dict["id"] = id
        if price_eur_per_gb_hour is not UNSET:
            field_dict["price_eur_per_gb_hour"] = price_eur_per_gb_hour
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency = d.pop("currency", UNSET)

        id = d.pop("id", UNSET)

        price_eur_per_gb_hour = d.pop("price_eur_per_gb_hour", UNSET)

        status = d.pop("status", UNSET)

        pricing_service = cls(
            currency=currency,
            id=id,
            price_eur_per_gb_hour=price_eur_per_gb_hour,
            status=status,
        )


        pricing_service.additional_properties = d
        return pricing_service

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
