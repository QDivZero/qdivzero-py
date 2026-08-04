from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.public_pricing_availability import PublicPricingAvailability





T = TypeVar("T", bound="PublicPricingGPU")



@_attrs_define
class PublicPricingGPU:
    """ 
        Attributes:
            availability (PublicPricingAvailability | Unset):
            capacity_tier (str | Unset):
            city (str | Unset):
            country (str | Unset):
            display_name (str | Unset):
            gpu_count (int | Unset):
            market_type (str | Unset):
            price_eur_per_hour (float | Unset):
            provider_codename (str | Unset):
            public_gpu_id (str | Unset):
            region (str | Unset):
            vram_gb (float | Unset):
     """

    availability: PublicPricingAvailability | Unset = UNSET
    capacity_tier: str | Unset = UNSET
    city: str | Unset = UNSET
    country: str | Unset = UNSET
    display_name: str | Unset = UNSET
    gpu_count: int | Unset = UNSET
    market_type: str | Unset = UNSET
    price_eur_per_hour: float | Unset = UNSET
    provider_codename: str | Unset = UNSET
    public_gpu_id: str | Unset = UNSET
    region: str | Unset = UNSET
    vram_gb: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        availability: dict[str, Any] | Unset = UNSET
        if not isinstance(self.availability, Unset):
            availability = self.availability.to_dict()

        capacity_tier = self.capacity_tier

        city = self.city

        country = self.country

        display_name = self.display_name

        gpu_count = self.gpu_count

        market_type = self.market_type

        price_eur_per_hour = self.price_eur_per_hour

        provider_codename = self.provider_codename

        public_gpu_id = self.public_gpu_id

        region = self.region

        vram_gb = self.vram_gb


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if availability is not UNSET:
            field_dict["availability"] = availability
        if capacity_tier is not UNSET:
            field_dict["capacity_tier"] = capacity_tier
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if gpu_count is not UNSET:
            field_dict["gpu_count"] = gpu_count
        if market_type is not UNSET:
            field_dict["market_type"] = market_type
        if price_eur_per_hour is not UNSET:
            field_dict["price_eur_per_hour"] = price_eur_per_hour
        if provider_codename is not UNSET:
            field_dict["provider_codename"] = provider_codename
        if public_gpu_id is not UNSET:
            field_dict["public_gpu_id"] = public_gpu_id
        if region is not UNSET:
            field_dict["region"] = region
        if vram_gb is not UNSET:
            field_dict["vram_gb"] = vram_gb

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_pricing_availability import PublicPricingAvailability
        d = dict(src_dict)
        _availability = d.pop("availability", UNSET)
        availability: PublicPricingAvailability | Unset
        if isinstance(_availability,  Unset):
            availability = UNSET
        else:
            availability = PublicPricingAvailability.from_dict(_availability)




        capacity_tier = d.pop("capacity_tier", UNSET)

        city = d.pop("city", UNSET)

        country = d.pop("country", UNSET)

        display_name = d.pop("display_name", UNSET)

        gpu_count = d.pop("gpu_count", UNSET)

        market_type = d.pop("market_type", UNSET)

        price_eur_per_hour = d.pop("price_eur_per_hour", UNSET)

        provider_codename = d.pop("provider_codename", UNSET)

        public_gpu_id = d.pop("public_gpu_id", UNSET)

        region = d.pop("region", UNSET)

        vram_gb = d.pop("vram_gb", UNSET)

        public_pricing_gpu = cls(
            availability=availability,
            capacity_tier=capacity_tier,
            city=city,
            country=country,
            display_name=display_name,
            gpu_count=gpu_count,
            market_type=market_type,
            price_eur_per_hour=price_eur_per_hour,
            provider_codename=provider_codename,
            public_gpu_id=public_gpu_id,
            region=region,
            vram_gb=vram_gb,
        )


        public_pricing_gpu.additional_properties = d
        return public_pricing_gpu

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
