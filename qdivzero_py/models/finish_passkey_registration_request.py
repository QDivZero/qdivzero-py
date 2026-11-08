from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FinishPasskeyRegistrationRequest")


@_attrs_define
class FinishPasskeyRegistrationRequest:
    """
    Attributes:
        challenge_id (str):
        credential (list[int]):
    """

    challenge_id: str
    credential: list[int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        challenge_id = self.challenge_id

        credential = self.credential

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "challenge_id": challenge_id,
                "credential": credential,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        challenge_id = d.pop("challenge_id")

        credential = cast(list[int], d.pop("credential"))

        finish_passkey_registration_request = cls(
            challenge_id=challenge_id,
            credential=credential,
        )

        finish_passkey_registration_request.additional_properties = d
        return finish_passkey_registration_request

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
