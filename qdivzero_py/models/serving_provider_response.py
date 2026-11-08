from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServingProviderResponse")


@_attrs_define
class ServingProviderResponse:
    """
    Attributes:
        model_id (str | Unset):
        name (str | Unset):
        region (str | Unset):
        supported_protocols (list[str] | Unset):
        supports_tools (bool | Unset):
    """

    model_id: str | Unset = UNSET
    name: str | Unset = UNSET
    region: str | Unset = UNSET
    supported_protocols: list[str] | Unset = UNSET
    supports_tools: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_id = self.model_id

        name = self.name

        region = self.region

        supported_protocols: list[str] | Unset = UNSET
        if not isinstance(self.supported_protocols, Unset):
            supported_protocols = self.supported_protocols

        supports_tools = self.supports_tools

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if model_id is not UNSET:
            field_dict["model_id"] = model_id
        if name is not UNSET:
            field_dict["name"] = name
        if region is not UNSET:
            field_dict["region"] = region
        if supported_protocols is not UNSET:
            field_dict["supported_protocols"] = supported_protocols
        if supports_tools is not UNSET:
            field_dict["supports_tools"] = supports_tools

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model_id = d.pop("model_id", UNSET)

        name = d.pop("name", UNSET)

        region = d.pop("region", UNSET)

        supported_protocols = cast(list[str], d.pop("supported_protocols", UNSET))

        supports_tools = d.pop("supports_tools", UNSET)

        serving_provider_response = cls(
            model_id=model_id,
            name=name,
            region=region,
            supported_protocols=supported_protocols,
            supports_tools=supports_tools,
        )

        serving_provider_response.additional_properties = d
        return serving_provider_response

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
