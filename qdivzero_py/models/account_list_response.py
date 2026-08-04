from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.account_membership_response import AccountMembershipResponse





T = TypeVar("T", bound="AccountListResponse")



@_attrs_define
class AccountListResponse:
    """ 
        Attributes:
            memberships (list[AccountMembershipResponse] | Unset):
     """

    memberships: list[AccountMembershipResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        memberships: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.memberships, Unset):
            memberships = []
            for memberships_item_data in self.memberships:
                memberships_item = memberships_item_data.to_dict()
                memberships.append(memberships_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if memberships is not UNSET:
            field_dict["memberships"] = memberships

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_membership_response import AccountMembershipResponse
        d = dict(src_dict)
        _memberships = d.pop("memberships", UNSET)
        memberships: list[AccountMembershipResponse] | Unset = UNSET
        if _memberships is not UNSET:
            memberships = []
            for memberships_item_data in _memberships:
                memberships_item = AccountMembershipResponse.from_dict(memberships_item_data)



                memberships.append(memberships_item)


        account_list_response = cls(
            memberships=memberships,
        )


        account_list_response.additional_properties = d
        return account_list_response

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
