from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_key_response import ApiKeyResponse


T = TypeVar("T", bound="ApiKeyListResponse")


@_attrs_define
class ApiKeyListResponse:
    """
    Attributes:
        api_keys (list[ApiKeyResponse] | Unset):
    """

    api_keys: list[ApiKeyResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_keys: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.api_keys, Unset):
            api_keys = []
            for api_keys_item_data in self.api_keys:
                api_keys_item = api_keys_item_data.to_dict()
                api_keys.append(api_keys_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_keys is not UNSET:
            field_dict["api_keys"] = api_keys

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_key_response import ApiKeyResponse

        d = dict(src_dict)
        _api_keys = d.pop("api_keys", UNSET)
        api_keys: list[ApiKeyResponse] | Unset = UNSET
        if _api_keys is not UNSET:
            api_keys = []
            for api_keys_item_data in _api_keys:
                api_keys_item = ApiKeyResponse.from_dict(api_keys_item_data)

                api_keys.append(api_keys_item)

        api_key_list_response = cls(
            api_keys=api_keys,
        )

        api_key_list_response.additional_properties = d
        return api_key_list_response

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
