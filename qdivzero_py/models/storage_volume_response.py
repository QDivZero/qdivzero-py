from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StorageVolumeResponse")



@_attrs_define
class StorageVolumeResponse:
    """ 
        Attributes:
            account_id (str | Unset):
            bucket (str | Unset):
            created_at (str | Unset):
            description (str | Unset):
            error_message (str | Unset):
            id (str | Unset):
            name (str | Unset):
            prefix (str | Unset):
            provider (str | Unset):
            status (str | Unset):
            updated_at (str | Unset):
     """

    account_id: str | Unset = UNSET
    bucket: str | Unset = UNSET
    created_at: str | Unset = UNSET
    description: str | Unset = UNSET
    error_message: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    prefix: str | Unset = UNSET
    provider: str | Unset = UNSET
    status: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        bucket = self.bucket

        created_at = self.created_at

        description = self.description

        error_message = self.error_message

        id = self.id

        name = self.name

        prefix = self.prefix

        provider = self.provider

        status = self.status

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if bucket is not UNSET:
            field_dict["bucket"] = bucket
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if provider is not UNSET:
            field_dict["provider"] = provider
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        bucket = d.pop("bucket", UNSET)

        created_at = d.pop("created_at", UNSET)

        description = d.pop("description", UNSET)

        error_message = d.pop("error_message", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        prefix = d.pop("prefix", UNSET)

        provider = d.pop("provider", UNSET)

        status = d.pop("status", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        storage_volume_response = cls(
            account_id=account_id,
            bucket=bucket,
            created_at=created_at,
            description=description,
            error_message=error_message,
            id=id,
            name=name,
            prefix=prefix,
            provider=provider,
            status=status,
            updated_at=updated_at,
        )


        storage_volume_response.additional_properties = d
        return storage_volume_response

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
