from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.timestamp import Timestamp
    from ..models.variant_translation import VariantTranslation


T = TypeVar("T", bound="Variant")


@_attrs_define
class Variant:
    """
    Attributes:
        artifact_type (str | Unset):
        created_at (Timestamp | Unset):
        gguf_files (list[str] | Unset):
        health_checked_at (Timestamp | Unset):
        health_error (str | Unset):
        health_status (str | Unset):
        icon_url (str | Unset):
        id (str | Unset):
        is_active (bool | Unset):
        max_context_tokens (int | Unset):
        model_id (str | Unset):
        ordering (int | Unset):
        quantization (str | Unset):
        recommended_preset (str | Unset):
        revision (str | Unset):
        stop_sequences (list[str] | Unset):
        system_prompt (str | Unset):
        temperature (float | Unset):
        template_id (str | Unset):
        translations (list[VariantTranslation] | Unset):
        updated_at (Timestamp | Unset):
    """

    artifact_type: str | Unset = UNSET
    created_at: Timestamp | Unset = UNSET
    gguf_files: list[str] | Unset = UNSET
    health_checked_at: Timestamp | Unset = UNSET
    health_error: str | Unset = UNSET
    health_status: str | Unset = UNSET
    icon_url: str | Unset = UNSET
    id: str | Unset = UNSET
    is_active: bool | Unset = UNSET
    max_context_tokens: int | Unset = UNSET
    model_id: str | Unset = UNSET
    ordering: int | Unset = UNSET
    quantization: str | Unset = UNSET
    recommended_preset: str | Unset = UNSET
    revision: str | Unset = UNSET
    stop_sequences: list[str] | Unset = UNSET
    system_prompt: str | Unset = UNSET
    temperature: float | Unset = UNSET
    template_id: str | Unset = UNSET
    translations: list[VariantTranslation] | Unset = UNSET
    updated_at: Timestamp | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        artifact_type = self.artifact_type

        created_at: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.to_dict()

        gguf_files: list[str] | Unset = UNSET
        if not isinstance(self.gguf_files, Unset):
            gguf_files = self.gguf_files

        health_checked_at: dict[str, Any] | Unset = UNSET
        if not isinstance(self.health_checked_at, Unset):
            health_checked_at = self.health_checked_at.to_dict()

        health_error = self.health_error

        health_status = self.health_status

        icon_url = self.icon_url

        id = self.id

        is_active = self.is_active

        max_context_tokens = self.max_context_tokens

        model_id = self.model_id

        ordering = self.ordering

        quantization = self.quantization

        recommended_preset = self.recommended_preset

        revision = self.revision

        stop_sequences: list[str] | Unset = UNSET
        if not isinstance(self.stop_sequences, Unset):
            stop_sequences = self.stop_sequences

        system_prompt = self.system_prompt

        temperature = self.temperature

        template_id = self.template_id

        translations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.translations, Unset):
            translations = []
            for translations_item_data in self.translations:
                translations_item = translations_item_data.to_dict()
                translations.append(translations_item)

        updated_at: dict[str, Any] | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if artifact_type is not UNSET:
            field_dict["artifact_type"] = artifact_type
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if gguf_files is not UNSET:
            field_dict["gguf_files"] = gguf_files
        if health_checked_at is not UNSET:
            field_dict["health_checked_at"] = health_checked_at
        if health_error is not UNSET:
            field_dict["health_error"] = health_error
        if health_status is not UNSET:
            field_dict["health_status"] = health_status
        if icon_url is not UNSET:
            field_dict["icon_url"] = icon_url
        if id is not UNSET:
            field_dict["id"] = id
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if max_context_tokens is not UNSET:
            field_dict["max_context_tokens"] = max_context_tokens
        if model_id is not UNSET:
            field_dict["model_id"] = model_id
        if ordering is not UNSET:
            field_dict["ordering"] = ordering
        if quantization is not UNSET:
            field_dict["quantization"] = quantization
        if recommended_preset is not UNSET:
            field_dict["recommended_preset"] = recommended_preset
        if revision is not UNSET:
            field_dict["revision"] = revision
        if stop_sequences is not UNSET:
            field_dict["stop_sequences"] = stop_sequences
        if system_prompt is not UNSET:
            field_dict["system_prompt"] = system_prompt
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if template_id is not UNSET:
            field_dict["template_id"] = template_id
        if translations is not UNSET:
            field_dict["translations"] = translations
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.timestamp import Timestamp
        from ..models.variant_translation import VariantTranslation

        d = dict(src_dict)
        artifact_type = d.pop("artifact_type", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Timestamp | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = Timestamp.from_dict(_created_at)

        gguf_files = cast(list[str], d.pop("gguf_files", UNSET))

        _health_checked_at = d.pop("health_checked_at", UNSET)
        health_checked_at: Timestamp | Unset
        if isinstance(_health_checked_at, Unset):
            health_checked_at = UNSET
        else:
            health_checked_at = Timestamp.from_dict(_health_checked_at)

        health_error = d.pop("health_error", UNSET)

        health_status = d.pop("health_status", UNSET)

        icon_url = d.pop("icon_url", UNSET)

        id = d.pop("id", UNSET)

        is_active = d.pop("is_active", UNSET)

        max_context_tokens = d.pop("max_context_tokens", UNSET)

        model_id = d.pop("model_id", UNSET)

        ordering = d.pop("ordering", UNSET)

        quantization = d.pop("quantization", UNSET)

        recommended_preset = d.pop("recommended_preset", UNSET)

        revision = d.pop("revision", UNSET)

        stop_sequences = cast(list[str], d.pop("stop_sequences", UNSET))

        system_prompt = d.pop("system_prompt", UNSET)

        temperature = d.pop("temperature", UNSET)

        template_id = d.pop("template_id", UNSET)

        _translations = d.pop("translations", UNSET)
        translations: list[VariantTranslation] | Unset = UNSET
        if _translations is not UNSET:
            translations = []
            for translations_item_data in _translations:
                translations_item = VariantTranslation.from_dict(translations_item_data)

                translations.append(translations_item)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Timestamp | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = Timestamp.from_dict(_updated_at)

        variant = cls(
            artifact_type=artifact_type,
            created_at=created_at,
            gguf_files=gguf_files,
            health_checked_at=health_checked_at,
            health_error=health_error,
            health_status=health_status,
            icon_url=icon_url,
            id=id,
            is_active=is_active,
            max_context_tokens=max_context_tokens,
            model_id=model_id,
            ordering=ordering,
            quantization=quantization,
            recommended_preset=recommended_preset,
            revision=revision,
            stop_sequences=stop_sequences,
            system_prompt=system_prompt,
            temperature=temperature,
            template_id=template_id,
            translations=translations,
            updated_at=updated_at,
        )

        variant.additional_properties = d
        return variant

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
