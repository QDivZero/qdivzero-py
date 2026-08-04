from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.public_pricing_service import PublicPricingService





T = TypeVar("T", bound="PublicPricingResponse")



@_attrs_define
class PublicPricingResponse:
    """ 
        Attributes:
            services (list[PublicPricingService] | Unset):
            updated_at (str | Unset):
            version (int | Unset):
     """

    services: list[PublicPricingService] | Unset = UNSET
    updated_at: str | Unset = UNSET
    version: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        services: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.services, Unset):
            services = []
            for services_item_data in self.services:
                services_item = services_item_data.to_dict()
                services.append(services_item)



        updated_at = self.updated_at

        version = self.version


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if services is not UNSET:
            field_dict["services"] = services
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_pricing_service import PublicPricingService
        d = dict(src_dict)
        _services = d.pop("services", UNSET)
        services: list[PublicPricingService] | Unset = UNSET
        if _services is not UNSET:
            services = []
            for services_item_data in _services:
                services_item = PublicPricingService.from_dict(services_item_data)



                services.append(services_item)


        updated_at = d.pop("updated_at", UNSET)

        version = d.pop("version", UNSET)

        public_pricing_response = cls(
            services=services,
            updated_at=updated_at,
            version=version,
        )


        public_pricing_response.additional_properties = d
        return public_pricing_response

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
