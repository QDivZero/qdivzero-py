from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.shared_capacity_response import SharedCapacityResponse


T = TypeVar("T", bound="SharedCapacityListResponse")


@_attrs_define
class SharedCapacityListResponse:
    """
    Attributes:
        capacities (list[SharedCapacityResponse] | Unset):
    """

    capacities: list[SharedCapacityResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        capacities: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.capacities, Unset):
            capacities = []
            for capacities_item_data in self.capacities:
                capacities_item = capacities_item_data.to_dict()
                capacities.append(capacities_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if capacities is not UNSET:
            field_dict["capacities"] = capacities

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.shared_capacity_response import SharedCapacityResponse

        d = dict(src_dict)
        _capacities = d.pop("capacities", UNSET)
        capacities: list[SharedCapacityResponse] | Unset = UNSET
        if _capacities is not UNSET:
            capacities = []
            for capacities_item_data in _capacities:
                capacities_item = SharedCapacityResponse.from_dict(capacities_item_data)

                capacities.append(capacities_item)

        shared_capacity_list_response = cls(
            capacities=capacities,
        )

        shared_capacity_list_response.additional_properties = d
        return shared_capacity_list_response

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
