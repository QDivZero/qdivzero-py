from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.unread_count_response_by_severity import UnreadCountResponseBySeverity


T = TypeVar("T", bound="UnreadCountResponse")


@_attrs_define
class UnreadCountResponse:
    """
    Attributes:
        by_severity (UnreadCountResponseBySeverity | Unset):
        count (int | Unset):
    """

    by_severity: UnreadCountResponseBySeverity | Unset = UNSET
    count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        by_severity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.by_severity, Unset):
            by_severity = self.by_severity.to_dict()

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if by_severity is not UNSET:
            field_dict["by_severity"] = by_severity
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.unread_count_response_by_severity import UnreadCountResponseBySeverity

        d = dict(src_dict)
        _by_severity = d.pop("by_severity", UNSET)
        by_severity: UnreadCountResponseBySeverity | Unset
        if isinstance(_by_severity, Unset):
            by_severity = UNSET
        else:
            by_severity = UnreadCountResponseBySeverity.from_dict(_by_severity)

        count = d.pop("count", UNSET)

        unread_count_response = cls(
            by_severity=by_severity,
            count=count,
        )

        unread_count_response.additional_properties = d
        return unread_count_response

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
