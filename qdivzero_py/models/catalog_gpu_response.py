from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CatalogGPUResponse")


@_attrs_define
class CatalogGPUResponse:
    """
    Attributes:
        availability_count (int | Unset):
        availability_total (int | Unset):
        capacity_tier (str | Unset):
        city (str | Unset):
        compute_tflops (float | Unset):
        continent (str | Unset):
        country (str | Unset):
        cpu_cores (int | Unset):
        cpu_name (str | Unset):
        cpu_ram_gb (int | Unset):
        cuda_max_good (float | Unset):
        disk_bandwidth_mbps (float | Unset):
        display_name (str | Unset):
        download_size_bytes (int | Unset):
        enabled (bool | Unset):
        estimated_download_cost_eur (float | Unset):
        estimated_one_hour_cost_eur (float | Unset):
        estimated_spot_reserve_eur (float | Unset):
        gpu_count (int | Unset):
        internet_down_mbps (float | Unset):
        internet_up_mbps (float | Unset):
        market_type (str | Unset):
        network_download_price_per_gb_eur (float | Unset):
        network_estimate_available (bool | Unset):
        network_pricing_known (bool | Unset):
        network_upload_price_per_gb_eur (float | Unset):
        price_per_hour_eur (float | Unset):
        provider_codename (str | Unset):
        public_gpu_id (str | Unset):
        reliability (float | Unset):
        stock_status (str | Unset):
        vram_gb (float | Unset):
    """

    availability_count: int | Unset = UNSET
    availability_total: int | Unset = UNSET
    capacity_tier: str | Unset = UNSET
    city: str | Unset = UNSET
    compute_tflops: float | Unset = UNSET
    continent: str | Unset = UNSET
    country: str | Unset = UNSET
    cpu_cores: int | Unset = UNSET
    cpu_name: str | Unset = UNSET
    cpu_ram_gb: int | Unset = UNSET
    cuda_max_good: float | Unset = UNSET
    disk_bandwidth_mbps: float | Unset = UNSET
    display_name: str | Unset = UNSET
    download_size_bytes: int | Unset = UNSET
    enabled: bool | Unset = UNSET
    estimated_download_cost_eur: float | Unset = UNSET
    estimated_one_hour_cost_eur: float | Unset = UNSET
    estimated_spot_reserve_eur: float | Unset = UNSET
    gpu_count: int | Unset = UNSET
    internet_down_mbps: float | Unset = UNSET
    internet_up_mbps: float | Unset = UNSET
    market_type: str | Unset = UNSET
    network_download_price_per_gb_eur: float | Unset = UNSET
    network_estimate_available: bool | Unset = UNSET
    network_pricing_known: bool | Unset = UNSET
    network_upload_price_per_gb_eur: float | Unset = UNSET
    price_per_hour_eur: float | Unset = UNSET
    provider_codename: str | Unset = UNSET
    public_gpu_id: str | Unset = UNSET
    reliability: float | Unset = UNSET
    stock_status: str | Unset = UNSET
    vram_gb: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        availability_count = self.availability_count

        availability_total = self.availability_total

        capacity_tier = self.capacity_tier

        city = self.city

        compute_tflops = self.compute_tflops

        continent = self.continent

        country = self.country

        cpu_cores = self.cpu_cores

        cpu_name = self.cpu_name

        cpu_ram_gb = self.cpu_ram_gb

        cuda_max_good = self.cuda_max_good

        disk_bandwidth_mbps = self.disk_bandwidth_mbps

        display_name = self.display_name

        download_size_bytes = self.download_size_bytes

        enabled = self.enabled

        estimated_download_cost_eur = self.estimated_download_cost_eur

        estimated_one_hour_cost_eur = self.estimated_one_hour_cost_eur

        estimated_spot_reserve_eur = self.estimated_spot_reserve_eur

        gpu_count = self.gpu_count

        internet_down_mbps = self.internet_down_mbps

        internet_up_mbps = self.internet_up_mbps

        market_type = self.market_type

        network_download_price_per_gb_eur = self.network_download_price_per_gb_eur

        network_estimate_available = self.network_estimate_available

        network_pricing_known = self.network_pricing_known

        network_upload_price_per_gb_eur = self.network_upload_price_per_gb_eur

        price_per_hour_eur = self.price_per_hour_eur

        provider_codename = self.provider_codename

        public_gpu_id = self.public_gpu_id

        reliability = self.reliability

        stock_status = self.stock_status

        vram_gb = self.vram_gb

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if availability_count is not UNSET:
            field_dict["availability_count"] = availability_count
        if availability_total is not UNSET:
            field_dict["availability_total"] = availability_total
        if capacity_tier is not UNSET:
            field_dict["capacity_tier"] = capacity_tier
        if city is not UNSET:
            field_dict["city"] = city
        if compute_tflops is not UNSET:
            field_dict["compute_tflops"] = compute_tflops
        if continent is not UNSET:
            field_dict["continent"] = continent
        if country is not UNSET:
            field_dict["country"] = country
        if cpu_cores is not UNSET:
            field_dict["cpu_cores"] = cpu_cores
        if cpu_name is not UNSET:
            field_dict["cpu_name"] = cpu_name
        if cpu_ram_gb is not UNSET:
            field_dict["cpu_ram_gb"] = cpu_ram_gb
        if cuda_max_good is not UNSET:
            field_dict["cuda_max_good"] = cuda_max_good
        if disk_bandwidth_mbps is not UNSET:
            field_dict["disk_bandwidth_mbps"] = disk_bandwidth_mbps
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if download_size_bytes is not UNSET:
            field_dict["download_size_bytes"] = download_size_bytes
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if estimated_download_cost_eur is not UNSET:
            field_dict["estimated_download_cost_eur"] = estimated_download_cost_eur
        if estimated_one_hour_cost_eur is not UNSET:
            field_dict["estimated_one_hour_cost_eur"] = estimated_one_hour_cost_eur
        if estimated_spot_reserve_eur is not UNSET:
            field_dict["estimated_spot_reserve_eur"] = estimated_spot_reserve_eur
        if gpu_count is not UNSET:
            field_dict["gpu_count"] = gpu_count
        if internet_down_mbps is not UNSET:
            field_dict["internet_down_mbps"] = internet_down_mbps
        if internet_up_mbps is not UNSET:
            field_dict["internet_up_mbps"] = internet_up_mbps
        if market_type is not UNSET:
            field_dict["market_type"] = market_type
        if network_download_price_per_gb_eur is not UNSET:
            field_dict["network_download_price_per_gb_eur"] = network_download_price_per_gb_eur
        if network_estimate_available is not UNSET:
            field_dict["network_estimate_available"] = network_estimate_available
        if network_pricing_known is not UNSET:
            field_dict["network_pricing_known"] = network_pricing_known
        if network_upload_price_per_gb_eur is not UNSET:
            field_dict["network_upload_price_per_gb_eur"] = network_upload_price_per_gb_eur
        if price_per_hour_eur is not UNSET:
            field_dict["price_per_hour_eur"] = price_per_hour_eur
        if provider_codename is not UNSET:
            field_dict["provider_codename"] = provider_codename
        if public_gpu_id is not UNSET:
            field_dict["public_gpu_id"] = public_gpu_id
        if reliability is not UNSET:
            field_dict["reliability"] = reliability
        if stock_status is not UNSET:
            field_dict["stock_status"] = stock_status
        if vram_gb is not UNSET:
            field_dict["vram_gb"] = vram_gb

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        availability_count = d.pop("availability_count", UNSET)

        availability_total = d.pop("availability_total", UNSET)

        capacity_tier = d.pop("capacity_tier", UNSET)

        city = d.pop("city", UNSET)

        compute_tflops = d.pop("compute_tflops", UNSET)

        continent = d.pop("continent", UNSET)

        country = d.pop("country", UNSET)

        cpu_cores = d.pop("cpu_cores", UNSET)

        cpu_name = d.pop("cpu_name", UNSET)

        cpu_ram_gb = d.pop("cpu_ram_gb", UNSET)

        cuda_max_good = d.pop("cuda_max_good", UNSET)

        disk_bandwidth_mbps = d.pop("disk_bandwidth_mbps", UNSET)

        display_name = d.pop("display_name", UNSET)

        download_size_bytes = d.pop("download_size_bytes", UNSET)

        enabled = d.pop("enabled", UNSET)

        estimated_download_cost_eur = d.pop("estimated_download_cost_eur", UNSET)

        estimated_one_hour_cost_eur = d.pop("estimated_one_hour_cost_eur", UNSET)

        estimated_spot_reserve_eur = d.pop("estimated_spot_reserve_eur", UNSET)

        gpu_count = d.pop("gpu_count", UNSET)

        internet_down_mbps = d.pop("internet_down_mbps", UNSET)

        internet_up_mbps = d.pop("internet_up_mbps", UNSET)

        market_type = d.pop("market_type", UNSET)

        network_download_price_per_gb_eur = d.pop("network_download_price_per_gb_eur", UNSET)

        network_estimate_available = d.pop("network_estimate_available", UNSET)

        network_pricing_known = d.pop("network_pricing_known", UNSET)

        network_upload_price_per_gb_eur = d.pop("network_upload_price_per_gb_eur", UNSET)

        price_per_hour_eur = d.pop("price_per_hour_eur", UNSET)

        provider_codename = d.pop("provider_codename", UNSET)

        public_gpu_id = d.pop("public_gpu_id", UNSET)

        reliability = d.pop("reliability", UNSET)

        stock_status = d.pop("stock_status", UNSET)

        vram_gb = d.pop("vram_gb", UNSET)

        catalog_gpu_response = cls(
            availability_count=availability_count,
            availability_total=availability_total,
            capacity_tier=capacity_tier,
            city=city,
            compute_tflops=compute_tflops,
            continent=continent,
            country=country,
            cpu_cores=cpu_cores,
            cpu_name=cpu_name,
            cpu_ram_gb=cpu_ram_gb,
            cuda_max_good=cuda_max_good,
            disk_bandwidth_mbps=disk_bandwidth_mbps,
            display_name=display_name,
            download_size_bytes=download_size_bytes,
            enabled=enabled,
            estimated_download_cost_eur=estimated_download_cost_eur,
            estimated_one_hour_cost_eur=estimated_one_hour_cost_eur,
            estimated_spot_reserve_eur=estimated_spot_reserve_eur,
            gpu_count=gpu_count,
            internet_down_mbps=internet_down_mbps,
            internet_up_mbps=internet_up_mbps,
            market_type=market_type,
            network_download_price_per_gb_eur=network_download_price_per_gb_eur,
            network_estimate_available=network_estimate_available,
            network_pricing_known=network_pricing_known,
            network_upload_price_per_gb_eur=network_upload_price_per_gb_eur,
            price_per_hour_eur=price_per_hour_eur,
            provider_codename=provider_codename,
            public_gpu_id=public_gpu_id,
            reliability=reliability,
            stock_status=stock_status,
            vram_gb=vram_gb,
        )

        catalog_gpu_response.additional_properties = d
        return catalog_gpu_response

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
