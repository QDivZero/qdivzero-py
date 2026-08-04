from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.smart_balancer_route_destination_response import SmartBalancerRouteDestinationResponse





T = TypeVar("T", bound="SmartBalancerRouteResponse")



@_attrs_define
class SmartBalancerRouteResponse:
    """ 
        Attributes:
            created_at (str | Unset):
            destination (SmartBalancerRouteDestinationResponse | Unset):
            enabled (bool | Unset):
            id (str | Unset):
            intent (str | Unset):
            is_default (bool | Unset):
            name (str | Unset):
            priority (int | Unset):
            updated_at (str | Unset):
     """

    created_at: str | Unset = UNSET
    destination: SmartBalancerRouteDestinationResponse | Unset = UNSET
    enabled: bool | Unset = UNSET
    id: str | Unset = UNSET
    intent: str | Unset = UNSET
    is_default: bool | Unset = UNSET
    name: str | Unset = UNSET
    priority: int | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        destination: dict[str, Any] | Unset = UNSET
        if not isinstance(self.destination, Unset):
            destination = self.destination.to_dict()

        enabled = self.enabled

        id = self.id

        intent = self.intent

        is_default = self.is_default

        name = self.name

        priority = self.priority

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if destination is not UNSET:
            field_dict["destination"] = destination
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if id is not UNSET:
            field_dict["id"] = id
        if intent is not UNSET:
            field_dict["intent"] = intent
        if is_default is not UNSET:
            field_dict["is_default"] = is_default
        if name is not UNSET:
            field_dict["name"] = name
        if priority is not UNSET:
            field_dict["priority"] = priority
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.smart_balancer_route_destination_response import SmartBalancerRouteDestinationResponse
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        _destination = d.pop("destination", UNSET)
        destination: SmartBalancerRouteDestinationResponse | Unset
        if isinstance(_destination,  Unset):
            destination = UNSET
        else:
            destination = SmartBalancerRouteDestinationResponse.from_dict(_destination)




        enabled = d.pop("enabled", UNSET)

        id = d.pop("id", UNSET)

        intent = d.pop("intent", UNSET)

        is_default = d.pop("is_default", UNSET)

        name = d.pop("name", UNSET)

        priority = d.pop("priority", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        smart_balancer_route_response = cls(
            created_at=created_at,
            destination=destination,
            enabled=enabled,
            id=id,
            intent=intent,
            is_default=is_default,
            name=name,
            priority=priority,
            updated_at=updated_at,
        )


        smart_balancer_route_response.additional_properties = d
        return smart_balancer_route_response

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
