from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execution_forecast_prediction import ExecutionForecastPrediction


T = TypeVar("T", bound="ExecutionForecastResponse")


@_attrs_define
class ExecutionForecastResponse:
    """
    Attributes:
        horizon (int | Unset):
        model (str | Unset):
        predictions (list[ExecutionForecastPrediction] | Unset):
        quantile_levels (list[float] | Unset):
    """

    horizon: int | Unset = UNSET
    model: str | Unset = UNSET
    predictions: list[ExecutionForecastPrediction] | Unset = UNSET
    quantile_levels: list[float] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        horizon = self.horizon

        model = self.model

        predictions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.predictions, Unset):
            predictions = []
            for predictions_item_data in self.predictions:
                predictions_item = predictions_item_data.to_dict()
                predictions.append(predictions_item)

        quantile_levels: list[float] | Unset = UNSET
        if not isinstance(self.quantile_levels, Unset):
            quantile_levels = self.quantile_levels

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if horizon is not UNSET:
            field_dict["horizon"] = horizon
        if model is not UNSET:
            field_dict["model"] = model
        if predictions is not UNSET:
            field_dict["predictions"] = predictions
        if quantile_levels is not UNSET:
            field_dict["quantile_levels"] = quantile_levels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_forecast_prediction import ExecutionForecastPrediction

        d = dict(src_dict)
        horizon = d.pop("horizon", UNSET)

        model = d.pop("model", UNSET)

        _predictions = d.pop("predictions", UNSET)
        predictions: list[ExecutionForecastPrediction] | Unset = UNSET
        if _predictions is not UNSET:
            predictions = []
            for predictions_item_data in _predictions:
                predictions_item = ExecutionForecastPrediction.from_dict(predictions_item_data)

                predictions.append(predictions_item)

        quantile_levels = cast(list[float], d.pop("quantile_levels", UNSET))

        execution_forecast_response = cls(
            horizon=horizon,
            model=model,
            predictions=predictions,
            quantile_levels=quantile_levels,
        )

        execution_forecast_response.additional_properties = d
        return execution_forecast_response

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
