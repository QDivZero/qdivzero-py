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
            model (str):
            prompt (str):
            image (File):
            mask (File | Unset):
            size (str | Unset):
            num_inference_steps (int | Unset):
            guidance_scale (float | Unset):
            seed (int | Unset):
            strength (float | Unset):
     """

    model: str
    prompt: str
    image: File
    mask: File | Unset = UNSET
    size: str | Unset = UNSET
    num_inference_steps: int | Unset = UNSET
    guidance_scale: float | Unset = UNSET
    seed: int | Unset = UNSET
    strength: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        model = self.model

        prompt = self.prompt

        image = self.image.to_tuple()


        mask: FileTypes | Unset = UNSET
        if not isinstance(self.mask, Unset):
            mask = self.mask.to_tuple()


        size = self.size

        num_inference_steps = self.num_inference_steps

        guidance_scale = self.guidance_scale

        seed = self.seed

        strength = self.strength


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "model": model,
            "prompt": prompt,
            "image": image,
        })
        if mask is not UNSET:
            field_dict["mask"] = mask
        if size is not UNSET:
            field_dict["size"] = size
        if num_inference_steps is not UNSET:
            field_dict["num_inference_steps"] = num_inference_steps
        if guidance_scale is not UNSET:
            field_dict["guidance_scale"] = guidance_scale
        if seed is not UNSET:
            field_dict["seed"] = seed
        if strength is not UNSET:
            field_dict["strength"] = strength

        return field_dict


    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("model", (None, str(self.model).encode(), "text/plain")))



        files.append(("prompt", (None, str(self.prompt).encode(), "text/plain")))



        files.append(("image", self.image.to_tuple()))



        if not isinstance(self.mask, Unset):
            files.append(("mask", self.mask.to_tuple()))



        if not isinstance(self.size, Unset):
            files.append(("size", (None, str(self.size).encode(), "text/plain")))



        if not isinstance(self.num_inference_steps, Unset):
            files.append(("num_inference_steps", (None, str(self.num_inference_steps).encode(), "text/plain")))



        if not isinstance(self.guidance_scale, Unset):
            files.append(("guidance_scale", (None, str(self.guidance_scale).encode(), "text/plain")))



        if not isinstance(self.seed, Unset):
            files.append(("seed", (None, str(self.seed).encode(), "text/plain")))



        if not isinstance(self.strength, Unset):
            files.append(("strength", (None, str(self.strength).encode(), "text/plain")))




        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))



        return files


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model = d.pop("model")

        prompt = d.pop("prompt")

        image = File(
             payload = BytesIO(d.pop("image"))
        )




        _mask = d.pop("mask", UNSET)
        mask: File | Unset
        if isinstance(_mask,  Unset):
            mask = UNSET
        else:
            mask = File(
             payload = BytesIO(_mask)
        )




        size = d.pop("size", UNSET)

        num_inference_steps = d.pop("num_inference_steps", UNSET)

        guidance_scale = d.pop("guidance_scale", UNSET)

        seed = d.pop("seed", UNSET)

        strength = d.pop("strength", UNSET)

        post_v1_image_edits_body = cls(
            model=model,
            prompt=prompt,
            image=image,
            mask=mask,
            size=size,
            num_inference_steps=num_inference_steps,
            guidance_scale=guidance_scale,
            seed=seed,
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
