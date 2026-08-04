from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.serving_target_request import ServingTargetRequest





T = TypeVar("T", bound="CreateServingEndpointRequest")



@_attrs_define
class CreateServingEndpointRequest:
    """ 
        Attributes:
            display_name (str | Unset):
            name (str | Unset):
            target (ServingTargetRequest | Unset):
            workload_kind (str | Unset):
     """

    display_name: str | Unset = UNSET
    name: str | Unset = UNSET
    target: ServingTargetRequest | Unset = UNSET
    workload_kind: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        name = self.name

        target: dict[str, Any] | Unset = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.to_dict()

        workload_kind = self.workload_kind


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if name is not UNSET:
            field_dict["name"] = name
        if target is not UNSET:
            field_dict["target"] = target
        if workload_kind is not UNSET:
            field_dict["workload_kind"] = workload_kind

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.serving_target_request import ServingTargetRequest
        d = dict(src_dict)
        display_name = d.pop("display_name", UNSET)

        name = d.pop("name", UNSET)

        _target = d.pop("target", UNSET)
        target: ServingTargetRequest | Unset
        if isinstance(_target,  Unset):
            target = UNSET
        else:
            target = ServingTargetRequest.from_dict(_target)




        workload_kind = d.pop("workload_kind", UNSET)

        create_serving_endpoint_request = cls(
            display_name=display_name,
            name=name,
            target=target,
            workload_kind=workload_kind,
        )


        create_serving_endpoint_request.additional_properties = d
        return create_serving_endpoint_request

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
