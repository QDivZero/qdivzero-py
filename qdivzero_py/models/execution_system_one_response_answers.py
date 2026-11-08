from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.execution_decision_choice_answer import ExecutionDecisionChoiceAnswer
    from ..models.execution_decision_noul_answer import ExecutionDecisionNoulAnswer
    from ..models.execution_decision_score_answer import ExecutionDecisionScoreAnswer


T = TypeVar("T", bound="ExecutionSystemOneResponseAnswers")


@_attrs_define
class ExecutionSystemOneResponseAnswers:
    """ """

    additional_properties: dict[
        str, ExecutionDecisionChoiceAnswer | ExecutionDecisionNoulAnswer | ExecutionDecisionScoreAnswer
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.execution_decision_choice_answer import ExecutionDecisionChoiceAnswer
        from ..models.execution_decision_noul_answer import ExecutionDecisionNoulAnswer

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, ExecutionDecisionChoiceAnswer):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ExecutionDecisionNoulAnswer):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_decision_choice_answer import ExecutionDecisionChoiceAnswer
        from ..models.execution_decision_noul_answer import ExecutionDecisionNoulAnswer
        from ..models.execution_decision_score_answer import ExecutionDecisionScoreAnswer

        d = dict(src_dict)
        execution_system_one_response_answers = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(
                data: object,
            ) -> ExecutionDecisionChoiceAnswer | ExecutionDecisionNoulAnswer | ExecutionDecisionScoreAnswer:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_execution_decision_answer_type_0 = ExecutionDecisionChoiceAnswer.from_dict(data)

                    return componentsschemas_execution_decision_answer_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_execution_decision_answer_type_1 = ExecutionDecisionNoulAnswer.from_dict(data)

                    return componentsschemas_execution_decision_answer_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_execution_decision_answer_type_2 = ExecutionDecisionScoreAnswer.from_dict(data)

                return componentsschemas_execution_decision_answer_type_2

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        execution_system_one_response_answers.additional_properties = additional_properties
        return execution_system_one_response_answers

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> ExecutionDecisionChoiceAnswer | ExecutionDecisionNoulAnswer | ExecutionDecisionScoreAnswer:
        return self.additional_properties[key]

    def __setitem__(
        self,
        key: str,
        value: ExecutionDecisionChoiceAnswer | ExecutionDecisionNoulAnswer | ExecutionDecisionScoreAnswer,
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
