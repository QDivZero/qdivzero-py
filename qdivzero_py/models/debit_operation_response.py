from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DebitOperationResponse")


@_attrs_define
class DebitOperationResponse:
    """
    Attributes:
        created_at (str | Unset):
        operation_id (str | Unset):
        outcome (str | Unset):
        reference (str | Unset):
        source (str | Unset):
        status (str | Unset):
        updated_at (str | Unset):
    """

    created_at: str | Unset = UNSET
    operation_id: str | Unset = UNSET
    outcome: str | Unset = UNSET
    reference: str | Unset = UNSET
    source: str | Unset = UNSET
    status: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        operation_id = self.operation_id

        outcome = self.outcome

        reference = self.reference

        source = self.source

        status = self.status

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if operation_id is not UNSET:
            field_dict["operation_id"] = operation_id
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
        if reference is not UNSET:
            field_dict["reference"] = reference
        if source is not UNSET:
            field_dict["source"] = source
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        operation_id = d.pop("operation_id", UNSET)

        outcome = d.pop("outcome", UNSET)

        reference = d.pop("reference", UNSET)

        source = d.pop("source", UNSET)

        status = d.pop("status", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        debit_operation_response = cls(
            created_at=created_at,
            operation_id=operation_id,
            outcome=outcome,
            reference=reference,
            source=source,
            status=status,
            updated_at=updated_at,
        )

        debit_operation_response.additional_properties = d
        return debit_operation_response

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
