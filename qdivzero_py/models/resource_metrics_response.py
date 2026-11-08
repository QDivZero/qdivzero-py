from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resource_metric_snapshot import ResourceMetricSnapshot


T = TypeVar("T", bound="ResourceMetricsResponse")


@_attrs_define
class ResourceMetricsResponse:
    """
    Attributes:
        latest (ResourceMetricSnapshot | Unset):
        retention_seconds (int | Unset):
        sample_interval_seconds (int | Unset):
        series (list[ResourceMetricSnapshot] | Unset):
    """

    latest: ResourceMetricSnapshot | Unset = UNSET
    retention_seconds: int | Unset = UNSET
    sample_interval_seconds: int | Unset = UNSET
    series: list[ResourceMetricSnapshot] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        latest: dict[str, Any] | Unset = UNSET
        if not isinstance(self.latest, Unset):
            latest = self.latest.to_dict()

        retention_seconds = self.retention_seconds

        sample_interval_seconds = self.sample_interval_seconds

        series: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.series, Unset):
            series = []
            for series_item_data in self.series:
                series_item = series_item_data.to_dict()
                series.append(series_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if latest is not UNSET:
            field_dict["latest"] = latest
        if retention_seconds is not UNSET:
            field_dict["retention_seconds"] = retention_seconds
        if sample_interval_seconds is not UNSET:
            field_dict["sample_interval_seconds"] = sample_interval_seconds
        if series is not UNSET:
            field_dict["series"] = series

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_metric_snapshot import ResourceMetricSnapshot

        d = dict(src_dict)
        _latest = d.pop("latest", UNSET)
        latest: ResourceMetricSnapshot | Unset
        if isinstance(_latest, Unset):
            latest = UNSET
        else:
            latest = ResourceMetricSnapshot.from_dict(_latest)

        retention_seconds = d.pop("retention_seconds", UNSET)

        sample_interval_seconds = d.pop("sample_interval_seconds", UNSET)

        _series = d.pop("series", UNSET)
        series: list[ResourceMetricSnapshot] | Unset = UNSET
        if _series is not UNSET:
            series = []
            for series_item_data in _series:
                series_item = ResourceMetricSnapshot.from_dict(series_item_data)

                series.append(series_item)

        resource_metrics_response = cls(
            latest=latest,
            retention_seconds=retention_seconds,
            sample_interval_seconds=sample_interval_seconds,
            series=series,
        )

        resource_metrics_response.additional_properties = d
        return resource_metrics_response

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
