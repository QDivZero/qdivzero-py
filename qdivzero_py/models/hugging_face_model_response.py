from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hugging_face_gguf_file_response import HuggingFaceGGUFFileResponse
    from ..models.hugging_face_yolo_file_response import HuggingFaceYOLOFileResponse


T = TypeVar("T", bound="HuggingFaceModelResponse")


@_attrs_define
class HuggingFaceModelResponse:
    """
    Attributes:
        compatibility_reason (str | Unset):
        compatible (bool | Unset):
        description (str | Unset):
        downloads (int | Unset):
        gguf_files (list[HuggingFaceGGUFFileResponse] | Unset):
        has_gguf (bool | Unset):
        has_safetensors (bool | Unset):
        last_modified (str | Unset):
        likes (int | Unset):
        pipeline_tag (str | Unset):
        repo_id (str | Unset):
        siblings (list[str] | Unset):
        tags (list[str] | Unset):
        warnings (list[str] | Unset):
        workload_kind (str | Unset):
        yolo_files (list[HuggingFaceYOLOFileResponse] | Unset):
    """

    compatibility_reason: str | Unset = UNSET
    compatible: bool | Unset = UNSET
    description: str | Unset = UNSET
    downloads: int | Unset = UNSET
    gguf_files: list[HuggingFaceGGUFFileResponse] | Unset = UNSET
    has_gguf: bool | Unset = UNSET
    has_safetensors: bool | Unset = UNSET
    last_modified: str | Unset = UNSET
    likes: int | Unset = UNSET
    pipeline_tag: str | Unset = UNSET
    repo_id: str | Unset = UNSET
    siblings: list[str] | Unset = UNSET
    tags: list[str] | Unset = UNSET
    warnings: list[str] | Unset = UNSET
    workload_kind: str | Unset = UNSET
    yolo_files: list[HuggingFaceYOLOFileResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        compatibility_reason = self.compatibility_reason

        compatible = self.compatible

        description = self.description

        downloads = self.downloads

        gguf_files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.gguf_files, Unset):
            gguf_files = []
            for gguf_files_item_data in self.gguf_files:
                gguf_files_item = gguf_files_item_data.to_dict()
                gguf_files.append(gguf_files_item)

        has_gguf = self.has_gguf

        has_safetensors = self.has_safetensors

        last_modified = self.last_modified

        likes = self.likes

        pipeline_tag = self.pipeline_tag

        repo_id = self.repo_id

        siblings: list[str] | Unset = UNSET
        if not isinstance(self.siblings, Unset):
            siblings = self.siblings

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        warnings: list[str] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        workload_kind = self.workload_kind

        yolo_files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.yolo_files, Unset):
            yolo_files = []
            for yolo_files_item_data in self.yolo_files:
                yolo_files_item = yolo_files_item_data.to_dict()
                yolo_files.append(yolo_files_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if compatibility_reason is not UNSET:
            field_dict["compatibility_reason"] = compatibility_reason
        if compatible is not UNSET:
            field_dict["compatible"] = compatible
        if description is not UNSET:
            field_dict["description"] = description
        if downloads is not UNSET:
            field_dict["downloads"] = downloads
        if gguf_files is not UNSET:
            field_dict["gguf_files"] = gguf_files
        if has_gguf is not UNSET:
            field_dict["has_gguf"] = has_gguf
        if has_safetensors is not UNSET:
            field_dict["has_safetensors"] = has_safetensors
        if last_modified is not UNSET:
            field_dict["last_modified"] = last_modified
        if likes is not UNSET:
            field_dict["likes"] = likes
        if pipeline_tag is not UNSET:
            field_dict["pipeline_tag"] = pipeline_tag
        if repo_id is not UNSET:
            field_dict["repo_id"] = repo_id
        if siblings is not UNSET:
            field_dict["siblings"] = siblings
        if tags is not UNSET:
            field_dict["tags"] = tags
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if workload_kind is not UNSET:
            field_dict["workload_kind"] = workload_kind
        if yolo_files is not UNSET:
            field_dict["yolo_files"] = yolo_files

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hugging_face_gguf_file_response import HuggingFaceGGUFFileResponse
        from ..models.hugging_face_yolo_file_response import HuggingFaceYOLOFileResponse

        d = dict(src_dict)
        compatibility_reason = d.pop("compatibility_reason", UNSET)

        compatible = d.pop("compatible", UNSET)

        description = d.pop("description", UNSET)

        downloads = d.pop("downloads", UNSET)

        _gguf_files = d.pop("gguf_files", UNSET)
        gguf_files: list[HuggingFaceGGUFFileResponse] | Unset = UNSET
        if _gguf_files is not UNSET:
            gguf_files = []
            for gguf_files_item_data in _gguf_files:
                gguf_files_item = HuggingFaceGGUFFileResponse.from_dict(gguf_files_item_data)

                gguf_files.append(gguf_files_item)

        has_gguf = d.pop("has_gguf", UNSET)

        has_safetensors = d.pop("has_safetensors", UNSET)

        last_modified = d.pop("last_modified", UNSET)

        likes = d.pop("likes", UNSET)

        pipeline_tag = d.pop("pipeline_tag", UNSET)

        repo_id = d.pop("repo_id", UNSET)

        siblings = cast(list[str], d.pop("siblings", UNSET))

        tags = cast(list[str], d.pop("tags", UNSET))

        warnings = cast(list[str], d.pop("warnings", UNSET))

        workload_kind = d.pop("workload_kind", UNSET)

        _yolo_files = d.pop("yolo_files", UNSET)
        yolo_files: list[HuggingFaceYOLOFileResponse] | Unset = UNSET
        if _yolo_files is not UNSET:
            yolo_files = []
            for yolo_files_item_data in _yolo_files:
                yolo_files_item = HuggingFaceYOLOFileResponse.from_dict(yolo_files_item_data)

                yolo_files.append(yolo_files_item)

        hugging_face_model_response = cls(
            compatibility_reason=compatibility_reason,
            compatible=compatible,
            description=description,
            downloads=downloads,
            gguf_files=gguf_files,
            has_gguf=has_gguf,
            has_safetensors=has_safetensors,
            last_modified=last_modified,
            likes=likes,
            pipeline_tag=pipeline_tag,
            repo_id=repo_id,
            siblings=siblings,
            tags=tags,
            warnings=warnings,
            workload_kind=workload_kind,
            yolo_files=yolo_files,
        )

        hugging_face_model_response.additional_properties = d
        return hugging_face_model_response

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
