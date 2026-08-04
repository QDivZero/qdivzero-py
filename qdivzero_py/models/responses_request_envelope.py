from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.responses_request_envelope_reasoning import ResponsesRequestEnvelopeReasoning





T = TypeVar("T", bound="ResponsesRequestEnvelope")



@_attrs_define
class ResponsesRequestEnvelope:
    """ 
        Attributes:
            input_ (list[int] | Unset):
            model (str | Unset):
            previous_response_id (str | Unset):
            reasoning (ResponsesRequestEnvelopeReasoning | Unset):
            reasoning_effort (str | Unset):
            store (bool | Unset):
            stream (bool | Unset):
            thinking_token_budget (int | Unset):
            type_ (str | Unset):
     """

    input_: list[int] | Unset = UNSET
    model: str | Unset = UNSET
    previous_response_id: str | Unset = UNSET
    reasoning: ResponsesRequestEnvelopeReasoning | Unset = UNSET
    reasoning_effort: str | Unset = UNSET
    store: bool | Unset = UNSET
    stream: bool | Unset = UNSET
    thinking_token_budget: int | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        input_: list[int] | Unset = UNSET
        if not isinstance(self.input_, Unset):
            input_ = self.input_



        model = self.model

        previous_response_id = self.previous_response_id

        reasoning: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reasoning, Unset):
            reasoning = self.reasoning.to_dict()

        reasoning_effort = self.reasoning_effort

        store = self.store

        stream = self.stream

        thinking_token_budget = self.thinking_token_budget

        type_ = self.type_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if input_ is not UNSET:
            field_dict["input"] = input_
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
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.responses_request_envelope_reasoning import ResponsesRequestEnvelopeReasoning
        d = dict(src_dict)
        input_ = cast(list[int], d.pop("input", UNSET))


        model = d.pop("model", UNSET)

        previous_response_id = d.pop("previous_response_id", UNSET)

        _reasoning = d.pop("reasoning", UNSET)
        reasoning: ResponsesRequestEnvelopeReasoning | Unset
        if isinstance(_reasoning,  Unset):
            reasoning = UNSET
        else:
            reasoning = ResponsesRequestEnvelopeReasoning.from_dict(_reasoning)




        reasoning_effort = d.pop("reasoning_effort", UNSET)

        store = d.pop("store", UNSET)

        stream = d.pop("stream", UNSET)

        thinking_token_budget = d.pop("thinking_token_budget", UNSET)

        type_ = d.pop("type", UNSET)

        responses_request_envelope = cls(
            input_=input_,
            model=model,
            previous_response_id=previous_response_id,
            reasoning=reasoning,
            reasoning_effort=reasoning_effort,
            store=store,
            stream=stream,
            thinking_token_budget=thinking_token_budget,
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
