from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OauthSignupRequest")


@_attrs_define
class OauthSignupRequest:
    """
    Attributes:
        continuation_token (str):
        privacy_acknowledged (bool):
        privacy_sha256 (str):
        privacy_version (str):
        terms_accepted (bool):
        terms_sha256 (str):
        terms_version (str):
        cf_turnstile_response (str | Unset):
    """

    continuation_token: str
    privacy_acknowledged: bool
    privacy_sha256: str
    privacy_version: str
    terms_accepted: bool
    terms_sha256: str
    terms_version: str
    cf_turnstile_response: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        continuation_token = self.continuation_token

        privacy_acknowledged = self.privacy_acknowledged

        privacy_sha256 = self.privacy_sha256

        privacy_version = self.privacy_version

        terms_accepted = self.terms_accepted

        terms_sha256 = self.terms_sha256

        terms_version = self.terms_version

        cf_turnstile_response = self.cf_turnstile_response

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "continuation_token": continuation_token,
                "privacy_acknowledged": privacy_acknowledged,
                "privacy_sha256": privacy_sha256,
                "privacy_version": privacy_version,
                "terms_accepted": terms_accepted,
                "terms_sha256": terms_sha256,
                "terms_version": terms_version,
            }
        )
        if cf_turnstile_response is not UNSET:
            field_dict["cf_turnstile_response"] = cf_turnstile_response

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        continuation_token = d.pop("continuation_token")

        privacy_acknowledged = d.pop("privacy_acknowledged")

        privacy_sha256 = d.pop("privacy_sha256")

        privacy_version = d.pop("privacy_version")

        terms_accepted = d.pop("terms_accepted")

        terms_sha256 = d.pop("terms_sha256")

        terms_version = d.pop("terms_version")

        cf_turnstile_response = d.pop("cf_turnstile_response", UNSET)

        oauth_signup_request = cls(
            continuation_token=continuation_token,
            privacy_acknowledged=privacy_acknowledged,
            privacy_sha256=privacy_sha256,
            privacy_version=privacy_version,
            terms_accepted=terms_accepted,
            terms_sha256=terms_sha256,
            terms_version=terms_version,
            cf_turnstile_response=cf_turnstile_response,
        )

        oauth_signup_request.additional_properties = d
        return oauth_signup_request

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
