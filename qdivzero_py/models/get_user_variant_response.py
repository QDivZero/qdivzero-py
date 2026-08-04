from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.variant_with_relations import VariantWithRelations





T = TypeVar("T", bound="GetUserVariantResponse")



@_attrs_define
class GetUserVariantResponse:
    """ 
        Attributes:
            variant (VariantWithRelations | Unset):
     """

    variant: VariantWithRelations | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        variant: dict[str, Any] | Unset = UNSET
        if not isinstance(self.variant, Unset):
            variant = self.variant.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if variant is not UNSET:
            field_dict["variant"] = variant

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.variant_with_relations import VariantWithRelations
        d = dict(src_dict)
        _variant = d.pop("variant", UNSET)
        variant: VariantWithRelations | Unset
        if isinstance(_variant,  Unset):
            variant = UNSET
        else:
            variant = VariantWithRelations.from_dict(_variant)




        get_user_variant_response = cls(
            variant=variant,
        )


        get_user_variant_response.additional_properties = d
        return get_user_variant_response

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
