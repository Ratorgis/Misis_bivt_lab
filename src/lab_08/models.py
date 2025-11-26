import datetime
from dataclasses import dataclass


@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        try:
            self.birthdate = datetime.strptime(self.birthdate, "%Y/%m/%d")
        except ValueError:
            raise ValueError("Invalid date of birth format")

        if self.fio is not str:
            raise TypeError("Fio must be str format")

        if len(self.fio.split()) != 3:
            raise ValueError("FIO must contain exactly 3 words")

        if not (0 <= self.gpa <= 10):
            raise ValueError("Gpa must be between 0 and 10")

    def age(self) -> int:
        birthdate = self.birthdate
        today = datetime.date.today()
        age = (
            today.year
            - birthdate.year
            - ((today.month, today.day) < (birthdate.month, birthdate.day))
        )
        return age

    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate.strftime("%Y/%m/%d"),
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, d: dict):
        required = ["fio", "birthdate", "group", "gpa"]
        if not all(key in d for key in required):
            raise ValueError("Dict must contain fio, birthdate, group, gpa")

        return cls(
            fio=d["fio"],
            birthdate=d["birthdate"],
            group=d["group"],
            gpa=d["gpa"],
        )

    def __str__(self):
        return f"{self.fio}, {self.group}, {self.birthdate.strftime('%Y/%m/%d')}, GPA: {self.gpa}"
