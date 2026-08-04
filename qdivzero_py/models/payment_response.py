from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PaymentResponse")



@_attrs_define
class PaymentResponse:
    """ 
        Attributes:
            account_id (str | Unset):
            amount_credit_base_minor (int | Unset):
            amount_discount_minor (int | Unset):
            amount_subtotal_minor (int | Unset):
            amount_tax_minor (int | Unset):
            amount_total_minor (int | Unset):
            created_at (str | Unset):
            credited_at (str | Unset):
            credited_eur_cents (int | Unset):
            currency (str | Unset):
            discount_code_snapshot (str | Unset):
            discount_ticket_id (str | Unset):
            holded_contact_id (str | Unset):
            holded_invoice_id (str | Unset):
            holded_invoice_number (str | Unset):
            holded_invoice_status (str | Unset):
            holded_invoice_url (str | Unset):
            id (str | Unset):
            invoice_state (str | Unset):
            ledger_entry_id (str | Unset):
            paid_at (str | Unset):
            provider (str | Unset):
            reference (str | Unset):
            status (str | Unset):
            stripe_customer_id (str | Unset):
            stripe_event_id (str | Unset):
            stripe_payment_intent_id (str | Unset):
            stripe_session_id (str | Unset):
            updated_at (str | Unset):
     """

    account_id: str | Unset = UNSET
    amount_credit_base_minor: int | Unset = UNSET
    amount_discount_minor: int | Unset = UNSET
    amount_subtotal_minor: int | Unset = UNSET
    amount_tax_minor: int | Unset = UNSET
    amount_total_minor: int | Unset = UNSET
    created_at: str | Unset = UNSET
    credited_at: str | Unset = UNSET
    credited_eur_cents: int | Unset = UNSET
    currency: str | Unset = UNSET
    discount_code_snapshot: str | Unset = UNSET
    discount_ticket_id: str | Unset = UNSET
    holded_contact_id: str | Unset = UNSET
    holded_invoice_id: str | Unset = UNSET
    holded_invoice_number: str | Unset = UNSET
    holded_invoice_status: str | Unset = UNSET
    holded_invoice_url: str | Unset = UNSET
    id: str | Unset = UNSET
    invoice_state: str | Unset = UNSET
    ledger_entry_id: str | Unset = UNSET
    paid_at: str | Unset = UNSET
    provider: str | Unset = UNSET
    reference: str | Unset = UNSET
    status: str | Unset = UNSET
    stripe_customer_id: str | Unset = UNSET
    stripe_event_id: str | Unset = UNSET
    stripe_payment_intent_id: str | Unset = UNSET
    stripe_session_id: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        amount_credit_base_minor = self.amount_credit_base_minor

        amount_discount_minor = self.amount_discount_minor

        amount_subtotal_minor = self.amount_subtotal_minor

        amount_tax_minor = self.amount_tax_minor

        amount_total_minor = self.amount_total_minor

        created_at = self.created_at

        credited_at = self.credited_at

        credited_eur_cents = self.credited_eur_cents

        currency = self.currency

        discount_code_snapshot = self.discount_code_snapshot

        discount_ticket_id = self.discount_ticket_id

        holded_contact_id = self.holded_contact_id

        holded_invoice_id = self.holded_invoice_id

        holded_invoice_number = self.holded_invoice_number

        holded_invoice_status = self.holded_invoice_status

        holded_invoice_url = self.holded_invoice_url

        id = self.id

        invoice_state = self.invoice_state

        ledger_entry_id = self.ledger_entry_id

        paid_at = self.paid_at

        provider = self.provider

        reference = self.reference

        status = self.status

        stripe_customer_id = self.stripe_customer_id

        stripe_event_id = self.stripe_event_id

        stripe_payment_intent_id = self.stripe_payment_intent_id

        stripe_session_id = self.stripe_session_id

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if amount_credit_base_minor is not UNSET:
            field_dict["amount_credit_base_minor"] = amount_credit_base_minor
        if amount_discount_minor is not UNSET:
            field_dict["amount_discount_minor"] = amount_discount_minor
        if amount_subtotal_minor is not UNSET:
            field_dict["amount_subtotal_minor"] = amount_subtotal_minor
        if amount_tax_minor is not UNSET:
            field_dict["amount_tax_minor"] = amount_tax_minor
        if amount_total_minor is not UNSET:
            field_dict["amount_total_minor"] = amount_total_minor
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if credited_at is not UNSET:
            field_dict["credited_at"] = credited_at
        if credited_eur_cents is not UNSET:
            field_dict["credited_eur_cents"] = credited_eur_cents
        if currency is not UNSET:
            field_dict["currency"] = currency
        if discount_code_snapshot is not UNSET:
            field_dict["discount_code_snapshot"] = discount_code_snapshot
        if discount_ticket_id is not UNSET:
            field_dict["discount_ticket_id"] = discount_ticket_id
        if holded_contact_id is not UNSET:
            field_dict["holded_contact_id"] = holded_contact_id
        if holded_invoice_id is not UNSET:
            field_dict["holded_invoice_id"] = holded_invoice_id
        if holded_invoice_number is not UNSET:
            field_dict["holded_invoice_number"] = holded_invoice_number
        if holded_invoice_status is not UNSET:
            field_dict["holded_invoice_status"] = holded_invoice_status
        if holded_invoice_url is not UNSET:
            field_dict["holded_invoice_url"] = holded_invoice_url
        if id is not UNSET:
            field_dict["id"] = id
        if invoice_state is not UNSET:
            field_dict["invoice_state"] = invoice_state
        if ledger_entry_id is not UNSET:
            field_dict["ledger_entry_id"] = ledger_entry_id
        if paid_at is not UNSET:
            field_dict["paid_at"] = paid_at
        if provider is not UNSET:
            field_dict["provider"] = provider
        if reference is not UNSET:
            field_dict["reference"] = reference
        if status is not UNSET:
            field_dict["status"] = status
        if stripe_customer_id is not UNSET:
            field_dict["stripe_customer_id"] = stripe_customer_id
        if stripe_event_id is not UNSET:
            field_dict["stripe_event_id"] = stripe_event_id
        if stripe_payment_intent_id is not UNSET:
            field_dict["stripe_payment_intent_id"] = stripe_payment_intent_id
        if stripe_session_id is not UNSET:
            field_dict["stripe_session_id"] = stripe_session_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        amount_credit_base_minor = d.pop("amount_credit_base_minor", UNSET)

        amount_discount_minor = d.pop("amount_discount_minor", UNSET)

        amount_subtotal_minor = d.pop("amount_subtotal_minor", UNSET)

        amount_tax_minor = d.pop("amount_tax_minor", UNSET)

        amount_total_minor = d.pop("amount_total_minor", UNSET)

        created_at = d.pop("created_at", UNSET)

        credited_at = d.pop("credited_at", UNSET)

        credited_eur_cents = d.pop("credited_eur_cents", UNSET)

        currency = d.pop("currency", UNSET)

        discount_code_snapshot = d.pop("discount_code_snapshot", UNSET)

        discount_ticket_id = d.pop("discount_ticket_id", UNSET)

        holded_contact_id = d.pop("holded_contact_id", UNSET)

        holded_invoice_id = d.pop("holded_invoice_id", UNSET)

        holded_invoice_number = d.pop("holded_invoice_number", UNSET)

        holded_invoice_status = d.pop("holded_invoice_status", UNSET)

        holded_invoice_url = d.pop("holded_invoice_url", UNSET)

        id = d.pop("id", UNSET)

        invoice_state = d.pop("invoice_state", UNSET)

        ledger_entry_id = d.pop("ledger_entry_id", UNSET)

        paid_at = d.pop("paid_at", UNSET)

        provider = d.pop("provider", UNSET)

        reference = d.pop("reference", UNSET)

        status = d.pop("status", UNSET)

        stripe_customer_id = d.pop("stripe_customer_id", UNSET)

        stripe_event_id = d.pop("stripe_event_id", UNSET)

        stripe_payment_intent_id = d.pop("stripe_payment_intent_id", UNSET)

        stripe_session_id = d.pop("stripe_session_id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        payment_response = cls(
            account_id=account_id,
            amount_credit_base_minor=amount_credit_base_minor,
            amount_discount_minor=amount_discount_minor,
            amount_subtotal_minor=amount_subtotal_minor,
            amount_tax_minor=amount_tax_minor,
            amount_total_minor=amount_total_minor,
            created_at=created_at,
            credited_at=credited_at,
            credited_eur_cents=credited_eur_cents,
            currency=currency,
            discount_code_snapshot=discount_code_snapshot,
            discount_ticket_id=discount_ticket_id,
            holded_contact_id=holded_contact_id,
            holded_invoice_id=holded_invoice_id,
            holded_invoice_number=holded_invoice_number,
            holded_invoice_status=holded_invoice_status,
            holded_invoice_url=holded_invoice_url,
            id=id,
            invoice_state=invoice_state,
            ledger_entry_id=ledger_entry_id,
            paid_at=paid_at,
            provider=provider,
            reference=reference,
            status=status,
            stripe_customer_id=stripe_customer_id,
            stripe_event_id=stripe_event_id,
            stripe_payment_intent_id=stripe_payment_intent_id,
            stripe_session_id=stripe_session_id,
            updated_at=updated_at,
        )


        payment_response.additional_properties = d
        return payment_response

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
