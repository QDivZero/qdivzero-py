from enum import StrEnum


class PreviewInstanceRequestWorkloadKind(StrEnum):
    DECISION = "decision"

    def __str__(self) -> str:
        return str(self.value)
