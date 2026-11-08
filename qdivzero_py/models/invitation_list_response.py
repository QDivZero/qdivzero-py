from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invitation_response import InvitationResponse


T = TypeVar("T", bound="InvitationListResponse")


@_attrs_define
class InvitationListResponse:
    """
    Attributes:
        invitations (list[InvitationResponse] | Unset):
    """

    invitations: list[InvitationResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        invitations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.invitations, Unset):
            invitations = []
            for invitations_item_data in self.invitations:
                invitations_item = invitations_item_data.to_dict()
                invitations.append(invitations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invitations is not UNSET:
            field_dict["invitations"] = invitations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invitation_response import InvitationResponse

        d = dict(src_dict)
        _invitations = d.pop("invitations", UNSET)
        invitations: list[InvitationResponse] | Unset = UNSET
        if _invitations is not UNSET:
            invitations = []
            for invitations_item_data in _invitations:
                invitations_item = InvitationResponse.from_dict(invitations_item_data)

                invitations.append(invitations_item)

        invitation_list_response = cls(
            invitations=invitations,
        )

        invitation_list_response.additional_properties = d
        return invitation_list_response

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
