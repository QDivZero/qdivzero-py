from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.serving_provider_response import ServingProviderResponse
    from ..models.serving_target_response import ServingTargetResponse


T = TypeVar("T", bound="ServingEndpointResponse")


@_attrs_define
class ServingEndpointResponse:
    """
    Attributes:
        created_at (str | Unset):
        display_name (str | Unset):
        enabled (bool | Unset):
        endpoint_type (str | Unset):
        id (str | Unset):
        model_ids (list[str] | Unset):
        name (str | Unset):
        providers (list[ServingProviderResponse] | Unset):
        public_audio_per_hour_eur (float | Unset):
        public_input_per_million_eur (float | Unset):
        public_output_per_million_eur (float | Unset):
        realtime_mode (str | Unset):
        realtime_profile (str | Unset):
        state (str | Unset):
        supported_protocols (list[str] | Unset):
        supports_duplex (bool | Unset):
        supports_realtime (bool | Unset):
        supports_server_vad (bool | Unset):
        supports_thinking (bool | Unset):
        targets (list[ServingTargetResponse] | Unset):
        updated_at (str | Unset):
        workload_kind (str | Unset):
    """

    created_at: str | Unset = UNSET
    display_name: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    endpoint_type: str | Unset = UNSET
    id: str | Unset = UNSET
    model_ids: list[str] | Unset = UNSET
    name: str | Unset = UNSET
    providers: list[ServingProviderResponse] | Unset = UNSET
    public_audio_per_hour_eur: float | Unset = UNSET
    public_input_per_million_eur: float | Unset = UNSET
    public_output_per_million_eur: float | Unset = UNSET
    realtime_mode: str | Unset = UNSET
    realtime_profile: str | Unset = UNSET
    state: str | Unset = UNSET
    supported_protocols: list[str] | Unset = UNSET
    supports_duplex: bool | Unset = UNSET
    supports_realtime: bool | Unset = UNSET
    supports_server_vad: bool | Unset = UNSET
    supports_thinking: bool | Unset = UNSET
    targets: list[ServingTargetResponse] | Unset = UNSET
    updated_at: str | Unset = UNSET
    workload_kind: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        display_name = self.display_name

        enabled = self.enabled

        endpoint_type = self.endpoint_type

        id = self.id

        model_ids: list[str] | Unset = UNSET
        if not isinstance(self.model_ids, Unset):
            model_ids = self.model_ids

        name = self.name

        providers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.providers, Unset):
            providers = []
            for providers_item_data in self.providers:
                providers_item = providers_item_data.to_dict()
                providers.append(providers_item)

        public_audio_per_hour_eur = self.public_audio_per_hour_eur

        public_input_per_million_eur = self.public_input_per_million_eur

        public_output_per_million_eur = self.public_output_per_million_eur

        realtime_mode = self.realtime_mode

        realtime_profile = self.realtime_profile

        state = self.state

        supported_protocols: list[str] | Unset = UNSET
        if not isinstance(self.supported_protocols, Unset):
            supported_protocols = self.supported_protocols

        supports_duplex = self.supports_duplex

        supports_realtime = self.supports_realtime

        supports_server_vad = self.supports_server_vad

        supports_thinking = self.supports_thinking

        targets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.targets, Unset):
            targets = []
            for targets_item_data in self.targets:
                targets_item = targets_item_data.to_dict()
                targets.append(targets_item)

        updated_at = self.updated_at

        workload_kind = self.workload_kind

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if endpoint_type is not UNSET:
            field_dict["endpoint_type"] = endpoint_type
        if id is not UNSET:
            field_dict["id"] = id
        if model_ids is not UNSET:
            field_dict["model_ids"] = model_ids
        if name is not UNSET:
            field_dict["name"] = name
        if providers is not UNSET:
            field_dict["providers"] = providers
        if public_audio_per_hour_eur is not UNSET:
            field_dict["public_audio_per_hour_eur"] = public_audio_per_hour_eur
        if public_input_per_million_eur is not UNSET:
            field_dict["public_input_per_million_eur"] = public_input_per_million_eur
        if public_output_per_million_eur is not UNSET:
            field_dict["public_output_per_million_eur"] = public_output_per_million_eur
        if realtime_mode is not UNSET:
            field_dict["realtime_mode"] = realtime_mode
        if realtime_profile is not UNSET:
            field_dict["realtime_profile"] = realtime_profile
        if state is not UNSET:
            field_dict["state"] = state
        if supported_protocols is not UNSET:
            field_dict["supported_protocols"] = supported_protocols
        if supports_duplex is not UNSET:
            field_dict["supports_duplex"] = supports_duplex
        if supports_realtime is not UNSET:
            field_dict["supports_realtime"] = supports_realtime
        if supports_server_vad is not UNSET:
            field_dict["supports_server_vad"] = supports_server_vad
        if supports_thinking is not UNSET:
            field_dict["supports_thinking"] = supports_thinking
        if targets is not UNSET:
            field_dict["targets"] = targets
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if workload_kind is not UNSET:
            field_dict["workload_kind"] = workload_kind

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.serving_provider_response import ServingProviderResponse
        from ..models.serving_target_response import ServingTargetResponse

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        display_name = d.pop("display_name", UNSET)

        enabled = d.pop("enabled", UNSET)

        endpoint_type = d.pop("endpoint_type", UNSET)

        id = d.pop("id", UNSET)

        model_ids = cast(list[str], d.pop("model_ids", UNSET))

        name = d.pop("name", UNSET)

        _providers = d.pop("providers", UNSET)
        providers: list[ServingProviderResponse] | Unset = UNSET
        if _providers is not UNSET:
            providers = []
            for providers_item_data in _providers:
                providers_item = ServingProviderResponse.from_dict(providers_item_data)

                providers.append(providers_item)

        public_audio_per_hour_eur = d.pop("public_audio_per_hour_eur", UNSET)

        public_input_per_million_eur = d.pop("public_input_per_million_eur", UNSET)

        public_output_per_million_eur = d.pop("public_output_per_million_eur", UNSET)

        realtime_mode = d.pop("realtime_mode", UNSET)

        realtime_profile = d.pop("realtime_profile", UNSET)

        state = d.pop("state", UNSET)

        supported_protocols = cast(list[str], d.pop("supported_protocols", UNSET))

        supports_duplex = d.pop("supports_duplex", UNSET)

        supports_realtime = d.pop("supports_realtime", UNSET)

        supports_server_vad = d.pop("supports_server_vad", UNSET)

        supports_thinking = d.pop("supports_thinking", UNSET)

        _targets = d.pop("targets", UNSET)
        targets: list[ServingTargetResponse] | Unset = UNSET
        if _targets is not UNSET:
            targets = []
            for targets_item_data in _targets:
                targets_item = ServingTargetResponse.from_dict(targets_item_data)

                targets.append(targets_item)

        updated_at = d.pop("updated_at", UNSET)

        workload_kind = d.pop("workload_kind", UNSET)

        serving_endpoint_response = cls(
            created_at=created_at,
            display_name=display_name,
            enabled=enabled,
            endpoint_type=endpoint_type,
            id=id,
            model_ids=model_ids,
            name=name,
            providers=providers,
            public_audio_per_hour_eur=public_audio_per_hour_eur,
            public_input_per_million_eur=public_input_per_million_eur,
            public_output_per_million_eur=public_output_per_million_eur,
            realtime_mode=realtime_mode,
            realtime_profile=realtime_profile,
            state=state,
            supported_protocols=supported_protocols,
            supports_duplex=supports_duplex,
            supports_realtime=supports_realtime,
            supports_server_vad=supports_server_vad,
            supports_thinking=supports_thinking,
            targets=targets,
            updated_at=updated_at,
            workload_kind=workload_kind,
        )

        serving_endpoint_response.additional_properties = d
        return serving_endpoint_response

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
