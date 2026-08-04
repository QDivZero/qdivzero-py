from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateFirewallRuleRequest")



@_attrs_define
class UpdateFirewallRuleRequest:
    """ 
        Attributes:
            category (str | Unset):
            default_severity (str | Unset):
            description (str | Unset):
            name (str | Unset):
            prompt (str | Unset):
            slug (str | Unset):
     """

    category: str | Unset = UNSET
    default_severity: str | Unset = UNSET
    description: str | Unset = UNSET
    name: str | Unset = UNSET
    prompt: str | Unset = UNSET
    slug: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        category = self.category

        default_severity = self.default_severity

        description = self.description

        name = self.name

        prompt = self.prompt

        slug = self.slug


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if category is not UNSET:
            field_dict["category"] = category
        if default_severity is not UNSET:
            field_dict["default_severity"] = default_severity
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if slug is not UNSET:
            field_dict["slug"] = slug

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = d.pop("category", UNSET)

        default_severity = d.pop("default_severity", UNSET)

        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        prompt = d.pop("prompt", UNSET)

        slug = d.pop("slug", UNSET)

        update_firewall_rule_request = cls(
            category=category,
            default_severity=default_severity,
            description=description,
            name=name,
            prompt=prompt,
            slug=slug,
        )


        update_firewall_rule_request.additional_properties = d
        return update_firewall_rule_request

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
