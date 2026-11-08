from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execution_system_one_request_questions import ExecutionSystemOneRequestQuestions
    from ..models.execution_system_one_request_state_type_1 import ExecutionSystemOneRequestStateType1


T = TypeVar("T", bound="ExecutionSystemOneRequest")


@_attrs_define
class ExecutionSystemOneRequest:
    """Request up to 32 MiB and depth 64, with at most 1 MiB of original JSON excluding only the top-level images value; at
    most 64 questions. Each instructions/criteria value is bounded to 64 KiB of JSON. Images require Qwen3.5-9B,
    DiffusionGemma, Clef or Clef Flash; Nimble rejects images. Nested media inputs and unknown fields are rejected.

        Attributes:
            model (str):
            questions (ExecutionSystemOneRequestQuestions): Nonblank question IDs up to 256 UTF-8 bytes; insertion order is
                retained.
            state (ExecutionSystemOneRequestStateType1 | list[Any] | str):
            images (list[str] | Unset): Inline images only, in attachment order. At most 5 MiB decoded and 16 million pixels
                each. Runtime validates actual image content and its declared MIME type. Remote and file URLs, malformed base64
                and null are rejected.
            instructions (None | str | Unset): Native Qwen/DiffusionGemma global instructions; Clef/Nimble reject nonempty
                global instructions.
    """

    model: str
    questions: ExecutionSystemOneRequestQuestions
    state: ExecutionSystemOneRequestStateType1 | list[Any] | str
    images: list[str] | Unset = UNSET
    instructions: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.execution_system_one_request_state_type_1 import ExecutionSystemOneRequestStateType1

        model = self.model

        questions = self.questions.to_dict()

        state: dict[str, Any] | list[Any] | str
        if isinstance(self.state, ExecutionSystemOneRequestStateType1):
            state = self.state.to_dict()
        elif isinstance(self.state, list):
            state = self.state

        else:
            state = self.state

        images: list[str] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = self.images

        instructions: None | str | Unset
        if isinstance(self.instructions, Unset):
            instructions = UNSET
        else:
            instructions = self.instructions

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "model": model,
                "questions": questions,
                "state": state,
            }
        )
        if images is not UNSET:
            field_dict["images"] = images
        if instructions is not UNSET:
            field_dict["instructions"] = instructions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_system_one_request_questions import ExecutionSystemOneRequestQuestions
        from ..models.execution_system_one_request_state_type_1 import ExecutionSystemOneRequestStateType1

        d = dict(src_dict)
        model = d.pop("model")

        questions = ExecutionSystemOneRequestQuestions.from_dict(d.pop("questions"))

        def _parse_state(data: object) -> ExecutionSystemOneRequestStateType1 | list[Any] | str:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                state_type_1 = ExecutionSystemOneRequestStateType1.from_dict(data)

                return state_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                state_type_2 = cast(list[Any], data)

                return state_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExecutionSystemOneRequestStateType1 | list[Any] | str, data)

        state = _parse_state(d.pop("state"))

        images = cast(list[str], d.pop("images", UNSET))

        def _parse_instructions(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        instructions = _parse_instructions(d.pop("instructions", UNSET))

        execution_system_one_request = cls(
            model=model,
            questions=questions,
            state=state,
            images=images,
            instructions=instructions,
        )

        return execution_system_one_request
