from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.smart_balancer_route_destination_request import SmartBalancerRouteDestinationRequest


T = TypeVar("T", bound="SmartBalancerRouteRequest")


@_attrs_define
class SmartBalancerRouteRequest:
    """
    Attributes:
        destination (SmartBalancerRouteDestinationRequest | Unset):
        enabled (bool | Unset):
        intent (str | Unset):
        is_default (bool | Unset):
        name (str | Unset):
        priority (int | Unset):
    """

    destination: SmartBalancerRouteDestinationRequest | Unset = UNSET
    enabled: bool | Unset = UNSET
    intent: str | Unset = UNSET
    is_default: bool | Unset = UNSET
    name: str | Unset = UNSET
    priority: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        destination: dict[str, Any] | Unset = UNSET
        if not isinstance(self.destination, Unset):
            destination = self.destination.to_dict()

        enabled = self.enabled

        intent = self.intent

        is_default = self.is_default

        name = self.name

        priority = self.priority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if destination is not UNSET:
            field_dict["destination"] = destination
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if intent is not UNSET:
            field_dict["intent"] = intent
        if is_default is not UNSET:
            field_dict["is_default"] = is_default
        if name is not UNSET:
            field_dict["name"] = name
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.smart_balancer_route_destination_request import SmartBalancerRouteDestinationRequest

        d = dict(src_dict)
        _destination = d.pop("destination", UNSET)
        destination: SmartBalancerRouteDestinationRequest | Unset
        if isinstance(_destination, Unset):
            destination = UNSET
        else:
            destination = SmartBalancerRouteDestinationRequest.from_dict(_destination)

        enabled = d.pop("enabled", UNSET)

        intent = d.pop("intent", UNSET)

        is_default = d.pop("is_default", UNSET)

        name = d.pop("name", UNSET)

        priority = d.pop("priority", UNSET)

        smart_balancer_route_request = cls(
            destination=destination,
            enabled=enabled,
            intent=intent,
            is_default=is_default,
            name=name,
            priority=priority,
        )

        smart_balancer_route_request.additional_properties = d
        return smart_balancer_route_request

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
