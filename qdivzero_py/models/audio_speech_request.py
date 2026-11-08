from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AudioSpeechRequest")


@_attrs_define
class AudioSpeechRequest:
    """
    Attributes:
        input_ (str | Unset):
        instructions (str | Unset):
        language (str | Unset):
        max_new_tokens (int | Unset):
        model (str | Unset):
        ref_audio (str | Unset):
        ref_text (str | Unset):
        response_format (str | Unset):
        seed (int | Unset):
        speed (float | Unset):
        task_type (str | Unset):
        voice (str | Unset):
        x_vector_only_mode (bool | Unset):
    """

    input_: str | Unset = UNSET
    instructions: str | Unset = UNSET
    language: str | Unset = UNSET
    max_new_tokens: int | Unset = UNSET
    model: str | Unset = UNSET
    ref_audio: str | Unset = UNSET
    ref_text: str | Unset = UNSET
    response_format: str | Unset = UNSET
    seed: int | Unset = UNSET
    speed: float | Unset = UNSET
    task_type: str | Unset = UNSET
    voice: str | Unset = UNSET
    x_vector_only_mode: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_ = self.input_

        instructions = self.instructions

        language = self.language

        max_new_tokens = self.max_new_tokens

        model = self.model

        ref_audio = self.ref_audio

        ref_text = self.ref_text

        response_format = self.response_format

        seed = self.seed

        speed = self.speed

        task_type = self.task_type

        voice = self.voice

        x_vector_only_mode = self.x_vector_only_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if input_ is not UNSET:
            field_dict["input"] = input_
        if instructions is not UNSET:
            field_dict["instructions"] = instructions
        if language is not UNSET:
            field_dict["language"] = language
        if max_new_tokens is not UNSET:
            field_dict["max_new_tokens"] = max_new_tokens
        if model is not UNSET:
            field_dict["model"] = model
        if ref_audio is not UNSET:
            field_dict["ref_audio"] = ref_audio
        if ref_text is not UNSET:
            field_dict["ref_text"] = ref_text
        if response_format is not UNSET:
            field_dict["response_format"] = response_format
        if seed is not UNSET:
            field_dict["seed"] = seed
        if speed is not UNSET:
            field_dict["speed"] = speed
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if voice is not UNSET:
            field_dict["voice"] = voice
        if x_vector_only_mode is not UNSET:
            field_dict["x_vector_only_mode"] = x_vector_only_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        input_ = d.pop("input", UNSET)

        instructions = d.pop("instructions", UNSET)

        language = d.pop("language", UNSET)

        max_new_tokens = d.pop("max_new_tokens", UNSET)

        model = d.pop("model", UNSET)

        ref_audio = d.pop("ref_audio", UNSET)

        ref_text = d.pop("ref_text", UNSET)

        response_format = d.pop("response_format", UNSET)

        seed = d.pop("seed", UNSET)

        speed = d.pop("speed", UNSET)

        task_type = d.pop("task_type", UNSET)

        voice = d.pop("voice", UNSET)

        x_vector_only_mode = d.pop("x_vector_only_mode", UNSET)

        audio_speech_request = cls(
            input_=input_,
            instructions=instructions,
            language=language,
            max_new_tokens=max_new_tokens,
            model=model,
            ref_audio=ref_audio,
            ref_text=ref_text,
            response_format=response_format,
            seed=seed,
            speed=speed,
            task_type=task_type,
            voice=voice,
            x_vector_only_mode=x_vector_only_mode,
        )

        audio_speech_request.additional_properties = d
        return audio_speech_request

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
