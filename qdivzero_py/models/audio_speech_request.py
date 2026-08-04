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
            model (str | Unset):
            response_format (str | Unset):
            speed (float | Unset):
            task_type (str | Unset):
            voice (str | Unset):
     """

    input_: str | Unset = UNSET
    instructions: str | Unset = UNSET
    language: str | Unset = UNSET
    model: str | Unset = UNSET
    response_format: str | Unset = UNSET
    speed: float | Unset = UNSET
    task_type: str | Unset = UNSET
    voice: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        input_ = self.input_

        instructions = self.instructions

        language = self.language

        model = self.model

        response_format = self.response_format

        speed = self.speed

        task_type = self.task_type

        voice = self.voice


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if input_ is not UNSET:
            field_dict["input"] = input_
        if instructions is not UNSET:
            field_dict["instructions"] = instructions
        if language is not UNSET:
            field_dict["language"] = language
        if model is not UNSET:
            field_dict["model"] = model
        if response_format is not UNSET:
            field_dict["response_format"] = response_format
        if speed is not UNSET:
            field_dict["speed"] = speed
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if voice is not UNSET:
            field_dict["voice"] = voice

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        input_ = d.pop("input", UNSET)

        instructions = d.pop("instructions", UNSET)

        language = d.pop("language", UNSET)

        model = d.pop("model", UNSET)

        response_format = d.pop("response_format", UNSET)

        speed = d.pop("speed", UNSET)

        task_type = d.pop("task_type", UNSET)

        voice = d.pop("voice", UNSET)

        audio_speech_request = cls(
            input_=input_,
            instructions=instructions,
            language=language,
            model=model,
            response_format=response_format,
            speed=speed,
            task_type=task_type,
            voice=voice,
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
