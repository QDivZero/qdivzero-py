from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ViewElementRequest")


@_attrs_define
class ViewElementRequest:
    """
    Attributes:
        document_id (str | Unset):
        recommend_token (str | Unset):
        weight (float | Unset):
    """

    document_id: str | Unset = UNSET
    recommend_token: str | Unset = UNSET
    weight: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        document_id = self.document_id

        recommend_token = self.recommend_token

        weight = self.weight

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if document_id is not UNSET:
            field_dict["document_id"] = document_id
        if recommend_token is not UNSET:
            field_dict["recommend_token"] = recommend_token
        if weight is not UNSET:
            field_dict["weight"] = weight

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        document_id = d.pop("document_id", UNSET)

        recommend_token = d.pop("recommend_token", UNSET)

        weight = d.pop("weight", UNSET)

        view_element_request = cls(
            document_id=document_id,
            recommend_token=recommend_token,
            weight=weight,
        )

        view_element_request.additional_properties = d
        return view_element_request

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
