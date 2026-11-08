from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.protocol_context_management import ProtocolContextManagement
    from ..models.responses_request_envelope_metadata import ResponsesRequestEnvelopeMetadata
    from ..models.responses_request_envelope_reasoning import ResponsesRequestEnvelopeReasoning


T = TypeVar("T", bound="ResponsesRequestEnvelope")


@_attrs_define
class ResponsesRequestEnvelope:
    """
    Attributes:
        context_management (list[ProtocolContextManagement] | Unset):
        input_ (list[int] | Unset):
        instructions (str | Unset):
        max_output_tokens (int | Unset):
        metadata (ResponsesRequestEnvelopeMetadata | Unset):
        model (str | Unset):
        previous_response_id (str | Unset):
        reasoning (ResponsesRequestEnvelopeReasoning | Unset):
        reasoning_effort (str | Unset):
        store (bool | Unset):
        stream (bool | Unset):
        thinking_token_budget (int | Unset):
        tools (list[int] | Unset):
        type_ (str | Unset):
    """

    context_management: list[ProtocolContextManagement] | Unset = UNSET
    input_: list[int] | Unset = UNSET
    instructions: str | Unset = UNSET
    max_output_tokens: int | Unset = UNSET
    metadata: ResponsesRequestEnvelopeMetadata | Unset = UNSET
    model: str | Unset = UNSET
    previous_response_id: str | Unset = UNSET
    reasoning: ResponsesRequestEnvelopeReasoning | Unset = UNSET
    reasoning_effort: str | Unset = UNSET
    store: bool | Unset = UNSET
    stream: bool | Unset = UNSET
    thinking_token_budget: int | Unset = UNSET
    tools: list[int] | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        context_management: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.context_management, Unset):
            context_management = []
            for context_management_item_data in self.context_management:
                context_management_item = context_management_item_data.to_dict()
                context_management.append(context_management_item)

        input_: list[int] | Unset = UNSET
        if not isinstance(self.input_, Unset):
            input_ = self.input_

        instructions = self.instructions

        max_output_tokens = self.max_output_tokens

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        model = self.model

        previous_response_id = self.previous_response_id

        reasoning: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reasoning, Unset):
            reasoning = self.reasoning.to_dict()

        reasoning_effort = self.reasoning_effort

        store = self.store

        stream = self.stream

        thinking_token_budget = self.thinking_token_budget

        tools: list[int] | Unset = UNSET
        if not isinstance(self.tools, Unset):
            tools = self.tools

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if context_management is not UNSET:
            field_dict["context_management"] = context_management
        if input_ is not UNSET:
            field_dict["input"] = input_
        if instructions is not UNSET:
            field_dict["instructions"] = instructions
        if max_output_tokens is not UNSET:
            field_dict["max_output_tokens"] = max_output_tokens
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if model is not UNSET:
            field_dict["model"] = model
        if previous_response_id is not UNSET:
            field_dict["previous_response_id"] = previous_response_id
        if reasoning is not UNSET:
            field_dict["reasoning"] = reasoning
        if reasoning_effort is not UNSET:
            field_dict["reasoning_effort"] = reasoning_effort
        if store is not UNSET:
            field_dict["store"] = store
        if stream is not UNSET:
            field_dict["stream"] = stream
        if thinking_token_budget is not UNSET:
            field_dict["thinking_token_budget"] = thinking_token_budget
        if tools is not UNSET:
            field_dict["tools"] = tools
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.protocol_context_management import ProtocolContextManagement
        from ..models.responses_request_envelope_metadata import ResponsesRequestEnvelopeMetadata
        from ..models.responses_request_envelope_reasoning import ResponsesRequestEnvelopeReasoning

        d = dict(src_dict)
        _context_management = d.pop("context_management", UNSET)
        context_management: list[ProtocolContextManagement] | Unset = UNSET
        if _context_management is not UNSET:
            context_management = []
            for context_management_item_data in _context_management:
                context_management_item = ProtocolContextManagement.from_dict(context_management_item_data)

                context_management.append(context_management_item)

        input_ = cast(list[int], d.pop("input", UNSET))

        instructions = d.pop("instructions", UNSET)

        max_output_tokens = d.pop("max_output_tokens", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: ResponsesRequestEnvelopeMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ResponsesRequestEnvelopeMetadata.from_dict(_metadata)

        model = d.pop("model", UNSET)

        previous_response_id = d.pop("previous_response_id", UNSET)

        _reasoning = d.pop("reasoning", UNSET)
        reasoning: ResponsesRequestEnvelopeReasoning | Unset
        if isinstance(_reasoning, Unset):
            reasoning = UNSET
        else:
            reasoning = ResponsesRequestEnvelopeReasoning.from_dict(_reasoning)

        reasoning_effort = d.pop("reasoning_effort", UNSET)

        store = d.pop("store", UNSET)

        stream = d.pop("stream", UNSET)

        thinking_token_budget = d.pop("thinking_token_budget", UNSET)

        tools = cast(list[int], d.pop("tools", UNSET))

        type_ = d.pop("type", UNSET)

        responses_request_envelope = cls(
            context_management=context_management,
            input_=input_,
            instructions=instructions,
            max_output_tokens=max_output_tokens,
            metadata=metadata,
            model=model,
            previous_response_id=previous_response_id,
            reasoning=reasoning,
            reasoning_effort=reasoning_effort,
            store=store,
            stream=stream,
            thinking_token_budget=thinking_token_budget,
            tools=tools,
            type_=type_,
        )

        responses_request_envelope.additional_properties = d
        return responses_request_envelope

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
