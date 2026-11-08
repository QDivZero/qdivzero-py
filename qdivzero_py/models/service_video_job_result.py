from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_video_job_result_status import ServiceVideoJobResultStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceVideoJobResult")


@_attrs_define
class ServiceVideoJobResult:
    """
    Attributes:
        cancel_requested (bool):
        completed_at (str): RFC3339 timestamp, or an empty string before this lifecycle event.
        created_at (datetime.datetime):
        expires_at (str): RFC3339 timestamp, or an empty string before this lifecycle event.
        id (UUID):
        model (str):
        prompt (str):
        started_at (str): RFC3339 timestamp, or an empty string before this lifecycle event.
        status (ServiceVideoJobResultStatus):
        error (str | Unset):
    """

    cancel_requested: bool
    completed_at: str
    created_at: datetime.datetime
    expires_at: str
    id: UUID
    model: str
    prompt: str
    started_at: str
    status: ServiceVideoJobResultStatus
    error: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cancel_requested = self.cancel_requested

        completed_at = self.completed_at

        created_at = self.created_at.isoformat()

        expires_at = self.expires_at

        id = str(self.id)

        model = self.model

        prompt = self.prompt

        started_at = self.started_at

        status = self.status.value

        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cancel_requested": cancel_requested,
                "completed_at": completed_at,
                "created_at": created_at,
                "expires_at": expires_at,
                "id": id,
                "model": model,
                "prompt": prompt,
                "started_at": started_at,
                "status": status,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cancel_requested = d.pop("cancel_requested")

        completed_at = d.pop("completed_at")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        expires_at = d.pop("expires_at")

        id = UUID(d.pop("id"))

        model = d.pop("model")

        prompt = d.pop("prompt")

        started_at = d.pop("started_at")

        status = ServiceVideoJobResultStatus(d.pop("status"))

        error = d.pop("error", UNSET)

        service_video_job_result = cls(
            cancel_requested=cancel_requested,
            completed_at=completed_at,
            created_at=created_at,
            expires_at=expires_at,
            id=id,
            model=model,
            prompt=prompt,
            started_at=started_at,
            status=status,
            error=error,
        )

        service_video_job_result.additional_properties = d
        return service_video_job_result

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
