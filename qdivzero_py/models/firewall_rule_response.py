from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FirewallRuleResponse")



@_attrs_define
class FirewallRuleResponse:
    """ 
        Attributes:
            category (str | Unset):
            created_at (str | Unset):
            default_severity (str | Unset):
            description (str | Unset):
            name (str | Unset):
            prompt (str | Unset):
            recommended (bool | Unset):
            slug (str | Unset):
            source (str | Unset):
            updated_at (str | Unset):
     """

    category: str | Unset = UNSET
    created_at: str | Unset = UNSET
    default_severity: str | Unset = UNSET
    description: str | Unset = UNSET
    name: str | Unset = UNSET
    prompt: str | Unset = UNSET
    recommended: bool | Unset = UNSET
    slug: str | Unset = UNSET
    source: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        category = self.category

        created_at = self.created_at

        default_severity = self.default_severity

        description = self.description

        name = self.name

        prompt = self.prompt

        recommended = self.recommended

        slug = self.slug

        source = self.source

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if category is not UNSET:
            field_dict["category"] = category
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if default_severity is not UNSET:
            field_dict["default_severity"] = default_severity
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if recommended is not UNSET:
            field_dict["recommended"] = recommended
        if slug is not UNSET:
            field_dict["slug"] = slug
        if source is not UNSET:
            field_dict["source"] = source
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = d.pop("category", UNSET)

        created_at = d.pop("created_at", UNSET)

        default_severity = d.pop("default_severity", UNSET)

        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        prompt = d.pop("prompt", UNSET)

        recommended = d.pop("recommended", UNSET)

        slug = d.pop("slug", UNSET)

        source = d.pop("source", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        firewall_rule_response = cls(
            category=category,
            created_at=created_at,
            default_severity=default_severity,
            description=description,
            name=name,
            prompt=prompt,
            recommended=recommended,
            slug=slug,
            source=source,
            updated_at=updated_at,
        )


        firewall_rule_response.additional_properties = d
        return firewall_rule_response

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
