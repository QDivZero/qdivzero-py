from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.template import Template
    from ..models.variant_with_relations import VariantWithRelations


T = TypeVar("T", bound="TemplateWithVariants")


@_attrs_define
class TemplateWithVariants:
    """
    Attributes:
        description (str | Unset):
        name (str | Unset):
        template (Template | Unset):
        variants (list[VariantWithRelations] | Unset):
    """

    description: str | Unset = UNSET
    name: str | Unset = UNSET
    template: Template | Unset = UNSET
    variants: list[VariantWithRelations] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        name = self.name

        template: dict[str, Any] | Unset = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.to_dict()

        variants: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.variants, Unset):
            variants = []
            for variants_item_data in self.variants:
                variants_item = variants_item_data.to_dict()
                variants.append(variants_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if template is not UNSET:
            field_dict["template"] = template
        if variants is not UNSET:
            field_dict["variants"] = variants

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template import Template
        from ..models.variant_with_relations import VariantWithRelations

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        _template = d.pop("template", UNSET)
        template: Template | Unset
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = Template.from_dict(_template)

        _variants = d.pop("variants", UNSET)
        variants: list[VariantWithRelations] | Unset = UNSET
        if _variants is not UNSET:
            variants = []
            for variants_item_data in _variants:
                variants_item = VariantWithRelations.from_dict(variants_item_data)

                variants.append(variants_item)

        template_with_variants = cls(
            description=description,
            name=name,
            template=template,
            variants=variants,
        )

        template_with_variants.additional_properties = d
        return template_with_variants

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
