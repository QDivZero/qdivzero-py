from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.chat_tool_call_function_envelope import ChatToolCallFunctionEnvelope





T = TypeVar("T", bound="ChatToolCallEnvelope")



@_attrs_define
class ChatToolCallEnvelope:
    """ 
        Attributes:
            function (ChatToolCallFunctionEnvelope | Unset):
            id (str | Unset):
            index (int | Unset):
            type_ (str | Unset):
     """

    function: ChatToolCallFunctionEnvelope | Unset = UNSET
    id: str | Unset = UNSET
    index: int | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        function: dict[str, Any] | Unset = UNSET
        if not isinstance(self.function, Unset):
            function = self.function.to_dict()

        id = self.id

        index = self.index

        type_ = self.type_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if function is not UNSET:
            field_dict["function"] = function
        if id is not UNSET:
            field_dict["id"] = id
        if index is not UNSET:
            field_dict["index"] = index
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_tool_call_function_envelope import ChatToolCallFunctionEnvelope
        d = dict(src_dict)
        _function = d.pop("function", UNSET)
        function: ChatToolCallFunctionEnvelope | Unset
        if isinstance(_function,  Unset):
            function = UNSET
        else:
            function = ChatToolCallFunctionEnvelope.from_dict(_function)




        id = d.pop("id", UNSET)

        index = d.pop("index", UNSET)

        type_ = d.pop("type", UNSET)

        chat_tool_call_envelope = cls(
            function=function,
            id=id,
            index=index,
            type_=type_,
        )


        chat_tool_call_envelope.additional_properties = d
        return chat_tool_call_envelope

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
