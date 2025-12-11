from pathlib import Path
from dataclasses import dataclass

from src.lib.text import csv_reader
from src.lab_04.io_text_csv import write_csv
from src.lab_08.models import Student


@dataclass
class Group:
    path_to_csv: str | Path
    content = None

    def __post_init__(self):
        self._read_all()

    def _read_all(self):
        self.content = csv_reader(self.path_to_csv)

    def list(self) -> list[Student]:
        return [
            Student.from_dict(
                {
                    "fio": row[0],
                    "birthdate": row[1],
                    "group": row[2],
                    "gpa": float(row[3]),
                }
            )
            for row in self.content[1:]
        ]

    def add(self, student: Student) -> None:
        new_student = [
            student.fio,
            str(student.birthdate),
            student.group,
            str(student.gpa),
        ]
        self.content.append(new_student)
        write_csv(self.content[1:], self.path_to_csv, self.content[0])
        self._read_all()

    def find(self, substr: str) -> Student:
        for one in self.content[1:]:
            if substr in one[0]:
                return Student(one[0], one[1], one[2], float(one[3]))

    def remove(self, fio: str) -> None:
        self.content = [one for one in self.content if not (fio in one[0])]
        write_csv(self.content[1:], self.path_to_csv, self.content[0])
        self._read_all()

    def update(self, fio: str, **kargs) -> None:
        new_content = []

        for row in self.content:
            if fio in row[0]:
                new_row = [
                    kargs.get("fio", row[0]),
                    kargs.get("birthdate", row[1]),
                    kargs.get("group", row[2]),
                    kargs.get("gpa", row[3]),
                ]
                new_content.append(new_row)
            else:
                new_content.append(row)

        self.content = new_content


if __name__ == "__main__":
    group = Group("src/data/lab_09/students.csv")
    group.remove("Arina")
    print(group.list())
