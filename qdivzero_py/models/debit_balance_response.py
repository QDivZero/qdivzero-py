from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DebitBalanceResponse")


@_attrs_define
class DebitBalanceResponse:
    """
    Attributes:
        new_balance (float | Unset):
        success (bool | Unset):
    """

    new_balance: float | Unset = UNSET
    success: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        new_balance = self.new_balance

        success = self.success

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if new_balance is not UNSET:
            field_dict["new_balance"] = new_balance
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        new_balance = d.pop("new_balance", UNSET)

        success = d.pop("success", UNSET)

        debit_balance_response = cls(
            new_balance=new_balance,
            success=success,
        )

        debit_balance_response.additional_properties = d
        return debit_balance_response

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
