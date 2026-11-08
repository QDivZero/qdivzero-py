from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model import Model
    from ..models.pricing_service import PricingService


T = TypeVar("T", bound="ModelPricesResponse")


@_attrs_define
class ModelPricesResponse:
    """
    Attributes:
        models (list[Model] | Unset):
        query (str | Unset):
        services (list[PricingService] | Unset):
        source (str | Unset):
        source_status (str | Unset):
        stale (bool | Unset):
        updated_at (str | Unset):
        version (int | Unset):
    """

    models: list[Model] | Unset = UNSET
    query: str | Unset = UNSET
    services: list[PricingService] | Unset = UNSET
    source: str | Unset = UNSET
    source_status: str | Unset = UNSET
    stale: bool | Unset = UNSET
    updated_at: str | Unset = UNSET
    version: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        models: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.models, Unset):
            models = []
            for models_item_data in self.models:
                models_item = models_item_data.to_dict()
                models.append(models_item)

        query = self.query

        services: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.services, Unset):
            services = []
            for services_item_data in self.services:
                services_item = services_item_data.to_dict()
                services.append(services_item)

        source = self.source

        source_status = self.source_status

        stale = self.stale

        updated_at = self.updated_at

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if models is not UNSET:
            field_dict["models"] = models
        if query is not UNSET:
            field_dict["query"] = query
        if services is not UNSET:
            field_dict["services"] = services
        if source is not UNSET:
            field_dict["source"] = source
        if source_status is not UNSET:
            field_dict["source_status"] = source_status
        if stale is not UNSET:
            field_dict["stale"] = stale
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model import Model
        from ..models.pricing_service import PricingService

        d = dict(src_dict)
        _models = d.pop("models", UNSET)
        models: list[Model] | Unset = UNSET
        if _models is not UNSET:
            models = []
            for models_item_data in _models:
                models_item = Model.from_dict(models_item_data)

                models.append(models_item)

        query = d.pop("query", UNSET)

        _services = d.pop("services", UNSET)
        services: list[PricingService] | Unset = UNSET
        if _services is not UNSET:
            services = []
            for services_item_data in _services:
                services_item = PricingService.from_dict(services_item_data)

                services.append(services_item)

        source = d.pop("source", UNSET)

        source_status = d.pop("source_status", UNSET)

        stale = d.pop("stale", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        version = d.pop("version", UNSET)

        model_prices_response = cls(
            models=models,
            query=query,
            services=services,
            source=source,
            source_status=source_status,
            stale=stale,
            updated_at=updated_at,
            version=version,
        )

        model_prices_response.additional_properties = d
        return model_prices_response

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
