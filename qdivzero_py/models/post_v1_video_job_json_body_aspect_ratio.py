from enum import StrEnum


class PostV1VideoJobJsonBodyAspectRatio(StrEnum):
    ADAPTIVE = "adaptive"
    VALUE_0 = "21:9"
    VALUE_1 = "16:9"
    VALUE_2 = "4:3"
    VALUE_3 = "1:1"
    VALUE_4 = "3:4"
    VALUE_5 = "9:16"

    def __str__(self) -> str:
        return str(self.value)
