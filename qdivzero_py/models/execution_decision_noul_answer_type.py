from enum import StrEnum


class ExecutionDecisionNoulAnswerType(StrEnum):
    NOUL = "noul"

    def __str__(self) -> str:
        return str(self.value)
