from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckoutQuoteRequest")



@_attrs_define
class CheckoutQuoteRequest:
    """ 
        Attributes:
            amount_cents (float | Unset):
            currency (str | Unset):
            discount_code (str | Unset):
     """

    amount_cents: float | Unset = UNSET
    currency: str | Unset = UNSET
    discount_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        amount_cents = self.amount_cents

        currency = self.currency

        discount_code = self.discount_code


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if amount_cents is not UNSET:
            field_dict["amount_cents"] = amount_cents
        if currency is not UNSET:
            field_dict["currency"] = currency
        if discount_code is not UNSET:
            field_dict["discount_code"] = discount_code

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount_cents = d.pop("amount_cents", UNSET)

        currency = d.pop("currency", UNSET)

        discount_code = d.pop("discount_code", UNSET)

        checkout_quote_request = cls(
            amount_cents=amount_cents,
            currency=currency,
            discount_code=discount_code,
        )


        checkout_quote_request.additional_properties = d
        return checkout_quote_request

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
