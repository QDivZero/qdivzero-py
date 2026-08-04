from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RefreshResponse")



@_attrs_define
class RefreshResponse:
    """ 
        Attributes:
            access_token (str | Unset):
            access_token_expiry (int | Unset):
     """

    access_token: str | Unset = UNSET
    access_token_expiry: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        access_token = self.access_token

        access_token_expiry = self.access_token_expiry


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if access_token is not UNSET:
            field_dict["access_token"] = access_token
        if access_token_expiry is not UNSET:
            field_dict["access_token_expiry"] = access_token_expiry

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_token = d.pop("access_token", UNSET)

        access_token_expiry = d.pop("access_token_expiry", UNSET)

        refresh_response = cls(
            access_token=access_token,
            access_token_expiry=access_token_expiry,
        )


        refresh_response.additional_properties = d
        return refresh_response

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
