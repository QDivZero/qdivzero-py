from enum import StrEnum


class ExecutionDecisionScoreQuestionType(StrEnum):
    SCORE = "score"

    def __str__(self) -> str:
        return str(self.value)
