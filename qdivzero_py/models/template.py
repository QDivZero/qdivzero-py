from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.timestamp import Timestamp
  from ..models.translation import Translation





T = TypeVar("T", bound="Template")



@_attrs_define
class Template:
    """ 
        Attributes:
            category (str | Unset):
            created_at (Timestamp | Unset):
            created_by (str | Unset):
            health_checked_at (Timestamp | Unset):
            health_error (str | Unset):
            health_status (str | Unset):
            id (str | Unset):
            is_active (bool | Unset):
            is_featured (bool | Unset):
            ordering (int | Unset):
            slug (str | Unset):
            tags (list[str] | Unset):
            translations (list[Translation] | Unset):
            updated_at (Timestamp | Unset):
            updated_by (str | Unset):
     """

    category: str | Unset = UNSET
    created_at: Timestamp | Unset = UNSET
    created_by: str | Unset = UNSET
    health_checked_at: Timestamp | Unset = UNSET
    health_error: str | Unset = UNSET
    health_status: str | Unset = UNSET
    id: str | Unset = UNSET
    is_active: bool | Unset = UNSET
    is_featured: bool | Unset = UNSET
    ordering: int | Unset = UNSET
    slug: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    translations: list[Translation] | Unset = UNSET
    updated_at: Timestamp | Unset = UNSET
    updated_by: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        category = self.category

        created_at: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.to_dict()

        created_by = self.created_by

        health_checked_at: dict[str, Any] | Unset = UNSET
        if not isinstance(self.health_checked_at, Unset):
            health_checked_at = self.health_checked_at.to_dict()

        health_error = self.health_error

        health_status = self.health_status

        id = self.id

        is_active = self.is_active

        is_featured = self.is_featured

        ordering = self.ordering

        slug = self.slug

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags



        translations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.translations, Unset):
            translations = []
            for translations_item_data in self.translations:
                translations_item = translations_item_data.to_dict()
                translations.append(translations_item)



        updated_at: dict[str, Any] | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.to_dict()

        updated_by = self.updated_by


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if category is not UNSET:
            field_dict["category"] = category
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if health_checked_at is not UNSET:
            field_dict["health_checked_at"] = health_checked_at
        if health_error is not UNSET:
            field_dict["health_error"] = health_error
        if health_status is not UNSET:
            field_dict["health_status"] = health_status
        if id is not UNSET:
            field_dict["id"] = id
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if is_featured is not UNSET:
            field_dict["is_featured"] = is_featured
        if ordering is not UNSET:
            field_dict["ordering"] = ordering
        if slug is not UNSET:
            field_dict["slug"] = slug
        if tags is not UNSET:
            field_dict["tags"] = tags
        if translations is not UNSET:
            field_dict["translations"] = translations
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.timestamp import Timestamp
        from ..models.translation import Translation
        d = dict(src_dict)
        category = d.pop("category", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Timestamp | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = Timestamp.from_dict(_created_at)




        created_by = d.pop("created_by", UNSET)

        _health_checked_at = d.pop("health_checked_at", UNSET)
        health_checked_at: Timestamp | Unset
        if isinstance(_health_checked_at,  Unset):
            health_checked_at = UNSET
        else:
            health_checked_at = Timestamp.from_dict(_health_checked_at)




        health_error = d.pop("health_error", UNSET)

        health_status = d.pop("health_status", UNSET)

        id = d.pop("id", UNSET)

        is_active = d.pop("is_active", UNSET)

        is_featured = d.pop("is_featured", UNSET)

        ordering = d.pop("ordering", UNSET)

        slug = d.pop("slug", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))


        _translations = d.pop("translations", UNSET)
        translations: list[Translation] | Unset = UNSET
        if _translations is not UNSET:
            translations = []
            for translations_item_data in _translations:
                translations_item = Translation.from_dict(translations_item_data)



                translations.append(translations_item)


        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Timestamp | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = Timestamp.from_dict(_updated_at)




        updated_by = d.pop("updated_by", UNSET)

        template = cls(
            category=category,
            created_at=created_at,
            created_by=created_by,
            health_checked_at=health_checked_at,
            health_error=health_error,
            health_status=health_status,
            id=id,
            is_active=is_active,
            is_featured=is_featured,
            ordering=ordering,
            slug=slug,
            tags=tags,
            translations=translations,
            updated_at=updated_at,
            updated_by=updated_by,
        )


        template.additional_properties = d
        return template

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
