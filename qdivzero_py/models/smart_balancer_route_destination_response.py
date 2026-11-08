from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SmartBalancerRouteDestinationResponse")


@_attrs_define
class SmartBalancerRouteDestinationResponse:
    """
    Attributes:
        label (str | Unset):
        ref (str | Unset):
        type_ (str | Unset):
    """

    label: str | Unset = UNSET
    ref: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        ref = self.ref

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label is not UNSET:
            field_dict["label"] = label
        if ref is not UNSET:
            field_dict["ref"] = ref
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        label = d.pop("label", UNSET)

        ref = d.pop("ref", UNSET)

        type_ = d.pop("type", UNSET)

        smart_balancer_route_destination_response = cls(
            label=label,
            ref=ref,
            type_=type_,
        )

        smart_balancer_route_destination_response.additional_properties = d
        return smart_balancer_route_destination_response

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
