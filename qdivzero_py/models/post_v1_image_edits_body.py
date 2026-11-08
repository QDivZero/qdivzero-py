from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="PostV1ImageEditsBody")


@_attrs_define
class PostV1ImageEditsBody:
    """
    Attributes:
        image (File): Source image file
        model (str): Model ID
        prompt (str): Edit prompt
        guidance_scale (float | Unset): Guidance scale (0-20)
        mask (File | Unset): Mask image file
        num_inference_steps (int | Unset): Inference steps (1-200)
        seed (int | Unset): Random seed
        size (str | Unset): Output size (WIDTHxHEIGHT)
        strength (float | Unset): Denoising strength (0-1, lower preserves original)
    """

    image: File
    model: str
    prompt: str
    guidance_scale: float | Unset = UNSET
    mask: File | Unset = UNSET
    num_inference_steps: int | Unset = UNSET
    seed: int | Unset = UNSET
    size: str | Unset = UNSET
    strength: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image = self.image.to_tuple()

        model = self.model

        prompt = self.prompt

        guidance_scale = self.guidance_scale

        mask: FileTypes | Unset = UNSET
        if not isinstance(self.mask, Unset):
            mask = self.mask.to_tuple()

        num_inference_steps = self.num_inference_steps

        seed = self.seed

        size = self.size

        strength = self.strength

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "image": image,
                "model": model,
                "prompt": prompt,
            }
        )
        if guidance_scale is not UNSET:
            field_dict["guidance_scale"] = guidance_scale
        if mask is not UNSET:
            field_dict["mask"] = mask
        if num_inference_steps is not UNSET:
            field_dict["num_inference_steps"] = num_inference_steps
        if seed is not UNSET:
            field_dict["seed"] = seed
        if size is not UNSET:
            field_dict["size"] = size
        if strength is not UNSET:
            field_dict["strength"] = strength

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("image", self.image.to_tuple()))

        files.append(("model", (None, str(self.model).encode(), "text/plain")))

        files.append(("prompt", (None, str(self.prompt).encode(), "text/plain")))

        if not isinstance(self.guidance_scale, Unset):
            files.append(("guidance_scale", (None, str(self.guidance_scale).encode(), "text/plain")))

        if not isinstance(self.mask, Unset):
            files.append(("mask", self.mask.to_tuple()))

        if not isinstance(self.num_inference_steps, Unset):
            files.append(("num_inference_steps", (None, str(self.num_inference_steps).encode(), "text/plain")))

        if not isinstance(self.seed, Unset):
            files.append(("seed", (None, str(self.seed).encode(), "text/plain")))

        if not isinstance(self.size, Unset):
            files.append(("size", (None, str(self.size).encode(), "text/plain")))

        if not isinstance(self.strength, Unset):
            files.append(("strength", (None, str(self.strength).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        image = File(payload=BytesIO(d.pop("image")))

        model = d.pop("model")

        prompt = d.pop("prompt")

        guidance_scale = d.pop("guidance_scale", UNSET)

        _mask = d.pop("mask", UNSET)
        mask: File | Unset
        if isinstance(_mask, Unset):
            mask = UNSET
        else:
            mask = File(payload=BytesIO(_mask))

        num_inference_steps = d.pop("num_inference_steps", UNSET)

        seed = d.pop("seed", UNSET)

        size = d.pop("size", UNSET)

        strength = d.pop("strength", UNSET)

        post_v1_image_edits_body = cls(
            image=image,
            model=model,
            prompt=prompt,
            guidance_scale=guidance_scale,
            mask=mask,
            num_inference_steps=num_inference_steps,
            seed=seed,
            size=size,
            strength=strength,
        )

        post_v1_image_edits_body.additional_properties = d
        return post_v1_image_edits_body

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
