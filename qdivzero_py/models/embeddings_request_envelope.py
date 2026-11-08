from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EmbeddingsRequestEnvelope")


@_attrs_define
class EmbeddingsRequestEnvelope:
    """
    Attributes:
        input_ (list[int] | Unset):
        model (str | Unset):
    """

    input_: list[int] | Unset = UNSET
    model: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_: list[int] | Unset = UNSET
        if not isinstance(self.input_, Unset):
            input_ = self.input_

        model = self.model

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if input_ is not UNSET:
            field_dict["input"] = input_
        if model is not UNSET:
            field_dict["model"] = model

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        input_ = cast(list[int], d.pop("input", UNSET))

        model = d.pop("model", UNSET)

        embeddings_request_envelope = cls(
            input_=input_,
            model=model,
        )

        embeddings_request_envelope.additional_properties = d
        return embeddings_request_envelope

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
