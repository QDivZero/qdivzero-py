from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.search_hit_response_metadata import SearchHitResponseMetadata
  from ..models.search_hit_source_response import SearchHitSourceResponse





T = TypeVar("T", bound="SearchHitResponse")



@_attrs_define
class SearchHitResponse:
    """ 
        Attributes:
            content (str | Unset):
            id (str | Unset):
            metadata (SearchHitResponseMetadata | Unset):
            score (float | Unset):
            source (SearchHitSourceResponse | Unset):
     """

    content: str | Unset = UNSET
    id: str | Unset = UNSET
    metadata: SearchHitResponseMetadata | Unset = UNSET
    score: float | Unset = UNSET
    source: SearchHitSourceResponse | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        content = self.content

        id = self.id

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        score = self.score

        source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if content is not UNSET:
            field_dict["content"] = content
        if id is not UNSET:
            field_dict["id"] = id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if score is not UNSET:
            field_dict["score"] = score
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_hit_response_metadata import SearchHitResponseMetadata
        from ..models.search_hit_source_response import SearchHitSourceResponse
        d = dict(src_dict)
        content = d.pop("content", UNSET)

        id = d.pop("id", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: SearchHitResponseMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = SearchHitResponseMetadata.from_dict(_metadata)




        score = d.pop("score", UNSET)

        _source = d.pop("source", UNSET)
        source: SearchHitSourceResponse | Unset
        if isinstance(_source,  Unset):
            source = UNSET
        else:
            source = SearchHitSourceResponse.from_dict(_source)




        search_hit_response = cls(
            content=content,
            id=id,
            metadata=metadata,
            score=score,
            source=source,
        )


        search_hit_response.additional_properties = d
        return search_hit_response

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
