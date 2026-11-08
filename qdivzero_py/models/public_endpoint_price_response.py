from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicEndpointPriceResponse")


@_attrs_define
class PublicEndpointPriceResponse:
    """
    Attributes:
        audio_per_hour_eur (float | Unset):
        input_per_million_eur (float | Unset):
        output_per_million_eur (float | Unset):
    """

    audio_per_hour_eur: float | Unset = UNSET
    input_per_million_eur: float | Unset = UNSET
    output_per_million_eur: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        audio_per_hour_eur = self.audio_per_hour_eur

        input_per_million_eur = self.input_per_million_eur

        output_per_million_eur = self.output_per_million_eur

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if audio_per_hour_eur is not UNSET:
            field_dict["audio_per_hour_eur"] = audio_per_hour_eur
        if input_per_million_eur is not UNSET:
            field_dict["input_per_million_eur"] = input_per_million_eur
        if output_per_million_eur is not UNSET:
            field_dict["output_per_million_eur"] = output_per_million_eur

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        audio_per_hour_eur = d.pop("audio_per_hour_eur", UNSET)

        input_per_million_eur = d.pop("input_per_million_eur", UNSET)

        output_per_million_eur = d.pop("output_per_million_eur", UNSET)

        public_endpoint_price_response = cls(
            audio_per_hour_eur=audio_per_hour_eur,
            input_per_million_eur=input_per_million_eur,
            output_per_million_eur=output_per_million_eur,
        )

        public_endpoint_price_response.additional_properties = d
        return public_endpoint_price_response

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
