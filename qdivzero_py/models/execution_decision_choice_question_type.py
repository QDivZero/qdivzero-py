from enum import StrEnum


class ExecutionDecisionChoiceQuestionType(StrEnum):
    CHOICE = "choice"

    def __str__(self) -> str:
        return str(self.value)
