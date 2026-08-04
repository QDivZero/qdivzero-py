from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.system_tool_output_configuration_schema import SystemToolOutputConfigurationSchema





T = TypeVar("T", bound="SystemToolOutput")



@_attrs_define
class SystemToolOutput:
    """ 
        Attributes:
            configuration_schema (SystemToolOutputConfigurationSchema | Unset):
            description (str | Unset):
            managed_by (str | Unset):
            type_ (str | Unset):
            visibility (str | Unset):
     """

    configuration_schema: SystemToolOutputConfigurationSchema | Unset = UNSET
    description: str | Unset = UNSET
    managed_by: str | Unset = UNSET
    type_: str | Unset = UNSET
    visibility: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        configuration_schema: dict[str, Any] | Unset = UNSET
        if not isinstance(self.configuration_schema, Unset):
            configuration_schema = self.configuration_schema.to_dict()

        description = self.description

        managed_by = self.managed_by

        type_ = self.type_

        visibility = self.visibility


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if configuration_schema is not UNSET:
            field_dict["configuration_schema"] = configuration_schema
        if description is not UNSET:
            field_dict["description"] = description
        if managed_by is not UNSET:
            field_dict["managed_by"] = managed_by
        if type_ is not UNSET:
            field_dict["type"] = type_
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.system_tool_output_configuration_schema import SystemToolOutputConfigurationSchema
        d = dict(src_dict)
        _configuration_schema = d.pop("configuration_schema", UNSET)
        configuration_schema: SystemToolOutputConfigurationSchema | Unset
        if isinstance(_configuration_schema,  Unset):
            configuration_schema = UNSET
        else:
            configuration_schema = SystemToolOutputConfigurationSchema.from_dict(_configuration_schema)




        description = d.pop("description", UNSET)

        managed_by = d.pop("managed_by", UNSET)

        type_ = d.pop("type", UNSET)

        visibility = d.pop("visibility", UNSET)

        system_tool_output = cls(
            configuration_schema=configuration_schema,
            description=description,
            managed_by=managed_by,
            type_=type_,
            visibility=visibility,
        )


        system_tool_output.additional_properties = d
        return system_tool_output

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
