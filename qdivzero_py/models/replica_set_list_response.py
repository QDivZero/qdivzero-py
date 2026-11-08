from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.replica_set_response import ReplicaSetResponse


T = TypeVar("T", bound="ReplicaSetListResponse")


@_attrs_define
class ReplicaSetListResponse:
    """
    Attributes:
        replica_sets (list[ReplicaSetResponse] | Unset):
    """

    replica_sets: list[ReplicaSetResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        replica_sets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.replica_sets, Unset):
            replica_sets = []
            for replica_sets_item_data in self.replica_sets:
                replica_sets_item = replica_sets_item_data.to_dict()
                replica_sets.append(replica_sets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if replica_sets is not UNSET:
            field_dict["replica_sets"] = replica_sets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.replica_set_response import ReplicaSetResponse

        d = dict(src_dict)
        _replica_sets = d.pop("replica_sets", UNSET)
        replica_sets: list[ReplicaSetResponse] | Unset = UNSET
        if _replica_sets is not UNSET:
            replica_sets = []
            for replica_sets_item_data in _replica_sets:
                replica_sets_item = ReplicaSetResponse.from_dict(replica_sets_item_data)

                replica_sets.append(replica_sets_item)

        replica_set_list_response = cls(
            replica_sets=replica_sets,
        )

        replica_set_list_response.additional_properties = d
        return replica_set_list_response

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
