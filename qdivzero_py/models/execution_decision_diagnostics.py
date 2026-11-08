from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ExecutionDecisionDiagnostics")


@_attrs_define
class ExecutionDecisionDiagnostics:
    """
    Attributes:
        argmax_is_label (bool):
        label_mass (float): Finite probability. Confidence may be lower than the normalized option probability because
            native models also report mass outside the answer labels.
    """

    argmax_is_label: bool
    label_mass: float

    def to_dict(self) -> dict[str, Any]:
        argmax_is_label = self.argmax_is_label

        label_mass = self.label_mass

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "argmax_is_label": argmax_is_label,
                "label_mass": label_mass,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        argmax_is_label = d.pop("argmax_is_label")

        label_mass = d.pop("label_mass")

        execution_decision_diagnostics = cls(
            argmax_is_label=argmax_is_label,
            label_mass=label_mass,
        )

        return execution_decision_diagnostics
