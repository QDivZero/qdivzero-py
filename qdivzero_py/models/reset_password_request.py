from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResetPasswordRequest")



@_attrs_define
class ResetPasswordRequest:
    """ 
        Attributes:
            new_password (str):
            token (str):
            cf_turnstile_response (str | Unset):
     """

    new_password: str
    token: str
    cf_turnstile_response: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        new_password = self.new_password

        token = self.token

        cf_turnstile_response = self.cf_turnstile_response


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "new_password": new_password,
            "token": token,
        })
        if cf_turnstile_response is not UNSET:
            field_dict["cf_turnstile_response"] = cf_turnstile_response

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        new_password = d.pop("new_password")

        token = d.pop("token")

        cf_turnstile_response = d.pop("cf_turnstile_response", UNSET)

        reset_password_request = cls(
            new_password=new_password,
            token=token,
            cf_turnstile_response=cf_turnstile_response,
        )


        reset_password_request.additional_properties = d
        return reset_password_request

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
