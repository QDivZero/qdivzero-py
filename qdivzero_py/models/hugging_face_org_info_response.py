from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HuggingFaceOrgInfoResponse")


@_attrs_define
class HuggingFaceOrgInfoResponse:
    """
    Attributes:
        avatar_url (str | Unset):
        fullname (str | Unset):
    """

    avatar_url: str | Unset = UNSET
    fullname: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avatar_url = self.avatar_url

        fullname = self.fullname

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if fullname is not UNSET:
            field_dict["fullname"] = fullname

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avatar_url = d.pop("avatar_url", UNSET)

        fullname = d.pop("fullname", UNSET)

        hugging_face_org_info_response = cls(
            avatar_url=avatar_url,
            fullname=fullname,
        )

        hugging_face_org_info_response.additional_properties = d
        return hugging_face_org_info_response

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
