from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RecommendRequest")


@_attrs_define
class RecommendRequest:
    """
    Attributes:
        recommend_token (str | Unset):
        top_k (int | Unset):
    """

    recommend_token: str | Unset = UNSET
    top_k: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        recommend_token = self.recommend_token

        top_k = self.top_k

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if recommend_token is not UNSET:
            field_dict["recommend_token"] = recommend_token
        if top_k is not UNSET:
            field_dict["top_k"] = top_k

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        recommend_token = d.pop("recommend_token", UNSET)

        top_k = d.pop("top_k", UNSET)

        recommend_request = cls(
            recommend_token=recommend_token,
            top_k=top_k,
        )

        recommend_request.additional_properties = d
        return recommend_request

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
