from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.execution_decision_score_answer_type import ExecutionDecisionScoreAnswerType

if TYPE_CHECKING:
    from ..models.execution_decision_score_answer_legend import ExecutionDecisionScoreAnswerLegend
    from ..models.execution_decision_score_answer_probabilities import ExecutionDecisionScoreAnswerProbabilities


T = TypeVar("T", bound="ExecutionDecisionScoreAnswer")


@_attrs_define
class ExecutionDecisionScoreAnswer:
    """
    Attributes:
        confidence (float): Finite probability. Confidence may be lower than the normalized option probability because
            native models also report mass outside the answer labels.
        legend (ExecutionDecisionScoreAnswerLegend): Every 0-indexed key matches its requested level description. Native
            null descriptions are returned as the string None.
        probabilities (ExecutionDecisionScoreAnswerProbabilities): Complete distribution over declared options;
            probabilities sum to one within rounding tolerance.
        score (float): Expected 0-indexed level; bounded by the final declared level.
        type_ (ExecutionDecisionScoreAnswerType):
    """

    confidence: float
    legend: ExecutionDecisionScoreAnswerLegend
    probabilities: ExecutionDecisionScoreAnswerProbabilities
    score: float
    type_: ExecutionDecisionScoreAnswerType

    def to_dict(self) -> dict[str, Any]:
        confidence = self.confidence

        legend = self.legend.to_dict()

        probabilities = self.probabilities.to_dict()

        score = self.score

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "confidence": confidence,
                "legend": legend,
                "probabilities": probabilities,
                "score": score,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_decision_score_answer_legend import ExecutionDecisionScoreAnswerLegend
        from ..models.execution_decision_score_answer_probabilities import ExecutionDecisionScoreAnswerProbabilities

        d = dict(src_dict)
        confidence = d.pop("confidence")

        legend = ExecutionDecisionScoreAnswerLegend.from_dict(d.pop("legend"))

        probabilities = ExecutionDecisionScoreAnswerProbabilities.from_dict(d.pop("probabilities"))

        score = d.pop("score")

        type_ = ExecutionDecisionScoreAnswerType(d.pop("type"))

        execution_decision_score_answer = cls(
            confidence=confidence,
            legend=legend,
            probabilities=probabilities,
            score=score,
            type_=type_,
        )

        return execution_decision_score_answer
