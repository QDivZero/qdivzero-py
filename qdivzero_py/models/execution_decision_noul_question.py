from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.execution_decision_noul_question_type import ExecutionDecisionNoulQuestionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execution_decision_noul_question_criteria_type_0 import ExecutionDecisionNoulQuestionCriteriaType0


T = TypeVar("T", bound="ExecutionDecisionNoulQuestion")


@_attrs_define
class ExecutionDecisionNoulQuestion:
    """
    Attributes:
        type_ (ExecutionDecisionNoulQuestionType):
        criteria (ExecutionDecisionNoulQuestionCriteriaType0 | None | Unset):
        instructions (None | str | Unset): Question instructions as text or null.
    """

    type_: ExecutionDecisionNoulQuestionType
    criteria: ExecutionDecisionNoulQuestionCriteriaType0 | None | Unset = UNSET
    instructions: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.execution_decision_noul_question_criteria_type_0 import ExecutionDecisionNoulQuestionCriteriaType0

        type_ = self.type_.value

        criteria: dict[str, Any] | None | Unset
        if isinstance(self.criteria, Unset):
            criteria = UNSET
        elif isinstance(self.criteria, ExecutionDecisionNoulQuestionCriteriaType0):
            criteria = self.criteria.to_dict()
        else:
            criteria = self.criteria

        instructions: None | str | Unset
        if isinstance(self.instructions, Unset):
            instructions = UNSET
        else:
            instructions = self.instructions

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
            }
        )
        if criteria is not UNSET:
            field_dict["criteria"] = criteria
        if instructions is not UNSET:
            field_dict["instructions"] = instructions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_decision_noul_question_criteria_type_0 import ExecutionDecisionNoulQuestionCriteriaType0

        d = dict(src_dict)
        type_ = ExecutionDecisionNoulQuestionType(d.pop("type"))

        def _parse_criteria(data: object) -> ExecutionDecisionNoulQuestionCriteriaType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                criteria_type_0 = ExecutionDecisionNoulQuestionCriteriaType0.from_dict(data)

                return criteria_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExecutionDecisionNoulQuestionCriteriaType0 | None | Unset, data)

        criteria = _parse_criteria(d.pop("criteria", UNSET))

        def _parse_instructions(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        instructions = _parse_instructions(d.pop("instructions", UNSET))

        execution_decision_noul_question = cls(
            type_=type_,
            criteria=criteria,
            instructions=instructions,
        )

        return execution_decision_noul_question
