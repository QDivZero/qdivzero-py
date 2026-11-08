from enum import StrEnum


class ExecutionDecisionScoreAnswerType(StrEnum):
    SCORE = "score"

    def __str__(self) -> str:
        return str(self.value)
