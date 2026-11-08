from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.template_with_variants import TemplateWithVariants


T = TypeVar("T", bound="GetTemplateBySlugResponse")


@_attrs_define
class GetTemplateBySlugResponse:
    """
    Attributes:
        template (TemplateWithVariants | Unset):
    """

    template: TemplateWithVariants | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        template: dict[str, Any] | Unset = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if template is not UNSET:
            field_dict["template"] = template

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template_with_variants import TemplateWithVariants

        d = dict(src_dict)
        _template = d.pop("template", UNSET)
        template: TemplateWithVariants | Unset
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = TemplateWithVariants.from_dict(_template)

        get_template_by_slug_response = cls(
            template=template,
        )

        get_template_by_slug_response.additional_properties = d
        return get_template_by_slug_response

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
