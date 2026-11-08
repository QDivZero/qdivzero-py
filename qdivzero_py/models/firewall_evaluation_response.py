from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FirewallEvaluationResponse")


@_attrs_define
class FirewallEvaluationResponse:
    """
    Attributes:
        allowed (bool | Unset):
        evaluator_serving_name (str | Unset):
        firewall_slug (str | Unset):
        matched_rules (list[str] | Unset):
        mode (str | Unset):
        reason (str | Unset):
        severity (str | Unset):
    """

    allowed: bool | Unset = UNSET
    evaluator_serving_name: str | Unset = UNSET
    firewall_slug: str | Unset = UNSET
    matched_rules: list[str] | Unset = UNSET
    mode: str | Unset = UNSET
    reason: str | Unset = UNSET
    severity: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allowed = self.allowed

        evaluator_serving_name = self.evaluator_serving_name

        firewall_slug = self.firewall_slug

        matched_rules: list[str] | Unset = UNSET
        if not isinstance(self.matched_rules, Unset):
            matched_rules = self.matched_rules

        mode = self.mode

        reason = self.reason

        severity = self.severity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allowed is not UNSET:
            field_dict["allowed"] = allowed
        if evaluator_serving_name is not UNSET:
            field_dict["evaluator_serving_name"] = evaluator_serving_name
        if firewall_slug is not UNSET:
            field_dict["firewall_slug"] = firewall_slug
        if matched_rules is not UNSET:
            field_dict["matched_rules"] = matched_rules
        if mode is not UNSET:
            field_dict["mode"] = mode
        if reason is not UNSET:
            field_dict["reason"] = reason
        if severity is not UNSET:
            field_dict["severity"] = severity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allowed = d.pop("allowed", UNSET)

        evaluator_serving_name = d.pop("evaluator_serving_name", UNSET)

        firewall_slug = d.pop("firewall_slug", UNSET)

        matched_rules = cast(list[str], d.pop("matched_rules", UNSET))

        mode = d.pop("mode", UNSET)

        reason = d.pop("reason", UNSET)

        severity = d.pop("severity", UNSET)

        firewall_evaluation_response = cls(
            allowed=allowed,
            evaluator_serving_name=evaluator_serving_name,
            firewall_slug=firewall_slug,
            matched_rules=matched_rules,
            mode=mode,
            reason=reason,
            severity=severity,
        )

        firewall_evaluation_response.additional_properties = d
        return firewall_evaluation_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
