from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_recommend_request import SearchRecommendRequest


T = TypeVar("T", bound="SearchRequest")


@_attrs_define
class SearchRequest:
    """
    Attributes:
        image_url (str | Unset):
        query (str | Unset):
        recommend (SearchRecommendRequest | Unset):
        top_k (int | Unset):
    """

    image_url: str | Unset = UNSET
    query: str | Unset = UNSET
    recommend: SearchRecommendRequest | Unset = UNSET
    top_k: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image_url = self.image_url

        query = self.query

        recommend: dict[str, Any] | Unset = UNSET
        if not isinstance(self.recommend, Unset):
            recommend = self.recommend.to_dict()

        top_k = self.top_k

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if query is not UNSET:
            field_dict["query"] = query
        if recommend is not UNSET:
            field_dict["recommend"] = recommend
        if top_k is not UNSET:
            field_dict["top_k"] = top_k

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_recommend_request import SearchRecommendRequest

        d = dict(src_dict)
        image_url = d.pop("image_url", UNSET)

        query = d.pop("query", UNSET)

        _recommend = d.pop("recommend", UNSET)
        recommend: SearchRecommendRequest | Unset
        if isinstance(_recommend, Unset):
            recommend = UNSET
        else:
            recommend = SearchRecommendRequest.from_dict(_recommend)

        top_k = d.pop("top_k", UNSET)

        search_request = cls(
            image_url=image_url,
            query=query,
            recommend=recommend,
            top_k=top_k,
        )

        search_request.additional_properties = d
        return search_request

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
