from enum import StrEnum


class ExecutionDecisionNoulQuestionType(StrEnum):
    NOUL = "noul"

    def __str__(self) -> str:
        return str(self.value)
