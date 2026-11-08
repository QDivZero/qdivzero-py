from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat_tool_call_envelope import ChatToolCallEnvelope


T = TypeVar("T", bound="ChatMessageEnvelope")


@_attrs_define
class ChatMessageEnvelope:
    """
    Attributes:
        content (list[int] | Unset):
        reasoning (str | Unset):
        reasoning_content (str | Unset):
        role (str | Unset):
        tool_call_id (str | Unset):
        tool_calls (list[ChatToolCallEnvelope] | Unset):
    """

    content: list[int] | Unset = UNSET
    reasoning: str | Unset = UNSET
    reasoning_content: str | Unset = UNSET
    role: str | Unset = UNSET
    tool_call_id: str | Unset = UNSET
    tool_calls: list[ChatToolCallEnvelope] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content: list[int] | Unset = UNSET
        if not isinstance(self.content, Unset):
            content = self.content

        reasoning = self.reasoning

        reasoning_content = self.reasoning_content

        role = self.role

        tool_call_id = self.tool_call_id

        tool_calls: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tool_calls, Unset):
            tool_calls = []
            for tool_calls_item_data in self.tool_calls:
                tool_calls_item = tool_calls_item_data.to_dict()
                tool_calls.append(tool_calls_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if reasoning is not UNSET:
            field_dict["reasoning"] = reasoning
        if reasoning_content is not UNSET:
            field_dict["reasoning_content"] = reasoning_content
        if role is not UNSET:
            field_dict["role"] = role
        if tool_call_id is not UNSET:
            field_dict["tool_call_id"] = tool_call_id
        if tool_calls is not UNSET:
            field_dict["tool_calls"] = tool_calls

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_tool_call_envelope import ChatToolCallEnvelope

        d = dict(src_dict)
        content = cast(list[int], d.pop("content", UNSET))

        reasoning = d.pop("reasoning", UNSET)

        reasoning_content = d.pop("reasoning_content", UNSET)

        role = d.pop("role", UNSET)

        tool_call_id = d.pop("tool_call_id", UNSET)

        _tool_calls = d.pop("tool_calls", UNSET)
        tool_calls: list[ChatToolCallEnvelope] | Unset = UNSET
        if _tool_calls is not UNSET:
            tool_calls = []
            for tool_calls_item_data in _tool_calls:
                tool_calls_item = ChatToolCallEnvelope.from_dict(tool_calls_item_data)

                tool_calls.append(tool_calls_item)

        chat_message_envelope = cls(
            content=content,
            reasoning=reasoning,
            reasoning_content=reasoning_content,
            role=role,
            tool_call_id=tool_call_id,
            tool_calls=tool_calls,
        )

        chat_message_envelope.additional_properties = d
        return chat_message_envelope

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
