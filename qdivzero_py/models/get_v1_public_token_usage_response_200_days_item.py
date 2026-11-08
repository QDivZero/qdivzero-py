from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetV1PublicTokenUsageResponse200DaysItem")


@_attrs_define
class GetV1PublicTokenUsageResponse200DaysItem:
    """
    Attributes:
        date (datetime.date):
        total_tokens (int):
    """

    date: datetime.date
    total_tokens: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date.isoformat()

        total_tokens = self.total_tokens

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "total_tokens": total_tokens,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = datetime.date.fromisoformat(d.pop("date"))

        total_tokens = d.pop("total_tokens")

        get_v1_public_token_usage_response_200_days_item = cls(
            date=date,
            total_tokens=total_tokens,
        )

        get_v1_public_token_usage_response_200_days_item.additional_properties = d
        return get_v1_public_token_usage_response_200_days_item

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
