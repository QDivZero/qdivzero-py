from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChatToolCallFunctionEnvelope")


@_attrs_define
class ChatToolCallFunctionEnvelope:
    """
    Attributes:
        arguments (str | Unset):
        name (str | Unset):
    """

    arguments: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        arguments = self.arguments

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if arguments is not UNSET:
            field_dict["arguments"] = arguments
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        arguments = d.pop("arguments", UNSET)

        name = d.pop("name", UNSET)

        chat_tool_call_function_envelope = cls(
            arguments=arguments,
            name=name,
        )

        chat_tool_call_function_envelope.additional_properties = d
        return chat_tool_call_function_envelope

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
