from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.legal_acceptance_item import LegalAcceptanceItem


T = TypeVar("T", bound="LegalAcceptanceRequest")


@_attrs_define
class LegalAcceptanceRequest:
    """
    Attributes:
        acceptances (list[LegalAcceptanceItem]):
    """

    acceptances: list[LegalAcceptanceItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        acceptances = []
        for acceptances_item_data in self.acceptances:
            acceptances_item = acceptances_item_data.to_dict()
            acceptances.append(acceptances_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "acceptances": acceptances,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.legal_acceptance_item import LegalAcceptanceItem

        d = dict(src_dict)
        acceptances = []
        _acceptances = d.pop("acceptances")
        for acceptances_item_data in _acceptances:
            acceptances_item = LegalAcceptanceItem.from_dict(acceptances_item_data)

            acceptances.append(acceptances_item)

        legal_acceptance_request = cls(
            acceptances=acceptances,
        )

        legal_acceptance_request.additional_properties = d
        return legal_acceptance_request

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
