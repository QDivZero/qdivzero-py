from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.post_v1_video_job_files_body_aspect_ratio import PostV1VideoJobFilesBodyAspectRatio
from ..models.post_v1_video_job_files_body_fps import PostV1VideoJobFilesBodyFps
from ..models.post_v1_video_job_files_body_task import PostV1VideoJobFilesBodyTask
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="PostV1VideoJobFilesBody")


@_attrs_define
class PostV1VideoJobFilesBody:
    """
    Attributes:
        model (str): Model ID
        prompt (str): Video prompt (maximum 7,000 Unicode characters)
        aspect_ratio (PostV1VideoJobFilesBodyAspectRatio | Unset): Standard aspect ratio or adaptive
        audio_flow_shift (float | Unset): Non-negative audio flow shift Default: 3.0.
        audio_reference (File | Unset): Optional H3 Ref2VA audio reference up to 15 MiB; requires at least one image or
            video reference
        audio_reference_url (str | Unset): HTTP(S) audio URL up to 16 KiB or data URL with decoded audio up to 15 MiB
        duration (float | Unset): Duration in seconds Default: 5.0.
        flow_shift (float | Unset): Non-negative flow shift Default: 12.0.
        fps (PostV1VideoJobFilesBodyFps | Unset): Frames per second Default: PostV1VideoJobFilesBodyFps.VALUE_24.
        height (int | Unset): Output height; provide with width
        input_reference (File | Unset): Image up to 30 MiB or video up to 50 MiB; may be repeated. H3 Ref2VA allows
            mixed references, up to nine images, three videos, and twelve total; aggregate references plus audio up to 64
            MiB
        input_references (File | Unset): Repeated image or video references with the same limits as input_reference
        num_inference_steps (int | Unset): Inference steps Default: 50.
        seed (int | Unset): Random seed
        short_edge (int | Unset): Output short edge; only with adaptive aspect ratio
        task (PostV1VideoJobFilesBodyTask | Unset): Generation task Default: PostV1VideoJobFilesBodyTask.T2VA.
        width (int | Unset): Output width; provide with height
    """

    model: str
    prompt: str
    aspect_ratio: PostV1VideoJobFilesBodyAspectRatio | Unset = UNSET
    audio_flow_shift: float | Unset = 3.0
    audio_reference: File | Unset = UNSET
    audio_reference_url: str | Unset = UNSET
    duration: float | Unset = 5.0
    flow_shift: float | Unset = 12.0
    fps: PostV1VideoJobFilesBodyFps | Unset = PostV1VideoJobFilesBodyFps.VALUE_24
    height: int | Unset = UNSET
    input_reference: File | Unset = UNSET
    input_references: File | Unset = UNSET
    num_inference_steps: int | Unset = 50
    seed: int | Unset = UNSET
    short_edge: int | Unset = UNSET
    task: PostV1VideoJobFilesBodyTask | Unset = PostV1VideoJobFilesBodyTask.T2VA
    width: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model = self.model

        prompt = self.prompt

        aspect_ratio: str | Unset = UNSET
        if not isinstance(self.aspect_ratio, Unset):
            aspect_ratio = self.aspect_ratio.value

        audio_flow_shift = self.audio_flow_shift

        audio_reference: FileTypes | Unset = UNSET
        if not isinstance(self.audio_reference, Unset):
            audio_reference = self.audio_reference.to_tuple()

        audio_reference_url = self.audio_reference_url

        duration = self.duration

        flow_shift = self.flow_shift

        fps: int | Unset = UNSET
        if not isinstance(self.fps, Unset):
            fps = self.fps.value

        height = self.height

        input_reference: FileTypes | Unset = UNSET
        if not isinstance(self.input_reference, Unset):
            input_reference = self.input_reference.to_tuple()

        input_references: FileTypes | Unset = UNSET
        if not isinstance(self.input_references, Unset):
            input_references = self.input_references.to_tuple()

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
        if audio_reference is not UNSET:
            field_dict["audio_reference"] = audio_reference
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
        if input_reference is not UNSET:
            field_dict["input_reference"] = input_reference
        if input_references is not UNSET:
            field_dict["input_references"] = input_references
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

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("model", (None, str(self.model).encode(), "text/plain")))

        files.append(("prompt", (None, str(self.prompt).encode(), "text/plain")))

        if not isinstance(self.aspect_ratio, Unset):
            files.append(("aspect_ratio", (None, str(self.aspect_ratio.value).encode(), "text/plain")))

        if not isinstance(self.audio_flow_shift, Unset):
            files.append(("audio_flow_shift", (None, str(self.audio_flow_shift).encode(), "text/plain")))

        if not isinstance(self.audio_reference, Unset):
            files.append(("audio_reference", self.audio_reference.to_tuple()))

        if not isinstance(self.audio_reference_url, Unset):
            files.append(("audio_reference_url", (None, str(self.audio_reference_url).encode(), "text/plain")))

        if not isinstance(self.duration, Unset):
            files.append(("duration", (None, str(self.duration).encode(), "text/plain")))

        if not isinstance(self.flow_shift, Unset):
            files.append(("flow_shift", (None, str(self.flow_shift).encode(), "text/plain")))

        if not isinstance(self.fps, Unset):
            files.append(("fps", (None, str(self.fps.value).encode(), "text/plain")))

        if not isinstance(self.height, Unset):
            files.append(("height", (None, str(self.height).encode(), "text/plain")))

        if not isinstance(self.input_reference, Unset):
            files.append(("input_reference", self.input_reference.to_tuple()))

        if not isinstance(self.input_references, Unset):
            files.append(("input_references", self.input_references.to_tuple()))

        if not isinstance(self.num_inference_steps, Unset):
            files.append(("num_inference_steps", (None, str(self.num_inference_steps).encode(), "text/plain")))

        if not isinstance(self.seed, Unset):
            files.append(("seed", (None, str(self.seed).encode(), "text/plain")))

        if not isinstance(self.short_edge, Unset):
            files.append(("short_edge", (None, str(self.short_edge).encode(), "text/plain")))

        if not isinstance(self.task, Unset):
            files.append(("task", (None, str(self.task.value).encode(), "text/plain")))

        if not isinstance(self.width, Unset):
            files.append(("width", (None, str(self.width).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model = d.pop("model")

        prompt = d.pop("prompt")

        _aspect_ratio = d.pop("aspect_ratio", UNSET)
        aspect_ratio: PostV1VideoJobFilesBodyAspectRatio | Unset
        if isinstance(_aspect_ratio, Unset):
            aspect_ratio = UNSET
        else:
            aspect_ratio = PostV1VideoJobFilesBodyAspectRatio(_aspect_ratio)

        audio_flow_shift = d.pop("audio_flow_shift", UNSET)

        _audio_reference = d.pop("audio_reference", UNSET)
        audio_reference: File | Unset
        if isinstance(_audio_reference, Unset):
            audio_reference = UNSET
        else:
            audio_reference = File(payload=BytesIO(_audio_reference))

        audio_reference_url = d.pop("audio_reference_url", UNSET)

        duration = d.pop("duration", UNSET)

        flow_shift = d.pop("flow_shift", UNSET)

        _fps = d.pop("fps", UNSET)
        fps: PostV1VideoJobFilesBodyFps | Unset
        if isinstance(_fps, Unset):
            fps = UNSET
        else:
            fps = PostV1VideoJobFilesBodyFps(_fps)

        height = d.pop("height", UNSET)

        _input_reference = d.pop("input_reference", UNSET)
        input_reference: File | Unset
        if isinstance(_input_reference, Unset):
            input_reference = UNSET
        else:
            input_reference = File(payload=BytesIO(_input_reference))

        _input_references = d.pop("input_references", UNSET)
        input_references: File | Unset
        if isinstance(_input_references, Unset):
            input_references = UNSET
        else:
            input_references = File(payload=BytesIO(_input_references))

        num_inference_steps = d.pop("num_inference_steps", UNSET)

        seed = d.pop("seed", UNSET)

        short_edge = d.pop("short_edge", UNSET)

        _task = d.pop("task", UNSET)
        task: PostV1VideoJobFilesBodyTask | Unset
        if isinstance(_task, Unset):
            task = UNSET
        else:
            task = PostV1VideoJobFilesBodyTask(_task)

        width = d.pop("width", UNSET)

        post_v1_video_job_files_body = cls(
            model=model,
            prompt=prompt,
            aspect_ratio=aspect_ratio,
            audio_flow_shift=audio_flow_shift,
            audio_reference=audio_reference,
            audio_reference_url=audio_reference_url,
            duration=duration,
            flow_shift=flow_shift,
            fps=fps,
            height=height,
            input_reference=input_reference,
            input_references=input_references,
            num_inference_steps=num_inference_steps,
            seed=seed,
            short_edge=short_edge,
            task=task,
            width=width,
        )

        post_v1_video_job_files_body.additional_properties = d
        return post_v1_video_job_files_body

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
