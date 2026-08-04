from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.index_document_request_metadata import IndexDocumentRequestMetadata
  from ..models.index_document_source_request import IndexDocumentSourceRequest





T = TypeVar("T", bound="IndexDocumentRequest")



@_attrs_define
class IndexDocumentRequest:
    """ 
        Attributes:
            content (str | Unset):
            content_image_url (str | Unset):
            id (str | Unset):
            metadata (IndexDocumentRequestMetadata | Unset):
            source (IndexDocumentSourceRequest | Unset):
     """

    content: str | Unset = UNSET
    content_image_url: str | Unset = UNSET
    id: str | Unset = UNSET
    metadata: IndexDocumentRequestMetadata | Unset = UNSET
    source: IndexDocumentSourceRequest | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        content = self.content

        content_image_url = self.content_image_url

        id = self.id

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if content is not UNSET:
            field_dict["content"] = content
        if content_image_url is not UNSET:
            field_dict["content_image_url"] = content_image_url
        if id is not UNSET:
            field_dict["id"] = id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.index_document_request_metadata import IndexDocumentRequestMetadata
        from ..models.index_document_source_request import IndexDocumentSourceRequest
        d = dict(src_dict)
        content = d.pop("content", UNSET)

        content_image_url = d.pop("content_image_url", UNSET)

        id = d.pop("id", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: IndexDocumentRequestMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = IndexDocumentRequestMetadata.from_dict(_metadata)




        _source = d.pop("source", UNSET)
        source: IndexDocumentSourceRequest | Unset
        if isinstance(_source,  Unset):
            source = UNSET
        else:
            source = IndexDocumentSourceRequest.from_dict(_source)




        index_document_request = cls(
            content=content,
            content_image_url=content_image_url,
            id=id,
            metadata=metadata,
            source=source,
        )


        index_document_request.additional_properties = d
        return index_document_request

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
