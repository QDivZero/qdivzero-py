from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.public_endpoint_price_response import PublicEndpointPriceResponse


T = TypeVar("T", bound="PublicEndpointResponse")


@_attrs_define
class PublicEndpointResponse:
    """
    Attributes:
        name (str | Unset):
        price (PublicEndpointPriceResponse | Unset):
    """

    name: str | Unset = UNSET
    price: PublicEndpointPriceResponse | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.price, Unset):
            price = self.price.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if price is not UNSET:
            field_dict["price"] = price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_endpoint_price_response import PublicEndpointPriceResponse

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _price = d.pop("price", UNSET)
        price: PublicEndpointPriceResponse | Unset
        if isinstance(_price, Unset):
            price = UNSET
        else:
            price = PublicEndpointPriceResponse.from_dict(_price)

        public_endpoint_response = cls(
            name=name,
            price=price,
        )

        public_endpoint_response.additional_properties = d
        return public_endpoint_response

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
