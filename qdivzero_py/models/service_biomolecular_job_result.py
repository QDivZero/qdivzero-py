from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_biomolecular_artifact import ServiceBiomolecularArtifact
    from ..models.service_biomolecular_job_result_affinity import ServiceBiomolecularJobResultAffinity
    from ..models.service_biomolecular_job_result_confidence_item import ServiceBiomolecularJobResultConfidenceItem
    from ..models.service_biomolecular_job_result_metadata import ServiceBiomolecularJobResultMetadata


T = TypeVar("T", bound="ServiceBiomolecularJobResult")


@_attrs_define
class ServiceBiomolecularJobResult:
    """
    Attributes:
        affinity (ServiceBiomolecularJobResultAffinity | Unset):
        artifacts (list[ServiceBiomolecularArtifact] | Unset):
        completed_at (str | Unset):
        confidence (list[ServiceBiomolecularJobResultConfidenceItem] | Unset):
        created_at (str | Unset):
        error (str | Unset):
        id (str | Unset):
        metadata (ServiceBiomolecularJobResultMetadata | Unset):
        model (str | Unset):
        started_at (str | Unset):
        status (str | Unset):
    """

    affinity: ServiceBiomolecularJobResultAffinity | Unset = UNSET
    artifacts: list[ServiceBiomolecularArtifact] | Unset = UNSET
    completed_at: str | Unset = UNSET
    confidence: list[ServiceBiomolecularJobResultConfidenceItem] | Unset = UNSET
    created_at: str | Unset = UNSET
    error: str | Unset = UNSET
    id: str | Unset = UNSET
    metadata: ServiceBiomolecularJobResultMetadata | Unset = UNSET
    model: str | Unset = UNSET
    started_at: str | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affinity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.affinity, Unset):
            affinity = self.affinity.to_dict()

        artifacts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.artifacts, Unset):
            artifacts = []
            for artifacts_item_data in self.artifacts:
                artifacts_item = artifacts_item_data.to_dict()
                artifacts.append(artifacts_item)

        completed_at = self.completed_at

        confidence: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.confidence, Unset):
            confidence = []
            for confidence_item_data in self.confidence:
                confidence_item = confidence_item_data.to_dict()
                confidence.append(confidence_item)

        created_at = self.created_at

        error = self.error

        id = self.id

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        model = self.model

        started_at = self.started_at

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affinity is not UNSET:
            field_dict["affinity"] = affinity
        if artifacts is not UNSET:
            field_dict["artifacts"] = artifacts
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if confidence is not UNSET:
            field_dict["confidence"] = confidence
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if error is not UNSET:
            field_dict["error"] = error
        if id is not UNSET:
            field_dict["id"] = id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if model is not UNSET:
            field_dict["model"] = model
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_biomolecular_artifact import ServiceBiomolecularArtifact
        from ..models.service_biomolecular_job_result_affinity import ServiceBiomolecularJobResultAffinity
        from ..models.service_biomolecular_job_result_confidence_item import ServiceBiomolecularJobResultConfidenceItem
        from ..models.service_biomolecular_job_result_metadata import ServiceBiomolecularJobResultMetadata

        d = dict(src_dict)
        _affinity = d.pop("affinity", UNSET)
        affinity: ServiceBiomolecularJobResultAffinity | Unset
        if isinstance(_affinity, Unset):
            affinity = UNSET
        else:
            affinity = ServiceBiomolecularJobResultAffinity.from_dict(_affinity)

        _artifacts = d.pop("artifacts", UNSET)
        artifacts: list[ServiceBiomolecularArtifact] | Unset = UNSET
        if _artifacts is not UNSET:
            artifacts = []
            for artifacts_item_data in _artifacts:
                artifacts_item = ServiceBiomolecularArtifact.from_dict(artifacts_item_data)

                artifacts.append(artifacts_item)

        completed_at = d.pop("completed_at", UNSET)

        _confidence = d.pop("confidence", UNSET)
        confidence: list[ServiceBiomolecularJobResultConfidenceItem] | Unset = UNSET
        if _confidence is not UNSET:
            confidence = []
            for confidence_item_data in _confidence:
                confidence_item = ServiceBiomolecularJobResultConfidenceItem.from_dict(confidence_item_data)

                confidence.append(confidence_item)

        created_at = d.pop("created_at", UNSET)

        error = d.pop("error", UNSET)

        id = d.pop("id", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: ServiceBiomolecularJobResultMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ServiceBiomolecularJobResultMetadata.from_dict(_metadata)

        model = d.pop("model", UNSET)

        started_at = d.pop("started_at", UNSET)

        status = d.pop("status", UNSET)

        service_biomolecular_job_result = cls(
            affinity=affinity,
            artifacts=artifacts,
            completed_at=completed_at,
            confidence=confidence,
            created_at=created_at,
            error=error,
            id=id,
            metadata=metadata,
            model=model,
            started_at=started_at,
            status=status,
        )

        service_biomolecular_job_result.additional_properties = d
        return service_biomolecular_job_result

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
