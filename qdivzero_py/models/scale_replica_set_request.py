from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScaleReplicaSetRequest")


@_attrs_define
class ScaleReplicaSetRequest:
    """
    Attributes:
        desired_replicas (int | Unset):
    """

    desired_replicas: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        desired_replicas = self.desired_replicas

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if desired_replicas is not UNSET:
            field_dict["desired_replicas"] = desired_replicas

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        desired_replicas = d.pop("desired_replicas", UNSET)

        scale_replica_set_request = cls(
            desired_replicas=desired_replicas,
        )

        scale_replica_set_request.additional_properties = d
        return scale_replica_set_request

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
