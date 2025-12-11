from pathlib import Path

from src.lab_08.models import Student
from src.lib.text import write_json, json_reader


def student_to_json(student: list[Student], path_to_json: Path) -> None:
    content = [one.to_dict() for one in student]
    write_json(content, path_to_json)


def student_from_json(path_to_json: Path) -> list[Student]:
    content = json_reader(path_to_json)
    result = [
        Student(
            one.get("fio", None),
            one.get("birthdate", None),
            one.get("group", None),
            one.get("gpa", None),
        )
        for one in content
    ]
    return result


if __name__ == "__main__":
    max = Student("Max Ryabov Anatol", "04082007", "Misis", 3.3)
    student_to_json([max], "src/data/samples/people.json")
