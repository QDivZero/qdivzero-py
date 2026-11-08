from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.instance_usage_bucket_response import InstanceUsageBucketResponse
    from ..models.instance_usage_summary_response import InstanceUsageSummaryResponse
    from ..models.resource_metrics_response import ResourceMetricsResponse


T = TypeVar("T", bound="InstanceUsageResponse")


@_attrs_define
class InstanceUsageResponse:
    """
    Attributes:
        bucket_unit (str | Unset):
        range_ (str | Unset):
        resource_metrics (ResourceMetricsResponse | Unset):
        series (list[InstanceUsageBucketResponse] | Unset):
        summary (InstanceUsageSummaryResponse | Unset):
    """

    bucket_unit: str | Unset = UNSET
    range_: str | Unset = UNSET
    resource_metrics: ResourceMetricsResponse | Unset = UNSET
    series: list[InstanceUsageBucketResponse] | Unset = UNSET
    summary: InstanceUsageSummaryResponse | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket_unit = self.bucket_unit

        range_ = self.range_

        resource_metrics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resource_metrics, Unset):
            resource_metrics = self.resource_metrics.to_dict()

        series: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.series, Unset):
            series = []
            for series_item_data in self.series:
                series_item = series_item_data.to_dict()
                series.append(series_item)

        summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.summary, Unset):
            summary = self.summary.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bucket_unit is not UNSET:
            field_dict["bucket_unit"] = bucket_unit
        if range_ is not UNSET:
            field_dict["range"] = range_
        if resource_metrics is not UNSET:
            field_dict["resource_metrics"] = resource_metrics
        if series is not UNSET:
            field_dict["series"] = series
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.instance_usage_bucket_response import InstanceUsageBucketResponse
        from ..models.instance_usage_summary_response import InstanceUsageSummaryResponse
        from ..models.resource_metrics_response import ResourceMetricsResponse

        d = dict(src_dict)
        bucket_unit = d.pop("bucket_unit", UNSET)

        range_ = d.pop("range", UNSET)

        _resource_metrics = d.pop("resource_metrics", UNSET)
        resource_metrics: ResourceMetricsResponse | Unset
        if isinstance(_resource_metrics, Unset):
            resource_metrics = UNSET
        else:
            resource_metrics = ResourceMetricsResponse.from_dict(_resource_metrics)

        _series = d.pop("series", UNSET)
        series: list[InstanceUsageBucketResponse] | Unset = UNSET
        if _series is not UNSET:
            series = []
            for series_item_data in _series:
                series_item = InstanceUsageBucketResponse.from_dict(series_item_data)

                series.append(series_item)

        _summary = d.pop("summary", UNSET)
        summary: InstanceUsageSummaryResponse | Unset
        if isinstance(_summary, Unset):
            summary = UNSET
        else:
            summary = InstanceUsageSummaryResponse.from_dict(_summary)

        instance_usage_response = cls(
            bucket_unit=bucket_unit,
            range_=range_,
            resource_metrics=resource_metrics,
            series=series,
            summary=summary,
        )

        instance_usage_response.additional_properties = d
        return instance_usage_response

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
