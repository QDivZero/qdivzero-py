from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_link_response import NotificationLinkResponse
    from ..models.notification_response_body_args import NotificationResponseBodyArgs
    from ..models.notification_response_metadata import NotificationResponseMetadata
    from ..models.notification_response_title_args import NotificationResponseTitleArgs


T = TypeVar("T", bound="NotificationResponse")


@_attrs_define
class NotificationResponse:
    """
    Attributes:
        body_args (NotificationResponseBodyArgs | Unset):
        body_key (str | Unset):
        created_at (str | Unset):
        dedupe_key (str | Unset):
        dismissed (bool | Unset):
        expires_at (str | Unset):
        icon (str | Unset):
        id (str | Unset):
        kind (str | Unset):
        links (list[NotificationLinkResponse] | Unset):
        metadata (NotificationResponseMetadata | Unset):
        read (bool | Unset):
        severity (str | Unset):
        source_topic (str | Unset):
        title_args (NotificationResponseTitleArgs | Unset):
        title_key (str | Unset):
    """

    body_args: NotificationResponseBodyArgs | Unset = UNSET
    body_key: str | Unset = UNSET
    created_at: str | Unset = UNSET
    dedupe_key: str | Unset = UNSET
    dismissed: bool | Unset = UNSET
    expires_at: str | Unset = UNSET
    icon: str | Unset = UNSET
    id: str | Unset = UNSET
    kind: str | Unset = UNSET
    links: list[NotificationLinkResponse] | Unset = UNSET
    metadata: NotificationResponseMetadata | Unset = UNSET
    read: bool | Unset = UNSET
    severity: str | Unset = UNSET
    source_topic: str | Unset = UNSET
    title_args: NotificationResponseTitleArgs | Unset = UNSET
    title_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body_args: dict[str, Any] | Unset = UNSET
        if not isinstance(self.body_args, Unset):
            body_args = self.body_args.to_dict()

        body_key = self.body_key

        created_at = self.created_at

        dedupe_key = self.dedupe_key

        dismissed = self.dismissed

        expires_at = self.expires_at

        icon = self.icon

        id = self.id

        kind = self.kind

        links: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        read = self.read

        severity = self.severity

        source_topic = self.source_topic

        title_args: dict[str, Any] | Unset = UNSET
        if not isinstance(self.title_args, Unset):
            title_args = self.title_args.to_dict()

        title_key = self.title_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if body_args is not UNSET:
            field_dict["body_args"] = body_args
        if body_key is not UNSET:
            field_dict["body_key"] = body_key
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if dedupe_key is not UNSET:
            field_dict["dedupe_key"] = dedupe_key
        if dismissed is not UNSET:
            field_dict["dismissed"] = dismissed
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if icon is not UNSET:
            field_dict["icon"] = icon
        if id is not UNSET:
            field_dict["id"] = id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if links is not UNSET:
            field_dict["links"] = links
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if read is not UNSET:
            field_dict["read"] = read
        if severity is not UNSET:
            field_dict["severity"] = severity
        if source_topic is not UNSET:
            field_dict["source_topic"] = source_topic
        if title_args is not UNSET:
            field_dict["title_args"] = title_args
        if title_key is not UNSET:
            field_dict["title_key"] = title_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_link_response import NotificationLinkResponse
        from ..models.notification_response_body_args import NotificationResponseBodyArgs
        from ..models.notification_response_metadata import NotificationResponseMetadata
        from ..models.notification_response_title_args import NotificationResponseTitleArgs

        d = dict(src_dict)
        _body_args = d.pop("body_args", UNSET)
        body_args: NotificationResponseBodyArgs | Unset
        if isinstance(_body_args, Unset):
            body_args = UNSET
        else:
            body_args = NotificationResponseBodyArgs.from_dict(_body_args)

        body_key = d.pop("body_key", UNSET)

        created_at = d.pop("created_at", UNSET)

        dedupe_key = d.pop("dedupe_key", UNSET)

        dismissed = d.pop("dismissed", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        icon = d.pop("icon", UNSET)

        id = d.pop("id", UNSET)

        kind = d.pop("kind", UNSET)

        _links = d.pop("links", UNSET)
        links: list[NotificationLinkResponse] | Unset = UNSET
        if _links is not UNSET:
            links = []
            for links_item_data in _links:
                links_item = NotificationLinkResponse.from_dict(links_item_data)

                links.append(links_item)

        _metadata = d.pop("metadata", UNSET)
        metadata: NotificationResponseMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = NotificationResponseMetadata.from_dict(_metadata)

        read = d.pop("read", UNSET)

        severity = d.pop("severity", UNSET)

        source_topic = d.pop("source_topic", UNSET)

        _title_args = d.pop("title_args", UNSET)
        title_args: NotificationResponseTitleArgs | Unset
        if isinstance(_title_args, Unset):
            title_args = UNSET
        else:
            title_args = NotificationResponseTitleArgs.from_dict(_title_args)

        title_key = d.pop("title_key", UNSET)

        notification_response = cls(
            body_args=body_args,
            body_key=body_key,
            created_at=created_at,
            dedupe_key=dedupe_key,
            dismissed=dismissed,
            expires_at=expires_at,
            icon=icon,
            id=id,
            kind=kind,
            links=links,
            metadata=metadata,
            read=read,
            severity=severity,
            source_topic=source_topic,
            title_args=title_args,
            title_key=title_key,
        )

        notification_response.additional_properties = d
        return notification_response

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
