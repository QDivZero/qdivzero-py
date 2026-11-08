from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FirewallRuleEvaluationRequest")


@_attrs_define
class FirewallRuleEvaluationRequest:
    """
    Attributes:
        evaluator_serving_name (str | Unset):
        input_ (str | Unset):
    """

    evaluator_serving_name: str | Unset = UNSET
    input_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        evaluator_serving_name = self.evaluator_serving_name

        input_ = self.input_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if evaluator_serving_name is not UNSET:
            field_dict["evaluator_serving_name"] = evaluator_serving_name
        if input_ is not UNSET:
            field_dict["input"] = input_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        evaluator_serving_name = d.pop("evaluator_serving_name", UNSET)

        input_ = d.pop("input", UNSET)

        firewall_rule_evaluation_request = cls(
            evaluator_serving_name=evaluator_serving_name,
            input_=input_,
        )

        firewall_rule_evaluation_request.additional_properties = d
        return firewall_rule_evaluation_request

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
