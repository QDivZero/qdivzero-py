from enum import StrEnum


class CreateInstanceRequestWorkloadKind(StrEnum):
    DECISION = "decision"

    def __str__(self) -> str:
        return str(self.value)
