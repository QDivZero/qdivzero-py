from enum import StrEnum


class PricingStatus(StrEnum):
    PRICING_ESTIMATED = "estimated"
    PRICING_UNAVAILABLE = "unavailable"

    def __str__(self) -> str:
        return str(self.value)
