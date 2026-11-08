from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.public_token_usage_day import PublicTokenUsageDay
    from ..models.public_token_usage_total import PublicTokenUsageTotal


T = TypeVar("T", bound="PublicTokenUsageResponse")


@_attrs_define
class PublicTokenUsageResponse:
    """
    Attributes:
        as_of (str | Unset):
        days (list[PublicTokenUsageDay] | Unset):
        from_ (str | Unset):
        measured_since (str | Unset):
        period_totals (PublicTokenUsageTotal | Unset):
        timezone (str | Unset):
        to (str | Unset):
        top_models (list[str] | Unset):
        totals (PublicTokenUsageTotal | Unset):
    """

    as_of: str | Unset = UNSET
    days: list[PublicTokenUsageDay] | Unset = UNSET
    from_: str | Unset = UNSET
    measured_since: str | Unset = UNSET
    period_totals: PublicTokenUsageTotal | Unset = UNSET
    timezone: str | Unset = UNSET
    to: str | Unset = UNSET
    top_models: list[str] | Unset = UNSET
    totals: PublicTokenUsageTotal | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        as_of = self.as_of

        days: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.days, Unset):
            days = []
            for days_item_data in self.days:
                days_item = days_item_data.to_dict()
                days.append(days_item)

        from_ = self.from_

        measured_since = self.measured_since

        period_totals: dict[str, Any] | Unset = UNSET
        if not isinstance(self.period_totals, Unset):
            period_totals = self.period_totals.to_dict()

        timezone = self.timezone

        to = self.to

        top_models: list[str] | Unset = UNSET
        if not isinstance(self.top_models, Unset):
            top_models = self.top_models

        totals: dict[str, Any] | Unset = UNSET
        if not isinstance(self.totals, Unset):
            totals = self.totals.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if as_of is not UNSET:
            field_dict["as_of"] = as_of
        if days is not UNSET:
            field_dict["days"] = days
        if from_ is not UNSET:
            field_dict["from"] = from_
        if measured_since is not UNSET:
            field_dict["measured_since"] = measured_since
        if period_totals is not UNSET:
            field_dict["period_totals"] = period_totals
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if to is not UNSET:
            field_dict["to"] = to
        if top_models is not UNSET:
            field_dict["top_models"] = top_models
        if totals is not UNSET:
            field_dict["totals"] = totals

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_token_usage_day import PublicTokenUsageDay
        from ..models.public_token_usage_total import PublicTokenUsageTotal

        d = dict(src_dict)
        as_of = d.pop("as_of", UNSET)

        _days = d.pop("days", UNSET)
        days: list[PublicTokenUsageDay] | Unset = UNSET
        if _days is not UNSET:
            days = []
            for days_item_data in _days:
                days_item = PublicTokenUsageDay.from_dict(days_item_data)

                days.append(days_item)

        from_ = d.pop("from", UNSET)

        measured_since = d.pop("measured_since", UNSET)

        _period_totals = d.pop("period_totals", UNSET)
        period_totals: PublicTokenUsageTotal | Unset
        if isinstance(_period_totals, Unset):
            period_totals = UNSET
        else:
            period_totals = PublicTokenUsageTotal.from_dict(_period_totals)

        timezone = d.pop("timezone", UNSET)

        to = d.pop("to", UNSET)

        top_models = cast(list[str], d.pop("top_models", UNSET))

        _totals = d.pop("totals", UNSET)
        totals: PublicTokenUsageTotal | Unset
        if isinstance(_totals, Unset):
            totals = UNSET
        else:
            totals = PublicTokenUsageTotal.from_dict(_totals)

        public_token_usage_response = cls(
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

        public_token_usage_response.additional_properties = d
        return public_token_usage_response

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
