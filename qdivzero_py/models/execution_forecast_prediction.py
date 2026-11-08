from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecutionForecastPrediction")


@_attrs_define
class ExecutionForecastPrediction:
    """
    Attributes:
        forecast (list[list[float]] | Unset):
        id (str | Unset):
        quantiles (list[list[list[float]]] | Unset):
    """

    forecast: list[list[float]] | Unset = UNSET
    id: str | Unset = UNSET
    quantiles: list[list[list[float]]] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        forecast: list[list[float]] | Unset = UNSET
        if not isinstance(self.forecast, Unset):
            forecast = []
            for forecast_item_data in self.forecast:
                forecast_item = forecast_item_data

                forecast.append(forecast_item)

        id = self.id

        quantiles: list[list[list[float]]] | Unset = UNSET
        if not isinstance(self.quantiles, Unset):
            quantiles = []
            for quantiles_item_data in self.quantiles:
                quantiles_item = []
                for quantiles_item_item_data in quantiles_item_data:
                    quantiles_item_item = quantiles_item_item_data

                    quantiles_item.append(quantiles_item_item)

                quantiles.append(quantiles_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if forecast is not UNSET:
            field_dict["forecast"] = forecast
        if id is not UNSET:
            field_dict["id"] = id
        if quantiles is not UNSET:
            field_dict["quantiles"] = quantiles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _forecast = d.pop("forecast", UNSET)
        forecast: list[list[float]] | Unset = UNSET
        if _forecast is not UNSET:
            forecast = []
            for forecast_item_data in _forecast:
                forecast_item = cast(list[float], forecast_item_data)

                forecast.append(forecast_item)

        id = d.pop("id", UNSET)

        _quantiles = d.pop("quantiles", UNSET)
        quantiles: list[list[list[float]]] | Unset = UNSET
        if _quantiles is not UNSET:
            quantiles = []
            for quantiles_item_data in _quantiles:
                quantiles_item = []
                _quantiles_item = quantiles_item_data
                for quantiles_item_item_data in _quantiles_item:
                    quantiles_item_item = cast(list[float], quantiles_item_item_data)

                    quantiles_item.append(quantiles_item_item)

                quantiles.append(quantiles_item)

        execution_forecast_prediction = cls(
            forecast=forecast,
            id=id,
            quantiles=quantiles,
        )

        execution_forecast_prediction.additional_properties = d
        return execution_forecast_prediction

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
