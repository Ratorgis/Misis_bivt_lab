import pytest

from src.lab_02.arrays import min_max, unique_sorted, flatten
from src.lab_02.matrix import transpose, row_sums, col_sums
from src.lab_02.tuples import student_registration


@pytest.mark.parametrize(
    "source, expected",
    [
        ([3, -1, 5, 5, 0], (-1, 5)),
        ([42], (42, 42)),
        ([], ValueError),
        ([1.5, 2, 2.0, -3.1], (-3.1, 2)),
    ],
)
def test_min_max(source, expected):
    if source == []:
        with pytest.raises(ValueError, match="nums list is empty"):
            min_max(source) == expected
    else:
        assert min_max(source) == expected


@pytest.mark.parametrize(
    "source, expected",
    [
        ([3, 1, 2, 1, 3], [1, 2, 3]),
        ([], []),
        ([1.0, 1, 2.5, 2.5, 0], [0, 1.0, 2.5]),
    ],
)
def test_unique_sorted(source, expected):
    assert unique_sorted(source) == expected


@pytest.mark.parametrize(
    "source, expected",
    [
        ([[1], [], [2, 3]], [1, 2, 3]),
        ([[1, 2], (3, 4, 5)], [1, 2, 3, 4, 5]),
        ([[1, 2], "ab"], TypeError),
    ],
)
def test_flatten(source, expected):
    if source == [[1, 2], "ab"]:
        with pytest.raises(TypeError, match="row is not a row of rows of a matrix"):
            flatten(source) == expected
    else:
        assert flatten(source) == expected


@pytest.mark.parametrize(
    "source, expected",
    [
        ([[1, 2, 3]], [[1], [2], [3]]),
        ([], []),
        ([[1, 2], [3]], ValueError),
    ],
)
def test_transpose(source, expected):
    if source == [[1, 2], [3]]:
        with pytest.raises(ValueError, match="Torn matrix"):
            transpose(source) == expected
    else:
        assert transpose(source) == expected


@pytest.mark.parametrize(
    "source, expected",
    [
        ([[-1, 1], [10, -10]], [0, 0]),
        ([[0, 0], [0, 0]], [0, 0]),
        ([[1, 2], [3]], ValueError),
    ],
)
def test_row_sums(source, expected):
    if source == [[1, 2], [3]]:
        with pytest.raises(ValueError, match="Torn matrix"):
            row_sums(source) == expected
    else:
        assert row_sums(source) == expected


@pytest.mark.parametrize(
    "source, expected",
    [
        ([[-1, 1], [10, -10]], [9, -9]),
        ([[0, 0], [0, 0]], [0, 0]),
        ([[1, 2], [3]], ValueError),
    ],
)
def test_col_sums(source, expected):
    if source == [[1, 2], [3]]:
        with pytest.raises(ValueError, match="Torn matrix"):
            col_sums(source) == expected
    else:
        assert col_sums(source) == expected


@pytest.mark.parametrize(
    "fio, group, gpa, expected",
    [
        ("Петров Пётр", "IKBO-12", 5.0, "Петров П., гр. IKBO-12, GPA 5.0"),
        (1, "IKBO-12", 5.0, TypeError),
        ("Петров Пётр", 2, 5.0, TypeError),
        ("Петров Пётр", "IKBO-12", 3, TypeError),
        ("Петров", "IKBO-12", 5.0, ValueError),
        ("Петров Пётр Петрович", "IKBO-12", 5.0, "Петров П.П., гр. IKBO-12, GPA 5.0"),
        (
            "  сидорова  анна   сергеевна ",
            "ABB-01",
            3.999,
            "Сидорова А.С., гр. ABB-01, GPA 4.0",
        ),
    ],
)
def test_student_registration(fio, group, gpa, expected):
    if fio == 1:
        with pytest.raises(TypeError, match="Fio must to be str"):
            student_registration(fio, group, gpa) == expected
    elif len(fio.split()) == 1:
        with pytest.raises(ValueError, match="Too short fio"):
            student_registration(fio, group, gpa) == expected
    elif group == 2:
        with pytest.raises(TypeError, match="Group must to be str"):
            student_registration(fio, group, gpa) == expected
    elif gpa == 3:
        with pytest.raises(TypeError, match="GPA must to be float"):
            student_registration(fio, group, gpa) == expected
    else:
        assert student_registration(fio, group, gpa) == expected
