from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FinishPasskeyloginRequest")


@_attrs_define
class FinishPasskeyloginRequest:
    """
    Attributes:
        challenge_id (str):
        credential (list[int]):
        email (str):
        cf_turnstile_response (str | Unset):
    """

    challenge_id: str
    credential: list[int]
    email: str
    cf_turnstile_response: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        challenge_id = self.challenge_id

        credential = self.credential

        email = self.email

        cf_turnstile_response = self.cf_turnstile_response

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "challenge_id": challenge_id,
                "credential": credential,
                "email": email,
            }
        )
        if cf_turnstile_response is not UNSET:
            field_dict["cf_turnstile_response"] = cf_turnstile_response

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        challenge_id = d.pop("challenge_id")

        credential = cast(list[int], d.pop("credential"))

        email = d.pop("email")

        cf_turnstile_response = d.pop("cf_turnstile_response", UNSET)

        finish_passkeylogin_request = cls(
            challenge_id=challenge_id,
            credential=credential,
            email=email,
            cf_turnstile_response=cf_turnstile_response,
        )

        finish_passkeylogin_request.additional_properties = d
        return finish_passkeylogin_request

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
