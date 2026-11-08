from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LoginRequest")


@_attrs_define
class LoginRequest:
    """
    Attributes:
        email (str):
        password (str):
        cf_turnstile_response (str | Unset):
        totp_code (str | Unset):
    """

    email: str
    password: str
    cf_turnstile_response: str | Unset = UNSET
    totp_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        password = self.password

        cf_turnstile_response = self.cf_turnstile_response

        totp_code = self.totp_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "password": password,
            }
        )
        if cf_turnstile_response is not UNSET:
            field_dict["cf_turnstile_response"] = cf_turnstile_response
        if totp_code is not UNSET:
            field_dict["totp_code"] = totp_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        password = d.pop("password")

        cf_turnstile_response = d.pop("cf_turnstile_response", UNSET)

        totp_code = d.pop("totp_code", UNSET)

        login_request = cls(
            email=email,
            password=password,
            cf_turnstile_response=cf_turnstile_response,
            totp_code=totp_code,
        )

        login_request.additional_properties = d
        return login_request

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
