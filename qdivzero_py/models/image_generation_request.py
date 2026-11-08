from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImageGenerationRequest")


@_attrs_define
class ImageGenerationRequest:
    """
    Attributes:
        guidance_scale (float | Unset):
        height (int | Unset):
        model (str | Unset):
        n (int | Unset):
        num_inference_steps (int | Unset):
        prompt (str | Unset):
        quality (str | Unset):
        response_format (str | Unset):
        seed (int | Unset):
        size (str | Unset):
        style (str | Unset):
        user (str | Unset):
        width (int | Unset):
    """

    guidance_scale: float | Unset = UNSET
    height: int | Unset = UNSET
    model: str | Unset = UNSET
    n: int | Unset = UNSET
    num_inference_steps: int | Unset = UNSET
    prompt: str | Unset = UNSET
    quality: str | Unset = UNSET
    response_format: str | Unset = UNSET
    seed: int | Unset = UNSET
    size: str | Unset = UNSET
    style: str | Unset = UNSET
    user: str | Unset = UNSET
    width: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        guidance_scale = self.guidance_scale

        height = self.height

        model = self.model

        n = self.n

        num_inference_steps = self.num_inference_steps

        prompt = self.prompt

        quality = self.quality

        response_format = self.response_format

        seed = self.seed

        size = self.size

        style = self.style

        user = self.user

        width = self.width

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if guidance_scale is not UNSET:
            field_dict["guidance_scale"] = guidance_scale
        if height is not UNSET:
            field_dict["height"] = height
        if model is not UNSET:
            field_dict["model"] = model
        if n is not UNSET:
            field_dict["n"] = n
        if num_inference_steps is not UNSET:
            field_dict["num_inference_steps"] = num_inference_steps
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if quality is not UNSET:
            field_dict["quality"] = quality
        if response_format is not UNSET:
            field_dict["response_format"] = response_format
        if seed is not UNSET:
            field_dict["seed"] = seed
        if size is not UNSET:
            field_dict["size"] = size
        if style is not UNSET:
            field_dict["style"] = style
        if user is not UNSET:
            field_dict["user"] = user
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        guidance_scale = d.pop("guidance_scale", UNSET)

        height = d.pop("height", UNSET)

        model = d.pop("model", UNSET)

        n = d.pop("n", UNSET)

        num_inference_steps = d.pop("num_inference_steps", UNSET)

        prompt = d.pop("prompt", UNSET)

        quality = d.pop("quality", UNSET)

        response_format = d.pop("response_format", UNSET)

        seed = d.pop("seed", UNSET)

        size = d.pop("size", UNSET)

        style = d.pop("style", UNSET)

        user = d.pop("user", UNSET)

        width = d.pop("width", UNSET)

        image_generation_request = cls(
            guidance_scale=guidance_scale,
            height=height,
            model=model,
            n=n,
            num_inference_steps=num_inference_steps,
            prompt=prompt,
            quality=quality,
            response_format=response_format,
            seed=seed,
            size=size,
            style=style,
            user=user,
            width=width,
        )

        image_generation_request.additional_properties = d
        return image_generation_request

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
