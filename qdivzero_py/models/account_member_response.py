from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountMemberResponse")



@_attrs_define
class AccountMemberResponse:
    """ 
        Attributes:
            account_id (str | Unset):
            created_at_unix (int | Unset):
            email (str | Unset):
            role (str | Unset):
            user_id (str | Unset):
     """

    account_id: str | Unset = UNSET
    created_at_unix: int | Unset = UNSET
    email: str | Unset = UNSET
    role: str | Unset = UNSET
    user_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        created_at_unix = self.created_at_unix

        email = self.email

        role = self.role

        user_id = self.user_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if created_at_unix is not UNSET:
            field_dict["created_at_unix"] = created_at_unix
        if email is not UNSET:
            field_dict["email"] = email
        if role is not UNSET:
            field_dict["role"] = role
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        created_at_unix = d.pop("created_at_unix", UNSET)

        email = d.pop("email", UNSET)

        role = d.pop("role", UNSET)

        user_id = d.pop("user_id", UNSET)

        account_member_response = cls(
            account_id=account_id,
            created_at_unix=created_at_unix,
            email=email,
            role=role,
            user_id=user_id,
        )


        account_member_response.additional_properties = d
        return account_member_response

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
