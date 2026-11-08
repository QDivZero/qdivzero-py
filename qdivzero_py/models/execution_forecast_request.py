from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execution_forecast_input import ExecutionForecastInput


T = TypeVar("T", bound="ExecutionForecastRequest")


@_attrs_define
class ExecutionForecastRequest:
    """
    Attributes:
        horizon (int):
        inputs (list[ExecutionForecastInput]):
        model (str):
        return_quantiles (bool | Unset):
        use_symmetric_averaging (bool | Unset):
    """

    horizon: int
    inputs: list[ExecutionForecastInput]
    model: str
    return_quantiles: bool | Unset = UNSET
    use_symmetric_averaging: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        horizon = self.horizon

        inputs = []
        for inputs_item_data in self.inputs:
            inputs_item = inputs_item_data.to_dict()
            inputs.append(inputs_item)

        model = self.model

        return_quantiles = self.return_quantiles

        use_symmetric_averaging = self.use_symmetric_averaging

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "horizon": horizon,
                "inputs": inputs,
                "model": model,
            }
        )
        if return_quantiles is not UNSET:
            field_dict["return_quantiles"] = return_quantiles
        if use_symmetric_averaging is not UNSET:
            field_dict["use_symmetric_averaging"] = use_symmetric_averaging

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_forecast_input import ExecutionForecastInput

        d = dict(src_dict)
        horizon = d.pop("horizon")

        inputs = []
        _inputs = d.pop("inputs")
        for inputs_item_data in _inputs:
            inputs_item = ExecutionForecastInput.from_dict(inputs_item_data)

            inputs.append(inputs_item)

        model = d.pop("model")

        return_quantiles = d.pop("return_quantiles", UNSET)

        use_symmetric_averaging = d.pop("use_symmetric_averaging", UNSET)

        execution_forecast_request = cls(
            horizon=horizon,
            inputs=inputs,
            model=model,
            return_quantiles=return_quantiles,
            use_symmetric_averaging=use_symmetric_averaging,
        )

        execution_forecast_request.additional_properties = d
        return execution_forecast_request

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
