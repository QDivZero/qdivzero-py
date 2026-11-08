from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RuntimeConfigRequestStorageMountsItem")


@_attrs_define
class RuntimeConfigRequestStorageMountsItem:
    """
    Attributes:
        mount_path (str | Unset):
        set_hf_home (bool | Unset):
        subpath (str | Unset):
        volume_id (str | Unset):
    """

    mount_path: str | Unset = UNSET
    set_hf_home: bool | Unset = UNSET
    subpath: str | Unset = UNSET
    volume_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mount_path = self.mount_path

        set_hf_home = self.set_hf_home

        subpath = self.subpath

        volume_id = self.volume_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mount_path is not UNSET:
            field_dict["mount_path"] = mount_path
        if set_hf_home is not UNSET:
            field_dict["set_hf_home"] = set_hf_home
        if subpath is not UNSET:
            field_dict["subpath"] = subpath
        if volume_id is not UNSET:
            field_dict["volume_id"] = volume_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mount_path = d.pop("mount_path", UNSET)

        set_hf_home = d.pop("set_hf_home", UNSET)

        subpath = d.pop("subpath", UNSET)

        volume_id = d.pop("volume_id", UNSET)

        runtime_config_request_storage_mounts_item = cls(
            mount_path=mount_path,
            set_hf_home=set_hf_home,
            subpath=subpath,
            volume_id=volume_id,
        )

        runtime_config_request_storage_mounts_item.additional_properties = d
        return runtime_config_request_storage_mounts_item

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
