from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ExecutionDecisionNoulAnswerProbabilitiesType1")


@_attrs_define
class ExecutionDecisionNoulAnswerProbabilitiesType1:
    """
    Attributes:
        false_ (float): Finite probability. Confidence may be lower than the normalized option probability because
            native models also report mass outside the answer labels.
        true_ (float): Finite probability. Confidence may be lower than the normalized option probability because native
            models also report mass outside the answer labels.
    """

    false_: float
    true_: float

    def to_dict(self) -> dict[str, Any]:
        false_ = self.false_

        true_ = self.true_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "false": false_,
                "true": true_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        false_ = d.pop("false")

        true_ = d.pop("true")

        execution_decision_noul_answer_probabilities_type_1 = cls(
            false_=false_,
            true_=true_,
        )

        return execution_decision_noul_answer_probabilities_type_1
