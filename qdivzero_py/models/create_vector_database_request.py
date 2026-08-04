from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateVectorDatabaseRequest")



@_attrs_define
class CreateVectorDatabaseRequest:
    """ 
        Attributes:
            description (str | Unset):
            embedding_serving_name (str | Unset):
            name (str | Unset):
            slug (str | Unset):
     """

    description: str | Unset = UNSET
    embedding_serving_name: str | Unset = UNSET
    name: str | Unset = UNSET
    slug: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        description = self.description

        embedding_serving_name = self.embedding_serving_name

        name = self.name

        slug = self.slug


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if embedding_serving_name is not UNSET:
            field_dict["embedding_serving_name"] = embedding_serving_name
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        embedding_serving_name = d.pop("embedding_serving_name", UNSET)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        create_vector_database_request = cls(
            description=description,
            embedding_serving_name=embedding_serving_name,
            name=name,
            slug=slug,
        )


        create_vector_database_request.additional_properties = d
        return create_vector_database_request

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
