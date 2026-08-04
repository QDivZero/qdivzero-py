from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckoutQuoteResponse")



@_attrs_define
class CheckoutQuoteResponse:
    """ 
        Attributes:
            currency (str | Unset):
            discount_amount_minor (int | Unset):
            gross_total_minor (int | Unset):
            original_amount_minor (int | Unset):
            policy_version (str | Unset):
            quote_hash (str | Unset):
            quote_id (str | Unset):
            reason (str | Unset):
            reverse_charge (bool | Unset):
            tax_included (bool | Unset):
            tax_minor (int | Unset):
            tax_rate_basis_points (int | Unset):
            taxable_base_minor (int | Unset):
     """

    currency: str | Unset = UNSET
    discount_amount_minor: int | Unset = UNSET
    gross_total_minor: int | Unset = UNSET
    original_amount_minor: int | Unset = UNSET
    policy_version: str | Unset = UNSET
    quote_hash: str | Unset = UNSET
    quote_id: str | Unset = UNSET
    reason: str | Unset = UNSET
    reverse_charge: bool | Unset = UNSET
    tax_included: bool | Unset = UNSET
    tax_minor: int | Unset = UNSET
    tax_rate_basis_points: int | Unset = UNSET
    taxable_base_minor: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        discount_amount_minor = self.discount_amount_minor

        gross_total_minor = self.gross_total_minor

        original_amount_minor = self.original_amount_minor

        policy_version = self.policy_version

        quote_hash = self.quote_hash

        quote_id = self.quote_id

        reason = self.reason

        reverse_charge = self.reverse_charge

        tax_included = self.tax_included

        tax_minor = self.tax_minor

        tax_rate_basis_points = self.tax_rate_basis_points

        taxable_base_minor = self.taxable_base_minor


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if currency is not UNSET:
            field_dict["currency"] = currency
        if discount_amount_minor is not UNSET:
            field_dict["discount_amount_minor"] = discount_amount_minor
        if gross_total_minor is not UNSET:
            field_dict["gross_total_minor"] = gross_total_minor
        if original_amount_minor is not UNSET:
            field_dict["original_amount_minor"] = original_amount_minor
        if policy_version is not UNSET:
            field_dict["policy_version"] = policy_version
        if quote_hash is not UNSET:
            field_dict["quote_hash"] = quote_hash
        if quote_id is not UNSET:
            field_dict["quote_id"] = quote_id
        if reason is not UNSET:
            field_dict["reason"] = reason
        if reverse_charge is not UNSET:
            field_dict["reverse_charge"] = reverse_charge
        if tax_included is not UNSET:
            field_dict["tax_included"] = tax_included
        if tax_minor is not UNSET:
            field_dict["tax_minor"] = tax_minor
        if tax_rate_basis_points is not UNSET:
            field_dict["tax_rate_basis_points"] = tax_rate_basis_points
        if taxable_base_minor is not UNSET:
            field_dict["taxable_base_minor"] = taxable_base_minor

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency = d.pop("currency", UNSET)

        discount_amount_minor = d.pop("discount_amount_minor", UNSET)

        gross_total_minor = d.pop("gross_total_minor", UNSET)

        original_amount_minor = d.pop("original_amount_minor", UNSET)

        policy_version = d.pop("policy_version", UNSET)

        quote_hash = d.pop("quote_hash", UNSET)

        quote_id = d.pop("quote_id", UNSET)

        reason = d.pop("reason", UNSET)

        reverse_charge = d.pop("reverse_charge", UNSET)

        tax_included = d.pop("tax_included", UNSET)

        tax_minor = d.pop("tax_minor", UNSET)

        tax_rate_basis_points = d.pop("tax_rate_basis_points", UNSET)

        taxable_base_minor = d.pop("taxable_base_minor", UNSET)

        checkout_quote_response = cls(
            currency=currency,
            discount_amount_minor=discount_amount_minor,
            gross_total_minor=gross_total_minor,
            original_amount_minor=original_amount_minor,
            policy_version=policy_version,
            quote_hash=quote_hash,
            quote_id=quote_id,
            reason=reason,
            reverse_charge=reverse_charge,
            tax_included=tax_included,
            tax_minor=tax_minor,
            tax_rate_basis_points=tax_rate_basis_points,
            taxable_base_minor=taxable_base_minor,
        )


        checkout_quote_response.additional_properties = d
        return checkout_quote_response

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
