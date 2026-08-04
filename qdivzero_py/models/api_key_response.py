from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiKeyResponse")



@_attrs_define
class ApiKeyResponse:
    """ 
        Attributes:
            created_at (str | Unset):
            id (str | Unset):
            key_prefix (str | Unset):
            plaintext_key (str | Unset):
            revoked_at (str | Unset):
     """

    created_at: str | Unset = UNSET
    id: str | Unset = UNSET
    key_prefix: str | Unset = UNSET
    plaintext_key: str | Unset = UNSET
    revoked_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        id = self.id

        key_prefix = self.key_prefix

        plaintext_key = self.plaintext_key

        revoked_at = self.revoked_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if key_prefix is not UNSET:
            field_dict["key_prefix"] = key_prefix
        if plaintext_key is not UNSET:
            field_dict["plaintext_key"] = plaintext_key
        if revoked_at is not UNSET:
            field_dict["revoked_at"] = revoked_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        id = d.pop("id", UNSET)

        key_prefix = d.pop("key_prefix", UNSET)

        plaintext_key = d.pop("plaintext_key", UNSET)

        revoked_at = d.pop("revoked_at", UNSET)

        api_key_response = cls(
            created_at=created_at,
            id=id,
            key_prefix=key_prefix,
            plaintext_key=plaintext_key,
            revoked_at=revoked_at,
        )


        api_key_response.additional_properties = d
        return api_key_response

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
