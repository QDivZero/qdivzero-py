from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.execution_decision_choice_answer_type import ExecutionDecisionChoiceAnswerType

if TYPE_CHECKING:
    from ..models.execution_decision_choice_answer_probabilities import ExecutionDecisionChoiceAnswerProbabilities


T = TypeVar("T", bound="ExecutionDecisionChoiceAnswer")


@_attrs_define
class ExecutionDecisionChoiceAnswer:
    """
    Attributes:
        choice (str): A declared option with maximal normalized probability.
        confidence (float): Finite probability. Confidence may be lower than the normalized option probability because
            native models also report mass outside the answer labels.
        probabilities (ExecutionDecisionChoiceAnswerProbabilities): Complete distribution over declared options;
            probabilities sum to one within rounding tolerance.
        type_ (ExecutionDecisionChoiceAnswerType):
    """

    choice: str
    confidence: float
    probabilities: ExecutionDecisionChoiceAnswerProbabilities
    type_: ExecutionDecisionChoiceAnswerType

    def to_dict(self) -> dict[str, Any]:
        choice = self.choice

        confidence = self.confidence

        probabilities = self.probabilities.to_dict()

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "choice": choice,
                "confidence": confidence,
                "probabilities": probabilities,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_decision_choice_answer_probabilities import ExecutionDecisionChoiceAnswerProbabilities

        d = dict(src_dict)
        choice = d.pop("choice")

        confidence = d.pop("confidence")

        probabilities = ExecutionDecisionChoiceAnswerProbabilities.from_dict(d.pop("probabilities"))

        type_ = ExecutionDecisionChoiceAnswerType(d.pop("type"))

        execution_decision_choice_answer = cls(
            choice=choice,
            confidence=confidence,
            probabilities=probabilities,
            type_=type_,
        )

        return execution_decision_choice_answer
