from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.execution_decision_choice_question import ExecutionDecisionChoiceQuestion
    from ..models.execution_decision_noul_question import ExecutionDecisionNoulQuestion
    from ..models.execution_decision_score_question import ExecutionDecisionScoreQuestion


T = TypeVar("T", bound="ExecutionSystemOneRequestQuestions")


@_attrs_define
class ExecutionSystemOneRequestQuestions:
    """Nonblank question IDs up to 256 UTF-8 bytes; insertion order is retained."""

    additional_properties: dict[
        str, ExecutionDecisionChoiceQuestion | ExecutionDecisionNoulQuestion | ExecutionDecisionScoreQuestion
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.execution_decision_choice_question import ExecutionDecisionChoiceQuestion
        from ..models.execution_decision_noul_question import ExecutionDecisionNoulQuestion

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, ExecutionDecisionChoiceQuestion):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ExecutionDecisionNoulQuestion):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_decision_choice_question import ExecutionDecisionChoiceQuestion
        from ..models.execution_decision_noul_question import ExecutionDecisionNoulQuestion
        from ..models.execution_decision_score_question import ExecutionDecisionScoreQuestion

        d = dict(src_dict)
        execution_system_one_request_questions = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(
                data: object,
            ) -> ExecutionDecisionChoiceQuestion | ExecutionDecisionNoulQuestion | ExecutionDecisionScoreQuestion:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_execution_decision_question_type_0 = ExecutionDecisionChoiceQuestion.from_dict(
                        data
                    )

                    return componentsschemas_execution_decision_question_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_execution_decision_question_type_1 = ExecutionDecisionNoulQuestion.from_dict(data)

                    return componentsschemas_execution_decision_question_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_execution_decision_question_type_2 = ExecutionDecisionScoreQuestion.from_dict(data)

                return componentsschemas_execution_decision_question_type_2

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        execution_system_one_request_questions.additional_properties = additional_properties
        return execution_system_one_request_questions

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> ExecutionDecisionChoiceQuestion | ExecutionDecisionNoulQuestion | ExecutionDecisionScoreQuestion:
        return self.additional_properties[key]

    def __setitem__(
        self,
        key: str,
        value: ExecutionDecisionChoiceQuestion | ExecutionDecisionNoulQuestion | ExecutionDecisionScoreQuestion,
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
