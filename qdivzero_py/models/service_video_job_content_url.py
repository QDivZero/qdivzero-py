from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceVideoJobContentURL")


@_attrs_define
class ServiceVideoJobContentURL:
    """
    Attributes:
        download_url (str | Unset):
        expires_at (str | Unset):
        url (str | Unset):
    """

    download_url: str | Unset = UNSET
    expires_at: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        download_url = self.download_url

        expires_at = self.expires_at

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if download_url is not UNSET:
            field_dict["download_url"] = download_url
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        download_url = d.pop("download_url", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        url = d.pop("url", UNSET)

        service_video_job_content_url = cls(
            download_url=download_url,
            expires_at=expires_at,
            url=url,
        )

        service_video_job_content_url.additional_properties = d
        return service_video_job_content_url

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
