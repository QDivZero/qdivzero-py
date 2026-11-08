from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_link_response_route_args import NotificationLinkResponseRouteArgs


T = TypeVar("T", bound="NotificationLinkResponse")


@_attrs_define
class NotificationLinkResponse:
    """
    Attributes:
        kind_route (str | Unset):
        label_key (str | Unset):
        route_args (NotificationLinkResponseRouteArgs | Unset):
    """

    kind_route: str | Unset = UNSET
    label_key: str | Unset = UNSET
    route_args: NotificationLinkResponseRouteArgs | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind_route = self.kind_route

        label_key = self.label_key

        route_args: dict[str, Any] | Unset = UNSET
        if not isinstance(self.route_args, Unset):
            route_args = self.route_args.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind_route is not UNSET:
            field_dict["kind_route"] = kind_route
        if label_key is not UNSET:
            field_dict["label_key"] = label_key
        if route_args is not UNSET:
            field_dict["route_args"] = route_args

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_link_response_route_args import NotificationLinkResponseRouteArgs

        d = dict(src_dict)
        kind_route = d.pop("kind_route", UNSET)

        label_key = d.pop("label_key", UNSET)

        _route_args = d.pop("route_args", UNSET)
        route_args: NotificationLinkResponseRouteArgs | Unset
        if isinstance(_route_args, Unset):
            route_args = UNSET
        else:
            route_args = NotificationLinkResponseRouteArgs.from_dict(_route_args)

        notification_link_response = cls(
            kind_route=kind_route,
            label_key=label_key,
            route_args=route_args,
        )

        notification_link_response.additional_properties = d
        return notification_link_response

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
