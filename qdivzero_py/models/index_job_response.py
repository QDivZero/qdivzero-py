from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IndexJobResponse")


@_attrs_define
class IndexJobResponse:
    """
    Attributes:
        account_id (str | Unset):
        completed_at (str | Unset):
        created_at (str | Unset):
        database_id (str | Unset):
        error_message (str | Unset):
        id (str | Unset):
        kind (str | Unset):
        status (str | Unset):
        updated_at (str | Unset):
    """

    account_id: str | Unset = UNSET
    completed_at: str | Unset = UNSET
    created_at: str | Unset = UNSET
    database_id: str | Unset = UNSET
    error_message: str | Unset = UNSET
    id: str | Unset = UNSET
    kind: str | Unset = UNSET
    status: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        completed_at = self.completed_at

        created_at = self.created_at

        database_id = self.database_id

        error_message = self.error_message

        id = self.id

        kind = self.kind

        status = self.status

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if database_id is not UNSET:
            field_dict["database_id"] = database_id
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if id is not UNSET:
            field_dict["id"] = id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        completed_at = d.pop("completed_at", UNSET)

        created_at = d.pop("created_at", UNSET)

        database_id = d.pop("database_id", UNSET)

        error_message = d.pop("error_message", UNSET)

        id = d.pop("id", UNSET)

        kind = d.pop("kind", UNSET)

        status = d.pop("status", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        index_job_response = cls(
            account_id=account_id,
            completed_at=completed_at,
            created_at=created_at,
            database_id=database_id,
            error_message=error_message,
            id=id,
            kind=kind,
            status=status,
            updated_at=updated_at,
        )

        index_job_response.additional_properties = d
        return index_job_response

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
