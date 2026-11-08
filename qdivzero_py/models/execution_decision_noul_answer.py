from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.execution_decision_noul_answer_type import ExecutionDecisionNoulAnswerType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execution_decision_noul_answer_probabilities_type_0 import (
        ExecutionDecisionNoulAnswerProbabilitiesType0,
    )
    from ..models.execution_decision_noul_answer_probabilities_type_1 import (
        ExecutionDecisionNoulAnswerProbabilitiesType1,
    )


T = TypeVar("T", bound="ExecutionDecisionNoulAnswer")


@_attrs_define
class ExecutionDecisionNoulAnswer:
    """
    Attributes:
        noul (float): Finite probability. Confidence may be lower than the normalized option probability because native
            models also report mass outside the answer labels.
        type_ (ExecutionDecisionNoulAnswerType):
        confidence (float | Unset): Finite probability. Confidence may be lower than the normalized option probability
            because native models also report mass outside the answer labels.
        probabilities (ExecutionDecisionNoulAnswerProbabilitiesType0 | ExecutionDecisionNoulAnswerProbabilitiesType1 |
            Unset): Complete distribution over declared options; probabilities sum to one within rounding tolerance.
    """

    noul: float
    type_: ExecutionDecisionNoulAnswerType
    confidence: float | Unset = UNSET
    probabilities: (
        ExecutionDecisionNoulAnswerProbabilitiesType0 | ExecutionDecisionNoulAnswerProbabilitiesType1 | Unset
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.execution_decision_noul_answer_probabilities_type_0 import (
            ExecutionDecisionNoulAnswerProbabilitiesType0,
        )

        noul = self.noul

        type_ = self.type_.value

        confidence = self.confidence

        probabilities: dict[str, Any] | Unset
        if isinstance(self.probabilities, Unset):
            probabilities = UNSET
        elif isinstance(self.probabilities, ExecutionDecisionNoulAnswerProbabilitiesType0):
            probabilities = self.probabilities.to_dict()
        else:
            probabilities = self.probabilities.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "noul": noul,
                "type": type_,
            }
        )
        if confidence is not UNSET:
            field_dict["confidence"] = confidence
        if probabilities is not UNSET:
            field_dict["probabilities"] = probabilities

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_decision_noul_answer_probabilities_type_0 import (
            ExecutionDecisionNoulAnswerProbabilitiesType0,
        )
        from ..models.execution_decision_noul_answer_probabilities_type_1 import (
            ExecutionDecisionNoulAnswerProbabilitiesType1,
        )

        d = dict(src_dict)
        noul = d.pop("noul")

        type_ = ExecutionDecisionNoulAnswerType(d.pop("type"))

        confidence = d.pop("confidence", UNSET)

        def _parse_probabilities(
            data: object,
        ) -> ExecutionDecisionNoulAnswerProbabilitiesType0 | ExecutionDecisionNoulAnswerProbabilitiesType1 | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                probabilities_type_0 = ExecutionDecisionNoulAnswerProbabilitiesType0.from_dict(data)

                return probabilities_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            probabilities_type_1 = ExecutionDecisionNoulAnswerProbabilitiesType1.from_dict(data)

            return probabilities_type_1

        probabilities = _parse_probabilities(d.pop("probabilities", UNSET))

        execution_decision_noul_answer = cls(
            noul=noul,
            type_=type_,
            confidence=confidence,
            probabilities=probabilities,
        )

        return execution_decision_noul_answer
