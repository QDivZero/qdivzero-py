from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateFiscalProfileRequest")



@_attrs_define
class UpdateFiscalProfileRequest:
    """ 
        Attributes:
            fiscal_address (str | Unset):
            fiscal_city (str | Unset):
            fiscal_company_name (str | Unset):
            fiscal_country (str | Unset):
            fiscal_customer_type (str | Unset):
            fiscal_invoice_email (str | Unset):
            fiscal_legal_name (str | Unset):
            fiscal_postcode (str | Unset):
            fiscal_profile_completed (bool | Unset):
            fiscal_region (str | Unset):
            fiscal_tax_id (str | Unset):
            fiscal_vat_validated (bool | Unset):
     """

    fiscal_address: str | Unset = UNSET
    fiscal_city: str | Unset = UNSET
    fiscal_company_name: str | Unset = UNSET
    fiscal_country: str | Unset = UNSET
    fiscal_customer_type: str | Unset = UNSET
    fiscal_invoice_email: str | Unset = UNSET
    fiscal_legal_name: str | Unset = UNSET
    fiscal_postcode: str | Unset = UNSET
    fiscal_profile_completed: bool | Unset = UNSET
    fiscal_region: str | Unset = UNSET
    fiscal_tax_id: str | Unset = UNSET
    fiscal_vat_validated: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        fiscal_address = self.fiscal_address

        fiscal_city = self.fiscal_city

        fiscal_company_name = self.fiscal_company_name

        fiscal_country = self.fiscal_country

        fiscal_customer_type = self.fiscal_customer_type

        fiscal_invoice_email = self.fiscal_invoice_email

        fiscal_legal_name = self.fiscal_legal_name

        fiscal_postcode = self.fiscal_postcode

        fiscal_profile_completed = self.fiscal_profile_completed

        fiscal_region = self.fiscal_region

        fiscal_tax_id = self.fiscal_tax_id

        fiscal_vat_validated = self.fiscal_vat_validated


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if fiscal_address is not UNSET:
            field_dict["fiscal_address"] = fiscal_address
        if fiscal_city is not UNSET:
            field_dict["fiscal_city"] = fiscal_city
        if fiscal_company_name is not UNSET:
            field_dict["fiscal_company_name"] = fiscal_company_name
        if fiscal_country is not UNSET:
            field_dict["fiscal_country"] = fiscal_country
        if fiscal_customer_type is not UNSET:
            field_dict["fiscal_customer_type"] = fiscal_customer_type
        if fiscal_invoice_email is not UNSET:
            field_dict["fiscal_invoice_email"] = fiscal_invoice_email
        if fiscal_legal_name is not UNSET:
            field_dict["fiscal_legal_name"] = fiscal_legal_name
        if fiscal_postcode is not UNSET:
            field_dict["fiscal_postcode"] = fiscal_postcode
        if fiscal_profile_completed is not UNSET:
            field_dict["fiscal_profile_completed"] = fiscal_profile_completed
        if fiscal_region is not UNSET:
            field_dict["fiscal_region"] = fiscal_region
        if fiscal_tax_id is not UNSET:
            field_dict["fiscal_tax_id"] = fiscal_tax_id
        if fiscal_vat_validated is not UNSET:
            field_dict["fiscal_vat_validated"] = fiscal_vat_validated

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fiscal_address = d.pop("fiscal_address", UNSET)

        fiscal_city = d.pop("fiscal_city", UNSET)

        fiscal_company_name = d.pop("fiscal_company_name", UNSET)

        fiscal_country = d.pop("fiscal_country", UNSET)

        fiscal_customer_type = d.pop("fiscal_customer_type", UNSET)

        fiscal_invoice_email = d.pop("fiscal_invoice_email", UNSET)

        fiscal_legal_name = d.pop("fiscal_legal_name", UNSET)

        fiscal_postcode = d.pop("fiscal_postcode", UNSET)

        fiscal_profile_completed = d.pop("fiscal_profile_completed", UNSET)

        fiscal_region = d.pop("fiscal_region", UNSET)

        fiscal_tax_id = d.pop("fiscal_tax_id", UNSET)

        fiscal_vat_validated = d.pop("fiscal_vat_validated", UNSET)

        update_fiscal_profile_request = cls(
            fiscal_address=fiscal_address,
            fiscal_city=fiscal_city,
            fiscal_company_name=fiscal_company_name,
            fiscal_country=fiscal_country,
            fiscal_customer_type=fiscal_customer_type,
            fiscal_invoice_email=fiscal_invoice_email,
            fiscal_legal_name=fiscal_legal_name,
            fiscal_postcode=fiscal_postcode,
            fiscal_profile_completed=fiscal_profile_completed,
            fiscal_region=fiscal_region,
            fiscal_tax_id=fiscal_tax_id,
            fiscal_vat_validated=fiscal_vat_validated,
        )


        update_fiscal_profile_request.additional_properties = d
        return update_fiscal_profile_request

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
