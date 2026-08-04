from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BeginPasskeyRegistrationResponse")



@_attrs_define
class BeginPasskeyRegistrationResponse:
    """ 
        Attributes:
            challenge_id (str | Unset):
            public_key (list[int] | Unset):
     """

    challenge_id: str | Unset = UNSET
    public_key: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        challenge_id = self.challenge_id

        public_key: list[int] | Unset = UNSET
        if not isinstance(self.public_key, Unset):
            public_key = self.public_key




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if challenge_id is not UNSET:
            field_dict["challenge_id"] = challenge_id
        if public_key is not UNSET:
            field_dict["public_key"] = public_key

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        challenge_id = d.pop("challenge_id", UNSET)

        public_key = cast(list[int], d.pop("public_key", UNSET))


        begin_passkey_registration_response = cls(
            challenge_id=challenge_id,
            public_key=public_key,
        )


        begin_passkey_registration_response.additional_properties = d
        return begin_passkey_registration_response

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
