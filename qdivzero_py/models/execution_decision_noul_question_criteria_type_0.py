from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecutionDecisionNoulQuestionCriteriaType0")


@_attrs_define
class ExecutionDecisionNoulQuestionCriteriaType0:
    """
    Attributes:
        false_ (None | str | Unset):
        true_ (None | str | Unset):
    """

    false_: None | str | Unset = UNSET
    true_: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        false_: None | str | Unset
        if isinstance(self.false_, Unset):
            false_ = UNSET
        else:
            false_ = self.false_

        true_: None | str | Unset
        if isinstance(self.true_, Unset):
            true_ = UNSET
        else:
            true_ = self.true_

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if false_ is not UNSET:
            field_dict["false"] = false_
        if true_ is not UNSET:
            field_dict["true"] = true_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_false_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        false_ = _parse_false_(d.pop("false", UNSET))

        def _parse_true_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        true_ = _parse_true_(d.pop("true", UNSET))

        execution_decision_noul_question_criteria_type_0 = cls(
            false_=false_,
            true_=true_,
        )

        return execution_decision_noul_question_criteria_type_0
