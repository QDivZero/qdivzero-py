from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execution_decision_usage import ExecutionDecisionUsage
    from ..models.execution_system_one_response_answers import ExecutionSystemOneResponseAnswers
    from ..models.execution_system_one_response_diagnostics import ExecutionSystemOneResponseDiagnostics


T = TypeVar("T", bound="ExecutionSystemOneResponse")


@_attrs_define
class ExecutionSystemOneResponse:
    """Response up to 1 MiB. Answer keys exactly match the requested question IDs; answer types/options match their
    declarations.

        Attributes:
            answers (ExecutionSystemOneResponseAnswers):
            model (str): The account-owned serving name or instance UUID used by the caller.
            usage (ExecutionDecisionUsage):
            created (int | Unset):
            diagnostics (ExecutionSystemOneResponseDiagnostics | Unset): When present, contains one diagnostic for every
                requested question.
            id (str | Unset):
            object_ (str | Unset):
    """

    answers: ExecutionSystemOneResponseAnswers
    model: str
    usage: ExecutionDecisionUsage
    created: int | Unset = UNSET
    diagnostics: ExecutionSystemOneResponseDiagnostics | Unset = UNSET
    id: str | Unset = UNSET
    object_: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        answers = self.answers.to_dict()

        model = self.model

        usage = self.usage.to_dict()

        created = self.created

        diagnostics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.diagnostics, Unset):
            diagnostics = self.diagnostics.to_dict()

        id = self.id

        object_ = self.object_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "answers": answers,
                "model": model,
                "usage": usage,
            }
        )
        if created is not UNSET:
            field_dict["created"] = created
        if diagnostics is not UNSET:
            field_dict["diagnostics"] = diagnostics
        if id is not UNSET:
            field_dict["id"] = id
        if object_ is not UNSET:
            field_dict["object"] = object_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_decision_usage import ExecutionDecisionUsage
        from ..models.execution_system_one_response_answers import ExecutionSystemOneResponseAnswers
        from ..models.execution_system_one_response_diagnostics import ExecutionSystemOneResponseDiagnostics

        d = dict(src_dict)
        answers = ExecutionSystemOneResponseAnswers.from_dict(d.pop("answers"))

        model = d.pop("model")

        usage = ExecutionDecisionUsage.from_dict(d.pop("usage"))

        created = d.pop("created", UNSET)

        _diagnostics = d.pop("diagnostics", UNSET)
        diagnostics: ExecutionSystemOneResponseDiagnostics | Unset
        if isinstance(_diagnostics, Unset):
            diagnostics = UNSET
        else:
            diagnostics = ExecutionSystemOneResponseDiagnostics.from_dict(_diagnostics)

        id = d.pop("id", UNSET)

        object_ = d.pop("object", UNSET)

        execution_system_one_response = cls(
            answers=answers,
            model=model,
            usage=usage,
            created=created,
            diagnostics=diagnostics,
            id=id,
            object_=object_,
        )

        return execution_system_one_response
