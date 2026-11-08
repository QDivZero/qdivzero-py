from enum import StrEnum


class PostV1VideoGenerationsJsonBodyTask(StrEnum):
    FL2VA = "fl2va"
    I2V = "i2v"
    REF2VA = "ref2va"
    T2V = "t2v"
    T2VA = "t2va"

    def __str__(self) -> str:
        return str(self.value)
