from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.execution_decision_choice_question_type import ExecutionDecisionChoiceQuestionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execution_decision_choice_question_criteria import ExecutionDecisionChoiceQuestionCriteria


T = TypeVar("T", bound="ExecutionDecisionChoiceQuestion")


@_attrs_define
class ExecutionDecisionChoiceQuestion:
    """
    Attributes:
        criteria (ExecutionDecisionChoiceQuestionCriteria): Nonblank option IDs (up to 256 UTF-8 bytes) map to text or
            null descriptions.
        type_ (ExecutionDecisionChoiceQuestionType):
        instructions (None | str | Unset): Question instructions as text or null.
    """

    criteria: ExecutionDecisionChoiceQuestionCriteria
    type_: ExecutionDecisionChoiceQuestionType
    instructions: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        criteria = self.criteria.to_dict()

        type_ = self.type_.value

        instructions: None | str | Unset
        if isinstance(self.instructions, Unset):
            instructions = UNSET
        else:
            instructions = self.instructions

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "criteria": criteria,
                "type": type_,
            }
        )
        if instructions is not UNSET:
            field_dict["instructions"] = instructions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_decision_choice_question_criteria import ExecutionDecisionChoiceQuestionCriteria

        d = dict(src_dict)
        criteria = ExecutionDecisionChoiceQuestionCriteria.from_dict(d.pop("criteria"))

        type_ = ExecutionDecisionChoiceQuestionType(d.pop("type"))

        def _parse_instructions(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        instructions = _parse_instructions(d.pop("instructions", UNSET))

        execution_decision_choice_question = cls(
            criteria=criteria,
            type_=type_,
            instructions=instructions,
        )

        return execution_decision_choice_question
