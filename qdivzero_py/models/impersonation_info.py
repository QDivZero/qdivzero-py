from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImpersonationInfo")


@_attrs_define
class ImpersonationInfo:
    """
    Attributes:
        impersonator_email (str | Unset):
        impersonator_user_id (str | Unset):
    """

    impersonator_email: str | Unset = UNSET
    impersonator_user_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        impersonator_email = self.impersonator_email

        impersonator_user_id = self.impersonator_user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if impersonator_email is not UNSET:
            field_dict["impersonator_email"] = impersonator_email
        if impersonator_user_id is not UNSET:
            field_dict["impersonator_user_id"] = impersonator_user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        impersonator_email = d.pop("impersonator_email", UNSET)

        impersonator_user_id = d.pop("impersonator_user_id", UNSET)

        impersonation_info = cls(
            impersonator_email=impersonator_email,
            impersonator_user_id=impersonator_user_id,
        )

        impersonation_info.additional_properties = d
        return impersonation_info

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
