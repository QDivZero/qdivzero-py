from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PasskeyResponse")



@_attrs_define
class PasskeyResponse:
    """ 
        Attributes:
            credential_id (str | Unset):
            public_key (str | Unset):
            sign_count (int | Unset):
     """

    credential_id: str | Unset = UNSET
    public_key: str | Unset = UNSET
    sign_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        credential_id = self.credential_id

        public_key = self.public_key

        sign_count = self.sign_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if credential_id is not UNSET:
            field_dict["credential_id"] = credential_id
        if public_key is not UNSET:
            field_dict["public_key"] = public_key
        if sign_count is not UNSET:
            field_dict["sign_count"] = sign_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        credential_id = d.pop("credential_id", UNSET)

        public_key = d.pop("public_key", UNSET)

        sign_count = d.pop("sign_count", UNSET)

        passkey_response = cls(
            credential_id=credential_id,
            public_key=public_key,
            sign_count=sign_count,
        )


        passkey_response.additional_properties = d
        return passkey_response

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
