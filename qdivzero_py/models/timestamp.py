from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Timestamp")


@_attrs_define
class Timestamp:
    """
    Attributes:
        nanos (int | Unset): Non-negative fractions of a second at nanosecond resolution. This field is
            the nanosecond portion of the duration, not an alternative to seconds.
            Negative second values with fractions must still have non-negative nanos
            values that count forward in time. Must be between 0 and 999,999,999
            inclusive.
        seconds (int | Unset): Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must
            be between -62135596800 and 253402300799 inclusive (which corresponds to
            0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z).
    """

    nanos: int | Unset = UNSET
    seconds: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        nanos = self.nanos

        seconds = self.seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nanos is not UNSET:
            field_dict["nanos"] = nanos
        if seconds is not UNSET:
            field_dict["seconds"] = seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        nanos = d.pop("nanos", UNSET)

        seconds = d.pop("seconds", UNSET)

        timestamp = cls(
            nanos=nanos,
            seconds=seconds,
        )

        timestamp.additional_properties = d
        return timestamp

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
