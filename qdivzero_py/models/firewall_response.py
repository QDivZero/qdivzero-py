from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FirewallResponse")


@_attrs_define
class FirewallResponse:
    """
    Attributes:
        created_at (str | Unset):
        description (str | Unset):
        evaluator_serving_name (str | Unset):
        mode (str | Unset):
        name (str | Unset):
        rule_slugs (list[str] | Unset):
        slug (str | Unset):
        updated_at (str | Unset):
    """

    created_at: str | Unset = UNSET
    description: str | Unset = UNSET
    evaluator_serving_name: str | Unset = UNSET
    mode: str | Unset = UNSET
    name: str | Unset = UNSET
    rule_slugs: list[str] | Unset = UNSET
    slug: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        description = self.description

        evaluator_serving_name = self.evaluator_serving_name

        mode = self.mode

        name = self.name

        rule_slugs: list[str] | Unset = UNSET
        if not isinstance(self.rule_slugs, Unset):
            rule_slugs = self.rule_slugs

        slug = self.slug

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if evaluator_serving_name is not UNSET:
            field_dict["evaluator_serving_name"] = evaluator_serving_name
        if mode is not UNSET:
            field_dict["mode"] = mode
        if name is not UNSET:
            field_dict["name"] = name
        if rule_slugs is not UNSET:
            field_dict["rule_slugs"] = rule_slugs
        if slug is not UNSET:
            field_dict["slug"] = slug
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        description = d.pop("description", UNSET)

        evaluator_serving_name = d.pop("evaluator_serving_name", UNSET)

        mode = d.pop("mode", UNSET)

        name = d.pop("name", UNSET)

        rule_slugs = cast(list[str], d.pop("rule_slugs", UNSET))

        slug = d.pop("slug", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        firewall_response = cls(
            created_at=created_at,
            description=description,
            evaluator_serving_name=evaluator_serving_name,
            mode=mode,
            name=name,
            rule_slugs=rule_slugs,
            slug=slug,
            updated_at=updated_at,
        )

        firewall_response.additional_properties = d
        return firewall_response

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
