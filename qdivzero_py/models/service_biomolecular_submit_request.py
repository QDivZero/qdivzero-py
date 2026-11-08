from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_biomolecular_attachment import ServiceBiomolecularAttachment
    from ..models.service_biomolecular_options import ServiceBiomolecularOptions
    from ..models.service_biomolecular_submit_request_input import ServiceBiomolecularSubmitRequestInput


T = TypeVar("T", bound="ServiceBiomolecularSubmitRequest")


@_attrs_define
class ServiceBiomolecularSubmitRequest:
    """
    Attributes:
        input_ (ServiceBiomolecularSubmitRequestInput):
        model (str):
        attachments (list[ServiceBiomolecularAttachment] | Unset):
        options (ServiceBiomolecularOptions | Unset):
    """

    input_: ServiceBiomolecularSubmitRequestInput
    model: str
    attachments: list[ServiceBiomolecularAttachment] | Unset = UNSET
    options: ServiceBiomolecularOptions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_ = self.input_.to_dict()

        model = self.model

        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)

        options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "input": input_,
                "model": model,
            }
        )
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_biomolecular_attachment import ServiceBiomolecularAttachment
        from ..models.service_biomolecular_options import ServiceBiomolecularOptions
        from ..models.service_biomolecular_submit_request_input import ServiceBiomolecularSubmitRequestInput

        d = dict(src_dict)
        input_ = ServiceBiomolecularSubmitRequestInput.from_dict(d.pop("input"))

        model = d.pop("model")

        _attachments = d.pop("attachments", UNSET)
        attachments: list[ServiceBiomolecularAttachment] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = ServiceBiomolecularAttachment.from_dict(attachments_item_data)

                attachments.append(attachments_item)

        _options = d.pop("options", UNSET)
        options: ServiceBiomolecularOptions | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = ServiceBiomolecularOptions.from_dict(_options)

        service_biomolecular_submit_request = cls(
            input_=input_,
            model=model,
            attachments=attachments,
            options=options,
        )

        service_biomolecular_submit_request.additional_properties = d
        return service_biomolecular_submit_request

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
