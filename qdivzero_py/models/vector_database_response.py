from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VectorDatabaseResponse")



@_attrs_define
class VectorDatabaseResponse:
    """ 
        Attributes:
            account_id (str | Unset):
            created_at (str | Unset):
            description (str | Unset):
            embedding_model_ref (str | Unset):
            embedding_serving_name (str | Unset):
            error_message (str | Unset):
            id (str | Unset):
            name (str | Unset):
            opensearch_index_name (str | Unset):
            slug (str | Unset):
            status (str | Unset):
            updated_at (str | Unset):
     """

    account_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    description: str | Unset = UNSET
    embedding_model_ref: str | Unset = UNSET
    embedding_serving_name: str | Unset = UNSET
    error_message: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    opensearch_index_name: str | Unset = UNSET
    slug: str | Unset = UNSET
    status: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        created_at = self.created_at

        description = self.description

        embedding_model_ref = self.embedding_model_ref

        embedding_serving_name = self.embedding_serving_name

        error_message = self.error_message

        id = self.id

        name = self.name

        opensearch_index_name = self.opensearch_index_name

        slug = self.slug

        status = self.status

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if embedding_model_ref is not UNSET:
            field_dict["embedding_model_ref"] = embedding_model_ref
        if embedding_serving_name is not UNSET:
            field_dict["embedding_serving_name"] = embedding_serving_name
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if opensearch_index_name is not UNSET:
            field_dict["opensearch_index_name"] = opensearch_index_name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        description = d.pop("description", UNSET)

        embedding_model_ref = d.pop("embedding_model_ref", UNSET)

        embedding_serving_name = d.pop("embedding_serving_name", UNSET)

        error_message = d.pop("error_message", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        opensearch_index_name = d.pop("opensearch_index_name", UNSET)

        slug = d.pop("slug", UNSET)

        status = d.pop("status", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        vector_database_response = cls(
            account_id=account_id,
            created_at=created_at,
            description=description,
            embedding_model_ref=embedding_model_ref,
            embedding_serving_name=embedding_serving_name,
            error_message=error_message,
            id=id,
            name=name,
            opensearch_index_name=opensearch_index_name,
            slug=slug,
            status=status,
            updated_at=updated_at,
        )


        vector_database_response.additional_properties = d
        return vector_database_response

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
