from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_response import AccountResponse


T = TypeVar("T", bound="AccountMembershipResponse")


@_attrs_define
class AccountMembershipResponse:
    """
    Attributes:
        account (AccountResponse | Unset):
        account_id (str | Unset):
        created_at_unix (int | Unset):
        role (str | Unset):
        user_id (str | Unset):
    """

    account: AccountResponse | Unset = UNSET
    account_id: str | Unset = UNSET
    created_at_unix: int | Unset = UNSET
    role: str | Unset = UNSET
    user_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account: dict[str, Any] | Unset = UNSET
        if not isinstance(self.account, Unset):
            account = self.account.to_dict()

        account_id = self.account_id

        created_at_unix = self.created_at_unix

        role = self.role

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account is not UNSET:
            field_dict["account"] = account
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if created_at_unix is not UNSET:
            field_dict["created_at_unix"] = created_at_unix
        if role is not UNSET:
            field_dict["role"] = role
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_response import AccountResponse

        d = dict(src_dict)
        _account = d.pop("account", UNSET)
        account: AccountResponse | Unset
        if isinstance(_account, Unset):
            account = UNSET
        else:
            account = AccountResponse.from_dict(_account)

        account_id = d.pop("account_id", UNSET)

        created_at_unix = d.pop("created_at_unix", UNSET)

        role = d.pop("role", UNSET)

        user_id = d.pop("user_id", UNSET)

        account_membership_response = cls(
            account=account,
            account_id=account_id,
            created_at_unix=created_at_unix,
            role=role,
            user_id=user_id,
        )

        account_membership_response.additional_properties = d
        return account_membership_response

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
