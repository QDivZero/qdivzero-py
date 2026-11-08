from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ExecutionDecisionUsage")


@_attrs_define
class ExecutionDecisionUsage:
    """
    Attributes:
        input_tokens (int):
        output_tokens (int):
    """

    input_tokens: int
    output_tokens: int

    def to_dict(self) -> dict[str, Any]:
        input_tokens = self.input_tokens

        output_tokens = self.output_tokens

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "input_tokens": input_tokens,
                "output_tokens": output_tokens,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        input_tokens = d.pop("input_tokens")

        output_tokens = d.pop("output_tokens")

        execution_decision_usage = cls(
            input_tokens=input_tokens,
            output_tokens=output_tokens,
        )

        return execution_decision_usage
