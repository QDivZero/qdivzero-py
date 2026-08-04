from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.public_pricing_gpu import PublicPricingGPU





T = TypeVar("T", bound="PublicPricingService")



@_attrs_define
class PublicPricingService:
    """ 
        Attributes:
            billing_model (str | Unset):
            currency (str | Unset):
            gpus (list[PublicPricingGPU] | Unset):
            id (str | Unset):
            name (str | Unset):
            price_eur_per_gb_hour (float | Unset):
            status (str | Unset):
            unit (str | Unset):
     """

    billing_model: str | Unset = UNSET
    currency: str | Unset = UNSET
    gpus: list[PublicPricingGPU] | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    price_eur_per_gb_hour: float | Unset = UNSET
    status: str | Unset = UNSET
    unit: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        billing_model = self.billing_model

        currency = self.currency

        gpus: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.gpus, Unset):
            gpus = []
            for gpus_item_data in self.gpus:
                gpus_item = gpus_item_data.to_dict()
                gpus.append(gpus_item)



        id = self.id

        name = self.name

        price_eur_per_gb_hour = self.price_eur_per_gb_hour

        status = self.status

        unit = self.unit


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if billing_model is not UNSET:
            field_dict["billing_model"] = billing_model
        if currency is not UNSET:
            field_dict["currency"] = currency
        if gpus is not UNSET:
            field_dict["gpus"] = gpus
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if price_eur_per_gb_hour is not UNSET:
            field_dict["price_eur_per_gb_hour"] = price_eur_per_gb_hour
        if status is not UNSET:
            field_dict["status"] = status
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_pricing_gpu import PublicPricingGPU
        d = dict(src_dict)
        billing_model = d.pop("billing_model", UNSET)

        currency = d.pop("currency", UNSET)

        _gpus = d.pop("gpus", UNSET)
        gpus: list[PublicPricingGPU] | Unset = UNSET
        if _gpus is not UNSET:
            gpus = []
            for gpus_item_data in _gpus:
                gpus_item = PublicPricingGPU.from_dict(gpus_item_data)



                gpus.append(gpus_item)


        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        price_eur_per_gb_hour = d.pop("price_eur_per_gb_hour", UNSET)

        status = d.pop("status", UNSET)

        unit = d.pop("unit", UNSET)

        public_pricing_service = cls(
            billing_model=billing_model,
            currency=currency,
            gpus=gpus,
            id=id,
            name=name,
            price_eur_per_gb_hour=price_eur_per_gb_hour,
            status=status,
            unit=unit,
        )


        public_pricing_service.additional_properties = d
        return public_pricing_service

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
