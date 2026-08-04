from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchHitSourceResponse")



@_attrs_define
class SearchHitSourceResponse:
    """ 
        Attributes:
            image_url (str | Unset):
            text (str | Unset):
            truncate (bool | Unset):
     """

    image_url: str | Unset = UNSET
    text: str | Unset = UNSET
    truncate: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        image_url = self.image_url

        text = self.text

        truncate = self.truncate


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if text is not UNSET:
            field_dict["text"] = text
        if truncate is not UNSET:
            field_dict["truncate"] = truncate

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        image_url = d.pop("image_url", UNSET)

        text = d.pop("text", UNSET)

        truncate = d.pop("truncate", UNSET)

        search_hit_source_response = cls(
            image_url=image_url,
            text=text,
            truncate=truncate,
        )


        search_hit_source_response.additional_properties = d
        return search_hit_source_response

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
