from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ExecutionDecisionNoulAnswerProbabilitiesType0")


@_attrs_define
class ExecutionDecisionNoulAnswerProbabilitiesType0:
    """
    Attributes:
        no (float): Finite probability. Confidence may be lower than the normalized option probability because native
            models also report mass outside the answer labels.
        yes (float): Finite probability. Confidence may be lower than the normalized option probability because native
            models also report mass outside the answer labels.
    """

    no: float
    yes: float

    def to_dict(self) -> dict[str, Any]:
        no = self.no

        yes = self.yes

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "no": no,
                "yes": yes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        no = d.pop("no")

        yes = d.pop("yes")

        execution_decision_noul_answer_probabilities_type_0 = cls(
            no=no,
            yes=yes,
        )

        return execution_decision_noul_answer_probabilities_type_0
