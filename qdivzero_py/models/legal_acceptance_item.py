from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LegalAcceptanceItem")


@_attrs_define
class LegalAcceptanceItem:
    """
    Attributes:
        context (str):
        document_type (str):
        sha256 (str):
        version (str):
    """

    context: str
    document_type: str
    sha256: str
    version: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        context = self.context

        document_type = self.document_type

        sha256 = self.sha256

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "context": context,
                "document_type": document_type,
                "sha256": sha256,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        context = d.pop("context")

        document_type = d.pop("document_type")

        sha256 = d.pop("sha256")

        version = d.pop("version")

        legal_acceptance_item = cls(
            context=context,
            document_type=document_type,
            sha256=sha256,
            version=version,
        )

        legal_acceptance_item.additional_properties = d
        return legal_acceptance_item

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
