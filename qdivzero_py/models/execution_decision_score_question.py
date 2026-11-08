from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.execution_decision_score_question_type import ExecutionDecisionScoreQuestionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecutionDecisionScoreQuestion")


@_attrs_define
class ExecutionDecisionScoreQuestion:
    """
    Attributes:
        criteria (list[None | str]):
        type_ (ExecutionDecisionScoreQuestionType):
        instructions (None | str | Unset): Question instructions as text or null.
    """

    criteria: list[None | str]
    type_: ExecutionDecisionScoreQuestionType
    instructions: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        criteria = []
        for criteria_item_data in self.criteria:
            criteria_item: None | str
            criteria_item = criteria_item_data
            criteria.append(criteria_item)

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
        d = dict(src_dict)
        criteria = []
        _criteria = d.pop("criteria")
        for criteria_item_data in _criteria:

            def _parse_criteria_item(data: object) -> None | str:
                if data is None:
                    return data
                return cast(None | str, data)

            criteria_item = _parse_criteria_item(criteria_item_data)

            criteria.append(criteria_item)

        type_ = ExecutionDecisionScoreQuestionType(d.pop("type"))

        def _parse_instructions(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        instructions = _parse_instructions(d.pop("instructions", UNSET))

        execution_decision_score_question = cls(
            criteria=criteria,
            type_=type_,
            instructions=instructions,
        )

        return execution_decision_score_question
