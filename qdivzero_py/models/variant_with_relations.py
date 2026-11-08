from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.variant import Variant


T = TypeVar("T", bound="VariantWithRelations")


@_attrs_define
class VariantWithRelations:
    """
    Attributes:
        description (str | Unset):
        name (str | Unset):
        template_category (str | Unset):
        template_is_active (bool | Unset):
        template_slug (str | Unset):
        template_tags (list[str] | Unset):
        variant (Variant | Unset):
    """

    description: str | Unset = UNSET
    name: str | Unset = UNSET
    template_category: str | Unset = UNSET
    template_is_active: bool | Unset = UNSET
    template_slug: str | Unset = UNSET
    template_tags: list[str] | Unset = UNSET
    variant: Variant | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        name = self.name

        template_category = self.template_category

        template_is_active = self.template_is_active

        template_slug = self.template_slug

        template_tags: list[str] | Unset = UNSET
        if not isinstance(self.template_tags, Unset):
            template_tags = self.template_tags

        variant: dict[str, Any] | Unset = UNSET
        if not isinstance(self.variant, Unset):
            variant = self.variant.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if template_category is not UNSET:
            field_dict["template_category"] = template_category
        if template_is_active is not UNSET:
            field_dict["template_is_active"] = template_is_active
        if template_slug is not UNSET:
            field_dict["template_slug"] = template_slug
        if template_tags is not UNSET:
            field_dict["template_tags"] = template_tags
        if variant is not UNSET:
            field_dict["variant"] = variant

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.variant import Variant

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        template_category = d.pop("template_category", UNSET)

        template_is_active = d.pop("template_is_active", UNSET)

        template_slug = d.pop("template_slug", UNSET)

        template_tags = cast(list[str], d.pop("template_tags", UNSET))

        _variant = d.pop("variant", UNSET)
        variant: Variant | Unset
        if isinstance(_variant, Unset):
            variant = UNSET
        else:
            variant = Variant.from_dict(_variant)

        variant_with_relations = cls(
            description=description,
            name=name,
            template_category=template_category,
            template_is_active=template_is_active,
            template_slug=template_slug,
            template_tags=template_tags,
            variant=variant,
        )

        variant_with_relations.additional_properties = d
        return variant_with_relations

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
