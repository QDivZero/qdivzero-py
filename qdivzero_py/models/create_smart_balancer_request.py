from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.smart_balancer_route_request import SmartBalancerRouteRequest
  from ..models.smart_balancer_router_model_request import SmartBalancerRouterModelRequest





T = TypeVar("T", bound="CreateSmartBalancerRequest")



@_attrs_define
class CreateSmartBalancerRequest:
    """ 
        Attributes:
            display_name (str | Unset):
            enabled (bool | Unset):
            name (str | Unset):
            router_model (SmartBalancerRouterModelRequest | Unset):
            routes (list[SmartBalancerRouteRequest] | Unset):
            routing_mode (str | Unset):
            workload_kind (str | Unset):
     """

    display_name: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    name: str | Unset = UNSET
    router_model: SmartBalancerRouterModelRequest | Unset = UNSET
    routes: list[SmartBalancerRouteRequest] | Unset = UNSET
    routing_mode: str | Unset = UNSET
    workload_kind: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        enabled = self.enabled

        name = self.name

        router_model: dict[str, Any] | Unset = UNSET
        if not isinstance(self.router_model, Unset):
            router_model = self.router_model.to_dict()

        routes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.routes, Unset):
            routes = []
            for routes_item_data in self.routes:
                routes_item = routes_item_data.to_dict()
                routes.append(routes_item)



        routing_mode = self.routing_mode

        workload_kind = self.workload_kind


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if name is not UNSET:
            field_dict["name"] = name
        if router_model is not UNSET:
            field_dict["router_model"] = router_model
        if routes is not UNSET:
            field_dict["routes"] = routes
        if routing_mode is not UNSET:
            field_dict["routing_mode"] = routing_mode
        if workload_kind is not UNSET:
            field_dict["workload_kind"] = workload_kind

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.smart_balancer_route_request import SmartBalancerRouteRequest
        from ..models.smart_balancer_router_model_request import SmartBalancerRouterModelRequest
        d = dict(src_dict)
        display_name = d.pop("display_name", UNSET)

        enabled = d.pop("enabled", UNSET)

        name = d.pop("name", UNSET)

        _router_model = d.pop("router_model", UNSET)
        router_model: SmartBalancerRouterModelRequest | Unset
        if isinstance(_router_model,  Unset):
            router_model = UNSET
        else:
            router_model = SmartBalancerRouterModelRequest.from_dict(_router_model)




        _routes = d.pop("routes", UNSET)
        routes: list[SmartBalancerRouteRequest] | Unset = UNSET
        if _routes is not UNSET:
            routes = []
            for routes_item_data in _routes:
                routes_item = SmartBalancerRouteRequest.from_dict(routes_item_data)



                routes.append(routes_item)


        routing_mode = d.pop("routing_mode", UNSET)

        workload_kind = d.pop("workload_kind", UNSET)

        create_smart_balancer_request = cls(
            display_name=display_name,
            enabled=enabled,
            name=name,
            router_model=router_model,
            routes=routes,
            routing_mode=routing_mode,
            workload_kind=workload_kind,
        )


        create_smart_balancer_request.additional_properties = d
        return create_smart_balancer_request

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
