from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResourceMetricSnapshot")


@_attrs_define
class ResourceMetricSnapshot:
    """
    Attributes:
        e2e_request_latency_p95_seconds (float | Unset):
        generation_tokens_per_second (float | Unset):
        generation_tokens_total (float | Unset):
        inter_token_latency_p95_seconds (float | Unset):
        kv_cache_usage_percent (float | Unset):
        prefix_cache_hit_percent (float | Unset):
        prompt_tokens_per_second (float | Unset):
        prompt_tokens_total (float | Unset):
        requests_running (float | Unset):
        requests_waiting (float | Unset):
        runtime_cpu_seconds_per_second (float | Unset):
        runtime_memory_bytes (float | Unset):
        sampled_at (str | Unset):
        time_to_first_token_p95_seconds (float | Unset):
    """

    e2e_request_latency_p95_seconds: float | Unset = UNSET
    generation_tokens_per_second: float | Unset = UNSET
    generation_tokens_total: float | Unset = UNSET
    inter_token_latency_p95_seconds: float | Unset = UNSET
    kv_cache_usage_percent: float | Unset = UNSET
    prefix_cache_hit_percent: float | Unset = UNSET
    prompt_tokens_per_second: float | Unset = UNSET
    prompt_tokens_total: float | Unset = UNSET
    requests_running: float | Unset = UNSET
    requests_waiting: float | Unset = UNSET
    runtime_cpu_seconds_per_second: float | Unset = UNSET
    runtime_memory_bytes: float | Unset = UNSET
    sampled_at: str | Unset = UNSET
    time_to_first_token_p95_seconds: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        e2e_request_latency_p95_seconds = self.e2e_request_latency_p95_seconds

        generation_tokens_per_second = self.generation_tokens_per_second

        generation_tokens_total = self.generation_tokens_total

        inter_token_latency_p95_seconds = self.inter_token_latency_p95_seconds

        kv_cache_usage_percent = self.kv_cache_usage_percent

        prefix_cache_hit_percent = self.prefix_cache_hit_percent

        prompt_tokens_per_second = self.prompt_tokens_per_second

        prompt_tokens_total = self.prompt_tokens_total

        requests_running = self.requests_running

        requests_waiting = self.requests_waiting

        runtime_cpu_seconds_per_second = self.runtime_cpu_seconds_per_second

        runtime_memory_bytes = self.runtime_memory_bytes

        sampled_at = self.sampled_at

        time_to_first_token_p95_seconds = self.time_to_first_token_p95_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if e2e_request_latency_p95_seconds is not UNSET:
            field_dict["e2e_request_latency_p95_seconds"] = e2e_request_latency_p95_seconds
        if generation_tokens_per_second is not UNSET:
            field_dict["generation_tokens_per_second"] = generation_tokens_per_second
        if generation_tokens_total is not UNSET:
            field_dict["generation_tokens_total"] = generation_tokens_total
        if inter_token_latency_p95_seconds is not UNSET:
            field_dict["inter_token_latency_p95_seconds"] = inter_token_latency_p95_seconds
        if kv_cache_usage_percent is not UNSET:
            field_dict["kv_cache_usage_percent"] = kv_cache_usage_percent
        if prefix_cache_hit_percent is not UNSET:
            field_dict["prefix_cache_hit_percent"] = prefix_cache_hit_percent
        if prompt_tokens_per_second is not UNSET:
            field_dict["prompt_tokens_per_second"] = prompt_tokens_per_second
        if prompt_tokens_total is not UNSET:
            field_dict["prompt_tokens_total"] = prompt_tokens_total
        if requests_running is not UNSET:
            field_dict["requests_running"] = requests_running
        if requests_waiting is not UNSET:
            field_dict["requests_waiting"] = requests_waiting
        if runtime_cpu_seconds_per_second is not UNSET:
            field_dict["runtime_cpu_seconds_per_second"] = runtime_cpu_seconds_per_second
        if runtime_memory_bytes is not UNSET:
            field_dict["runtime_memory_bytes"] = runtime_memory_bytes
        if sampled_at is not UNSET:
            field_dict["sampled_at"] = sampled_at
        if time_to_first_token_p95_seconds is not UNSET:
            field_dict["time_to_first_token_p95_seconds"] = time_to_first_token_p95_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        e2e_request_latency_p95_seconds = d.pop("e2e_request_latency_p95_seconds", UNSET)

        generation_tokens_per_second = d.pop("generation_tokens_per_second", UNSET)

        generation_tokens_total = d.pop("generation_tokens_total", UNSET)

        inter_token_latency_p95_seconds = d.pop("inter_token_latency_p95_seconds", UNSET)

        kv_cache_usage_percent = d.pop("kv_cache_usage_percent", UNSET)

        prefix_cache_hit_percent = d.pop("prefix_cache_hit_percent", UNSET)

        prompt_tokens_per_second = d.pop("prompt_tokens_per_second", UNSET)

        prompt_tokens_total = d.pop("prompt_tokens_total", UNSET)

        requests_running = d.pop("requests_running", UNSET)

        requests_waiting = d.pop("requests_waiting", UNSET)

        runtime_cpu_seconds_per_second = d.pop("runtime_cpu_seconds_per_second", UNSET)

        runtime_memory_bytes = d.pop("runtime_memory_bytes", UNSET)

        sampled_at = d.pop("sampled_at", UNSET)

        time_to_first_token_p95_seconds = d.pop("time_to_first_token_p95_seconds", UNSET)

        resource_metric_snapshot = cls(
            e2e_request_latency_p95_seconds=e2e_request_latency_p95_seconds,
            generation_tokens_per_second=generation_tokens_per_second,
            generation_tokens_total=generation_tokens_total,
            inter_token_latency_p95_seconds=inter_token_latency_p95_seconds,
            kv_cache_usage_percent=kv_cache_usage_percent,
            prefix_cache_hit_percent=prefix_cache_hit_percent,
            prompt_tokens_per_second=prompt_tokens_per_second,
            prompt_tokens_total=prompt_tokens_total,
            requests_running=requests_running,
            requests_waiting=requests_waiting,
            runtime_cpu_seconds_per_second=runtime_cpu_seconds_per_second,
            runtime_memory_bytes=runtime_memory_bytes,
            sampled_at=sampled_at,
            time_to_first_token_p95_seconds=time_to_first_token_p95_seconds,
        )

        resource_metric_snapshot.additional_properties = d
        return resource_metric_snapshot

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
