from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServingTargetRequest")


@_attrs_define
class ServingTargetRequest:
    """
    Attributes:
        instance_id (str | Unset):
        target_ref_id (str | Unset):
        type_ (str | Unset):
    """

    instance_id: str | Unset = UNSET
    target_ref_id: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_id = self.instance_id

        target_ref_id = self.target_ref_id

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_id is not UNSET:
            field_dict["instance_id"] = instance_id
        if target_ref_id is not UNSET:
            field_dict["target_ref_id"] = target_ref_id
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        instance_id = d.pop("instance_id", UNSET)

        target_ref_id = d.pop("target_ref_id", UNSET)

        type_ = d.pop("type", UNSET)

        serving_target_request = cls(
            instance_id=instance_id,
            target_ref_id=target_ref_id,
            type_=type_,
        )

        serving_target_request.additional_properties = d
        return serving_target_request

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
