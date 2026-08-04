from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LedgerEntryResponse")



@_attrs_define
class LedgerEntryResponse:
    """ 
        Attributes:
            account_id (str | Unset):
            amount (float | Unset):
            balance (float | Unset):
            created_at (str | Unset):
            event_type (str | Unset):
            id (str | Unset):
            reference (str | Unset):
     """

    account_id: str | Unset = UNSET
    amount: float | Unset = UNSET
    balance: float | Unset = UNSET
    created_at: str | Unset = UNSET
    event_type: str | Unset = UNSET
    id: str | Unset = UNSET
    reference: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        amount = self.amount

        balance = self.balance

        created_at = self.created_at

        event_type = self.event_type

        id = self.id

        reference = self.reference


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if balance is not UNSET:
            field_dict["balance"] = balance
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if event_type is not UNSET:
            field_dict["event_type"] = event_type
        if id is not UNSET:
            field_dict["id"] = id
        if reference is not UNSET:
            field_dict["reference"] = reference

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        amount = d.pop("amount", UNSET)

        balance = d.pop("balance", UNSET)

        created_at = d.pop("created_at", UNSET)

        event_type = d.pop("event_type", UNSET)

        id = d.pop("id", UNSET)

        reference = d.pop("reference", UNSET)

        ledger_entry_response = cls(
            account_id=account_id,
            amount=amount,
            balance=balance,
            created_at=created_at,
            event_type=event_type,
            id=id,
            reference=reference,
        )


        ledger_entry_response.additional_properties = d
        return ledger_entry_response

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
