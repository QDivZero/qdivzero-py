from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecutionForecastInput")


@_attrs_define
class ExecutionForecastInput:
    """
    Attributes:
        id (str | Unset):
        past_future_covariates (list[list[float]] | Unset):
        past_only_covariates (list[list[float]] | Unset):
        target (list[list[float]] | Unset):
    """

    id: str | Unset = UNSET
    past_future_covariates: list[list[float]] | Unset = UNSET
    past_only_covariates: list[list[float]] | Unset = UNSET
    target: list[list[float]] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        past_future_covariates: list[list[float]] | Unset = UNSET
        if not isinstance(self.past_future_covariates, Unset):
            past_future_covariates = []
            for past_future_covariates_item_data in self.past_future_covariates:
                past_future_covariates_item = past_future_covariates_item_data

                past_future_covariates.append(past_future_covariates_item)

        past_only_covariates: list[list[float]] | Unset = UNSET
        if not isinstance(self.past_only_covariates, Unset):
            past_only_covariates = []
            for past_only_covariates_item_data in self.past_only_covariates:
                past_only_covariates_item = past_only_covariates_item_data

                past_only_covariates.append(past_only_covariates_item)

        target: list[list[float]] | Unset = UNSET
        if not isinstance(self.target, Unset):
            target = []
            for target_item_data in self.target:
                target_item = target_item_data

                target.append(target_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if past_future_covariates is not UNSET:
            field_dict["past_future_covariates"] = past_future_covariates
        if past_only_covariates is not UNSET:
            field_dict["past_only_covariates"] = past_only_covariates
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _past_future_covariates = d.pop("past_future_covariates", UNSET)
        past_future_covariates: list[list[float]] | Unset = UNSET
        if _past_future_covariates is not UNSET:
            past_future_covariates = []
            for past_future_covariates_item_data in _past_future_covariates:
                past_future_covariates_item = cast(list[float], past_future_covariates_item_data)

                past_future_covariates.append(past_future_covariates_item)

        _past_only_covariates = d.pop("past_only_covariates", UNSET)
        past_only_covariates: list[list[float]] | Unset = UNSET
        if _past_only_covariates is not UNSET:
            past_only_covariates = []
            for past_only_covariates_item_data in _past_only_covariates:
                past_only_covariates_item = cast(list[float], past_only_covariates_item_data)

                past_only_covariates.append(past_only_covariates_item)

        _target = d.pop("target", UNSET)
        target: list[list[float]] | Unset = UNSET
        if _target is not UNSET:
            target = []
            for target_item_data in _target:
                target_item = cast(list[float], target_item_data)

                target.append(target_item)

        execution_forecast_input = cls(
            id=id,
            past_future_covariates=past_future_covariates,
            past_only_covariates=past_only_covariates,
            target=target,
        )

        execution_forecast_input.additional_properties = d
        return execution_forecast_input

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
