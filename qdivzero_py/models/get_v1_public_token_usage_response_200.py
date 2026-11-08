from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_v1_public_token_usage_response_200_days_item import GetV1PublicTokenUsageResponse200DaysItem
    from ..models.get_v1_public_token_usage_response_200_period_totals import (
        GetV1PublicTokenUsageResponse200PeriodTotals,
    )
    from ..models.get_v1_public_token_usage_response_200_totals import GetV1PublicTokenUsageResponse200Totals


T = TypeVar("T", bound="GetV1PublicTokenUsageResponse200")


@_attrs_define
class GetV1PublicTokenUsageResponse200:
    """
    Attributes:
        as_of (datetime.datetime):
        days (list[GetV1PublicTokenUsageResponse200DaysItem]):
        from_ (datetime.date):
        measured_since (datetime.datetime | None):
        period_totals (GetV1PublicTokenUsageResponse200PeriodTotals):
        timezone (str):  Example: Europe/Madrid.
        to (datetime.date):
        top_models (list[str]): Up to ten canonical public model names, ordered by total recorded tokens in the selected
            period (ties by name); no per-model quantities
        totals (GetV1PublicTokenUsageResponse200Totals):
    """

    as_of: datetime.datetime
    days: list[GetV1PublicTokenUsageResponse200DaysItem]
    from_: datetime.date
    measured_since: datetime.datetime | None
    period_totals: GetV1PublicTokenUsageResponse200PeriodTotals
    timezone: str
    to: datetime.date
    top_models: list[str]
    totals: GetV1PublicTokenUsageResponse200Totals
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        as_of = self.as_of.isoformat()

        days = []
        for days_item_data in self.days:
            days_item = days_item_data.to_dict()
            days.append(days_item)

        from_ = self.from_.isoformat()

        measured_since: None | str
        if isinstance(self.measured_since, datetime.datetime):
            measured_since = self.measured_since.isoformat()
        else:
            measured_since = self.measured_since

        period_totals = self.period_totals.to_dict()

        timezone = self.timezone

        to = self.to.isoformat()

        top_models = self.top_models

        totals = self.totals.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "as_of": as_of,
                "days": days,
                "from": from_,
                "measured_since": measured_since,
                "period_totals": period_totals,
                "timezone": timezone,
                "to": to,
                "top_models": top_models,
                "totals": totals,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v1_public_token_usage_response_200_days_item import GetV1PublicTokenUsageResponse200DaysItem
        from ..models.get_v1_public_token_usage_response_200_period_totals import (
            GetV1PublicTokenUsageResponse200PeriodTotals,
        )
        from ..models.get_v1_public_token_usage_response_200_totals import GetV1PublicTokenUsageResponse200Totals

        d = dict(src_dict)
        as_of = datetime.datetime.fromisoformat(d.pop("as_of"))

        days = []
        _days = d.pop("days")
        for days_item_data in _days:
            days_item = GetV1PublicTokenUsageResponse200DaysItem.from_dict(days_item_data)

            days.append(days_item)

        from_ = datetime.date.fromisoformat(d.pop("from"))

        def _parse_measured_since(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                measured_since_type_0 = datetime.datetime.fromisoformat(data)

                return measured_since_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        measured_since = _parse_measured_since(d.pop("measured_since"))

        period_totals = GetV1PublicTokenUsageResponse200PeriodTotals.from_dict(d.pop("period_totals"))

        timezone = d.pop("timezone")

        to = datetime.date.fromisoformat(d.pop("to"))

        top_models = cast(list[str], d.pop("top_models"))

        totals = GetV1PublicTokenUsageResponse200Totals.from_dict(d.pop("totals"))

        get_v1_public_token_usage_response_200 = cls(
            as_of=as_of,
            days=days,
            from_=from_,
            measured_since=measured_since,
            period_totals=period_totals,
            timezone=timezone,
            to=to,
            top_models=top_models,
            totals=totals,
        )

        get_v1_public_token_usage_response_200.additional_properties = d
        return get_v1_public_token_usage_response_200

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
