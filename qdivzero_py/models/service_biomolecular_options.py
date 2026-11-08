from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceBiomolecularOptions")


@_attrs_define
class ServiceBiomolecularOptions:
    """
    Attributes:
        affinity_mw_correction (bool | Unset):
        diffusion_samples (int | Unset):
        diffusion_samples_affinity (int | Unset):
        max_msa_seqs (int | Unset):
        msa_pairing_strategy (str | Unset):
        output_format (str | Unset):
        recycling_steps (int | Unset):
        sampling_steps (int | Unset):
        sampling_steps_affinity (int | Unset):
        seed (int | Unset):
        use_msa_server (bool | Unset):
        use_potentials (bool | Unset):
    """

    affinity_mw_correction: bool | Unset = UNSET
    diffusion_samples: int | Unset = UNSET
    diffusion_samples_affinity: int | Unset = UNSET
    max_msa_seqs: int | Unset = UNSET
    msa_pairing_strategy: str | Unset = UNSET
    output_format: str | Unset = UNSET
    recycling_steps: int | Unset = UNSET
    sampling_steps: int | Unset = UNSET
    sampling_steps_affinity: int | Unset = UNSET
    seed: int | Unset = UNSET
    use_msa_server: bool | Unset = UNSET
    use_potentials: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affinity_mw_correction = self.affinity_mw_correction

        diffusion_samples = self.diffusion_samples

        diffusion_samples_affinity = self.diffusion_samples_affinity

        max_msa_seqs = self.max_msa_seqs

        msa_pairing_strategy = self.msa_pairing_strategy

        output_format = self.output_format

        recycling_steps = self.recycling_steps

        sampling_steps = self.sampling_steps

        sampling_steps_affinity = self.sampling_steps_affinity

        seed = self.seed

        use_msa_server = self.use_msa_server

        use_potentials = self.use_potentials

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affinity_mw_correction is not UNSET:
            field_dict["affinity_mw_correction"] = affinity_mw_correction
        if diffusion_samples is not UNSET:
            field_dict["diffusion_samples"] = diffusion_samples
        if diffusion_samples_affinity is not UNSET:
            field_dict["diffusion_samples_affinity"] = diffusion_samples_affinity
        if max_msa_seqs is not UNSET:
            field_dict["max_msa_seqs"] = max_msa_seqs
        if msa_pairing_strategy is not UNSET:
            field_dict["msa_pairing_strategy"] = msa_pairing_strategy
        if output_format is not UNSET:
            field_dict["output_format"] = output_format
        if recycling_steps is not UNSET:
            field_dict["recycling_steps"] = recycling_steps
        if sampling_steps is not UNSET:
            field_dict["sampling_steps"] = sampling_steps
        if sampling_steps_affinity is not UNSET:
            field_dict["sampling_steps_affinity"] = sampling_steps_affinity
        if seed is not UNSET:
            field_dict["seed"] = seed
        if use_msa_server is not UNSET:
            field_dict["use_msa_server"] = use_msa_server
        if use_potentials is not UNSET:
            field_dict["use_potentials"] = use_potentials

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        affinity_mw_correction = d.pop("affinity_mw_correction", UNSET)

        diffusion_samples = d.pop("diffusion_samples", UNSET)

        diffusion_samples_affinity = d.pop("diffusion_samples_affinity", UNSET)

        max_msa_seqs = d.pop("max_msa_seqs", UNSET)

        msa_pairing_strategy = d.pop("msa_pairing_strategy", UNSET)

        output_format = d.pop("output_format", UNSET)

        recycling_steps = d.pop("recycling_steps", UNSET)

        sampling_steps = d.pop("sampling_steps", UNSET)

        sampling_steps_affinity = d.pop("sampling_steps_affinity", UNSET)

        seed = d.pop("seed", UNSET)

        use_msa_server = d.pop("use_msa_server", UNSET)

        use_potentials = d.pop("use_potentials", UNSET)

        service_biomolecular_options = cls(
            affinity_mw_correction=affinity_mw_correction,
            diffusion_samples=diffusion_samples,
            diffusion_samples_affinity=diffusion_samples_affinity,
            max_msa_seqs=max_msa_seqs,
            msa_pairing_strategy=msa_pairing_strategy,
            output_format=output_format,
            recycling_steps=recycling_steps,
            sampling_steps=sampling_steps,
            sampling_steps_affinity=sampling_steps_affinity,
            seed=seed,
            use_msa_server=use_msa_server,
            use_potentials=use_potentials,
        )

        service_biomolecular_options.additional_properties = d
        return service_biomolecular_options

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
