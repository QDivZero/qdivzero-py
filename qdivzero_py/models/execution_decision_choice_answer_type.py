from enum import StrEnum


class ExecutionDecisionChoiceAnswerType(StrEnum):
    CHOICE = "choice"

    def __str__(self) -> str:
        return str(self.value)
