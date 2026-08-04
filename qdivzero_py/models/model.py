from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pricing_status import PricingStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.recommended_gpu import RecommendedGPU





T = TypeVar("T", bound="Model")



@_attrs_define
class Model:
    """ 
        Attributes:
            display_name (str | Unset):
            downloads (int | Unset):
            likes (int | Unset):
            organization (str | Unset):
            organization_logo_url (str | Unset):
            pipeline_tag (str | Unset):
            price_eur_per_hour (float | Unset):
            pricing_status (PricingStatus | Unset):
            recommended_gpu (RecommendedGPU | Unset):
            repo_id (str | Unset):
            tags (list[str] | Unset):
     """

    display_name: str | Unset = UNSET
    downloads: int | Unset = UNSET
    likes: int | Unset = UNSET
    organization: str | Unset = UNSET
    organization_logo_url: str | Unset = UNSET
    pipeline_tag: str | Unset = UNSET
    price_eur_per_hour: float | Unset = UNSET
    pricing_status: PricingStatus | Unset = UNSET
    recommended_gpu: RecommendedGPU | Unset = UNSET
    repo_id: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        downloads = self.downloads

        likes = self.likes

        organization = self.organization

        organization_logo_url = self.organization_logo_url

        pipeline_tag = self.pipeline_tag

        price_eur_per_hour = self.price_eur_per_hour

        pricing_status: str | Unset = UNSET
        if not isinstance(self.pricing_status, Unset):
            pricing_status = self.pricing_status.value


        recommended_gpu: dict[str, Any] | Unset = UNSET
        if not isinstance(self.recommended_gpu, Unset):
            recommended_gpu = self.recommended_gpu.to_dict()

        repo_id = self.repo_id

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if downloads is not UNSET:
            field_dict["downloads"] = downloads
        if likes is not UNSET:
            field_dict["likes"] = likes
        if organization is not UNSET:
            field_dict["organization"] = organization
        if organization_logo_url is not UNSET:
            field_dict["organization_logo_url"] = organization_logo_url
        if pipeline_tag is not UNSET:
            field_dict["pipeline_tag"] = pipeline_tag
        if price_eur_per_hour is not UNSET:
            field_dict["price_eur_per_hour"] = price_eur_per_hour
        if pricing_status is not UNSET:
            field_dict["pricing_status"] = pricing_status
        if recommended_gpu is not UNSET:
            field_dict["recommended_gpu"] = recommended_gpu
        if repo_id is not UNSET:
            field_dict["repo_id"] = repo_id
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.recommended_gpu import RecommendedGPU
        d = dict(src_dict)
        display_name = d.pop("display_name", UNSET)

        downloads = d.pop("downloads", UNSET)

        likes = d.pop("likes", UNSET)

        organization = d.pop("organization", UNSET)

        organization_logo_url = d.pop("organization_logo_url", UNSET)

        pipeline_tag = d.pop("pipeline_tag", UNSET)

        price_eur_per_hour = d.pop("price_eur_per_hour", UNSET)

        _pricing_status = d.pop("pricing_status", UNSET)
        pricing_status: PricingStatus | Unset
        if isinstance(_pricing_status,  Unset):
            pricing_status = UNSET
        else:
            pricing_status = PricingStatus(_pricing_status)




        _recommended_gpu = d.pop("recommended_gpu", UNSET)
        recommended_gpu: RecommendedGPU | Unset
        if isinstance(_recommended_gpu,  Unset):
            recommended_gpu = UNSET
        else:
            recommended_gpu = RecommendedGPU.from_dict(_recommended_gpu)




        repo_id = d.pop("repo_id", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))


        model = cls(
            display_name=display_name,
            downloads=downloads,
            likes=likes,
            organization=organization,
            organization_logo_url=organization_logo_url,
            pipeline_tag=pipeline_tag,
            price_eur_per_hour=price_eur_per_hour,
            pricing_status=pricing_status,
            recommended_gpu=recommended_gpu,
            repo_id=repo_id,
            tags=tags,
        )


        model.additional_properties = d
        return model

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
