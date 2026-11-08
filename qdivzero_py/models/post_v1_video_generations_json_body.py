from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_v1_video_generations_json_body_aspect_ratio import PostV1VideoGenerationsJsonBodyAspectRatio
from ..models.post_v1_video_generations_json_body_fps import PostV1VideoGenerationsJsonBodyFps
from ..models.post_v1_video_generations_json_body_task import PostV1VideoGenerationsJsonBodyTask
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1VideoGenerationsJsonBody")


@_attrs_define
class PostV1VideoGenerationsJsonBody:
    """
    Attributes:
        model (str): Model ID
        prompt (str): Video prompt (maximum 7,000 Unicode characters)
        aspect_ratio (PostV1VideoGenerationsJsonBodyAspectRatio | Unset): Output aspect ratio: a standard ratio may
            accompany matching dimensions; adaptive requires short_edge
        audio_flow_shift (float | Unset): Non-negative audio flow shift Default: 3.0.
        audio_reference_url (str | Unset): Hosted audio reference URL; HTTP(S) URLs are limited to 16 KiB and data URLs
            to the bounded decoded-audio ceiling
        duration (float | Unset): Duration in seconds Default: 5.0.
        flow_shift (float | Unset): Non-negative flow shift Default: 12.0.
        fps (PostV1VideoGenerationsJsonBodyFps | Unset): Frames per second; only 24 is supported Default:
            PostV1VideoGenerationsJsonBodyFps.VALUE_24.
        height (int | Unset): Output height; provide with width; may accompany a matching standard aspect_ratio
        num_inference_steps (int | Unset): Inference steps Default: 50.
        seed (int | Unset): Random seed
        short_edge (int | Unset): Output short edge; only valid with aspect_ratio=adaptive
        task (PostV1VideoGenerationsJsonBodyTask | Unset): Generation task: t2va, fl2va, ref2va, t2v, or i2v Default:
            PostV1VideoGenerationsJsonBodyTask.T2VA.
        width (int | Unset): Output width; provide with height; may accompany a matching standard aspect_ratio
    """

    model: str
    prompt: str
    aspect_ratio: PostV1VideoGenerationsJsonBodyAspectRatio | Unset = UNSET
    audio_flow_shift: float | Unset = 3.0
    audio_reference_url: str | Unset = UNSET
    duration: float | Unset = 5.0
    flow_shift: float | Unset = 12.0
    fps: PostV1VideoGenerationsJsonBodyFps | Unset = PostV1VideoGenerationsJsonBodyFps.VALUE_24
    height: int | Unset = UNSET
    num_inference_steps: int | Unset = 50
    seed: int | Unset = UNSET
    short_edge: int | Unset = UNSET
    task: PostV1VideoGenerationsJsonBodyTask | Unset = PostV1VideoGenerationsJsonBodyTask.T2VA
    width: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model = self.model

        prompt = self.prompt

        aspect_ratio: str | Unset = UNSET
        if not isinstance(self.aspect_ratio, Unset):
            aspect_ratio = self.aspect_ratio.value

        audio_flow_shift = self.audio_flow_shift

        audio_reference_url = self.audio_reference_url

        duration = self.duration

        flow_shift = self.flow_shift

        fps: int | Unset = UNSET
        if not isinstance(self.fps, Unset):
            fps = self.fps.value

        height = self.height

        num_inference_steps = self.num_inference_steps

        seed = self.seed

        short_edge = self.short_edge

        task: str | Unset = UNSET
        if not isinstance(self.task, Unset):
            task = self.task.value

        width = self.width

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model": model,
                "prompt": prompt,
            }
        )
        if aspect_ratio is not UNSET:
            field_dict["aspect_ratio"] = aspect_ratio
        if audio_flow_shift is not UNSET:
            field_dict["audio_flow_shift"] = audio_flow_shift
        if audio_reference_url is not UNSET:
            field_dict["audio_reference_url"] = audio_reference_url
        if duration is not UNSET:
            field_dict["duration"] = duration
        if flow_shift is not UNSET:
            field_dict["flow_shift"] = flow_shift
        if fps is not UNSET:
            field_dict["fps"] = fps
        if height is not UNSET:
            field_dict["height"] = height
        if num_inference_steps is not UNSET:
            field_dict["num_inference_steps"] = num_inference_steps
        if seed is not UNSET:
            field_dict["seed"] = seed
        if short_edge is not UNSET:
            field_dict["short_edge"] = short_edge
        if task is not UNSET:
            field_dict["task"] = task
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model = d.pop("model")

        prompt = d.pop("prompt")

        _aspect_ratio = d.pop("aspect_ratio", UNSET)
        aspect_ratio: PostV1VideoGenerationsJsonBodyAspectRatio | Unset
        if isinstance(_aspect_ratio, Unset):
            aspect_ratio = UNSET
        else:
            aspect_ratio = PostV1VideoGenerationsJsonBodyAspectRatio(_aspect_ratio)

        audio_flow_shift = d.pop("audio_flow_shift", UNSET)

        audio_reference_url = d.pop("audio_reference_url", UNSET)

        duration = d.pop("duration", UNSET)

        flow_shift = d.pop("flow_shift", UNSET)

        _fps = d.pop("fps", UNSET)
        fps: PostV1VideoGenerationsJsonBodyFps | Unset
        if isinstance(_fps, Unset):
            fps = UNSET
        else:
            fps = PostV1VideoGenerationsJsonBodyFps(_fps)

        height = d.pop("height", UNSET)

        num_inference_steps = d.pop("num_inference_steps", UNSET)

        seed = d.pop("seed", UNSET)

        short_edge = d.pop("short_edge", UNSET)

        _task = d.pop("task", UNSET)
        task: PostV1VideoGenerationsJsonBodyTask | Unset
        if isinstance(_task, Unset):
            task = UNSET
        else:
            task = PostV1VideoGenerationsJsonBodyTask(_task)

        width = d.pop("width", UNSET)

        post_v1_video_generations_json_body = cls(
            model=model,
            prompt=prompt,
            aspect_ratio=aspect_ratio,
            audio_flow_shift=audio_flow_shift,
            audio_reference_url=audio_reference_url,
            duration=duration,
            flow_shift=flow_shift,
            fps=fps,
            height=height,
            num_inference_steps=num_inference_steps,
            seed=seed,
            short_edge=short_edge,
            task=task,
            width=width,
        )

        post_v1_video_generations_json_body.additional_properties = d
        return post_v1_video_generations_json_body

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
