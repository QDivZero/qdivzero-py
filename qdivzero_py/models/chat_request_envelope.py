from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat_message_envelope import ChatMessageEnvelope


T = TypeVar("T", bound="ChatRequestEnvelope")


@_attrs_define
class ChatRequestEnvelope:
    """
    Attributes:
        firewall (str | Unset):
        max_tokens (int | Unset):
        messages (list[ChatMessageEnvelope] | Unset):
        modalities (list[str] | Unset):
        model (str | Unset):
        speaker (str | Unset):
        stream (bool | Unset):
        temperature (float | Unset):
        top_p (float | Unset):
    """

    firewall: str | Unset = UNSET
    max_tokens: int | Unset = UNSET
    messages: list[ChatMessageEnvelope] | Unset = UNSET
    modalities: list[str] | Unset = UNSET
    model: str | Unset = UNSET
    speaker: str | Unset = UNSET
    stream: bool | Unset = UNSET
    temperature: float | Unset = UNSET
    top_p: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        firewall = self.firewall

        max_tokens = self.max_tokens

        messages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.messages, Unset):
            messages = []
            for messages_item_data in self.messages:
                messages_item = messages_item_data.to_dict()
                messages.append(messages_item)

        modalities: list[str] | Unset = UNSET
        if not isinstance(self.modalities, Unset):
            modalities = self.modalities

        model = self.model

        speaker = self.speaker

        stream = self.stream

        temperature = self.temperature

        top_p = self.top_p

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if firewall is not UNSET:
            field_dict["firewall"] = firewall
        if max_tokens is not UNSET:
            field_dict["max_tokens"] = max_tokens
        if messages is not UNSET:
            field_dict["messages"] = messages
        if modalities is not UNSET:
            field_dict["modalities"] = modalities
        if model is not UNSET:
            field_dict["model"] = model
        if speaker is not UNSET:
            field_dict["speaker"] = speaker
        if stream is not UNSET:
            field_dict["stream"] = stream
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if top_p is not UNSET:
            field_dict["top_p"] = top_p

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_message_envelope import ChatMessageEnvelope

        d = dict(src_dict)
        firewall = d.pop("firewall", UNSET)

        max_tokens = d.pop("max_tokens", UNSET)

        _messages = d.pop("messages", UNSET)
        messages: list[ChatMessageEnvelope] | Unset = UNSET
        if _messages is not UNSET:
            messages = []
            for messages_item_data in _messages:
                messages_item = ChatMessageEnvelope.from_dict(messages_item_data)

                messages.append(messages_item)

        modalities = cast(list[str], d.pop("modalities", UNSET))

        model = d.pop("model", UNSET)

        speaker = d.pop("speaker", UNSET)

        stream = d.pop("stream", UNSET)

        temperature = d.pop("temperature", UNSET)

        top_p = d.pop("top_p", UNSET)

        chat_request_envelope = cls(
            firewall=firewall,
            max_tokens=max_tokens,
            messages=messages,
            modalities=modalities,
            model=model,
            speaker=speaker,
            stream=stream,
            temperature=temperature,
            top_p=top_p,
        )

        chat_request_envelope.additional_properties = d
        return chat_request_envelope

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
