import pytest

from src.lab_01.tasks_lab_01 import (
    greeting,
    sum_avg,
    discount_vat,
    minutes_to_hhmm,
    initials_and_len,
    attendance,
    transcript,
)


@pytest.mark.parametrize(
    "name, age, expected",
    [
        ("Max", 17, "Привет, Max! Через год тебе будет 18"),
        ("Anna", 30, "Привет, Anna! Через год тебе будет 31"),
        ("Леонид", 0, "Привет, Леонид! Через год тебе будет 1"),
        ("Юля", 99, "Привет, Юля! Через год тебе будет 100"),
    ],
)
def test_greeting(name, age, expected):
    assert greeting(name, age) == expected


@pytest.mark.parametrize(
    "a_input, b_input, expected",
    [
        (2, 3, "sum = 5; avg = 2.5"),
        (1.5, 2.5, "sum = 4.0; avg = 2.0"),
        (0, 0, "sum = 0; avg = 0.0"),
        (-1, 1, "sum = 0; avg = 0.0"),
    ],
)
def test_sum_avg(a_input, b_input, expected):
    assert sum_avg(a_input, b_input) == expected


@pytest.mark.parametrize(
    "price, discount, vat, expected",
    [
        (
            100,
            10,
            20,
            ["База полсе скидки: 90.0", "НДС: 90.0", "Итого к оплате: 108.0"],
        ),
        (
            200,
            0,
            10,
            ["База полсе скидки: 200.0", "НДС: 200.0", "Итого к оплате: 220.0"],
        ),
        (50, 50, 0, ["База полсе скидки: 25.0", "НДС: 25.0", "Итого к оплате: 25.0"]),
        (0, 0, 0, ["База полсе скидки: 0.0", "НДС: 0.0", "Итого к оплате: 0.0"]),
    ],
)
def test_discount_vat(price, discount, vat, expected):
    assert discount_vat(price, discount, vat) == expected


@pytest.mark.parametrize(
    "mns, expected",
    [
        (60, "1:0"),
        (61, "1:1"),
        (0, "0:0"),
        (125, "2:5"),
    ],
)
def test_minutes_to_hhmm(mns, expected):
    assert minutes_to_hhmm(mns) == expected


@pytest.mark.parametrize(
    "names, expected",
    [
        (["Сергей", "Серый", "Сергеевич"], ["Инициалы: ССС", "Длина (символы): 22"]),
        (["Алексей", "Борис", "Вера"], ["Инициалы: АБВ", "Длина (символы): 18"]),
        (["A", "B", "C"], ["Инициалы: ABC", "Длина (символы): 5"]),
        (["John", "Doe", "Ray"], ["Инициалы: JDR", "Длина (символы): 12"]),
    ],
)
def test_initials_and_len(names, expected):
    assert initials_and_len(names) == expected


@pytest.mark.parametrize(
    "visitors, expected",
    [
        (
            [
                ["Max", "Leo", 18, True],
                ["Anna", "Ivan", 20, False],
                ["John", "Doe", 22, True],
            ],
            "out: 2, 1",
        ),
        ([["A", "B", 18, True], ["C", "D", 19, True]], "out: 2, 0"),
        ([["A", "B", 18, False], ["C", "D", 19, False]], "out: 0, 2"),
        (
            [
                ["X", "Y", 20, True],
                ["P", "Q", 21, False],
                ["R", "S", 22, True],
                ["T", "U", 23, False],
            ],
            "out: 2, 2",
        ),
        (
            [
                ["John", "Smith", 30, True],
                ["Mary", "Jane", 25, True],
                ["Bob", "Brown", 40, True],
            ],
            "out: 3, 0",
        ),
        (
            [
                ["Alice", "White", 19, False],
                ["Tom", "Black", 21, False],
                ["Eve", "Green", 22, False],
            ],
            "out: 0, 3",
        ),
        (
            [
                ["Mike", "Blue", 20, True],
                ["Sue", "Red", 22, False],
                ["Jim", "Gray", 21, True],
                ["Kim", "Pink", 23, False],
            ],
            "out: 2, 2",
        ),
    ],
)
def test_attendance(visitors, expected):
    assert attendance(visitors) == expected


@pytest.mark.parametrize(
    "cipher, expected",
    [
        ("thisisabracadabraHt1eadljjl12ojh.", "Hello."),
        ("X1aYbZc.", "Ya1X"),
        ("abcMdefN2ghI3jk.", "NgIj."),
        ("prefixA3bC6dE9fG12h.", "Ab6Ef1h"),
    ],
)
def test_transcript(cipher, expected):
    assert transcript(cipher) == expected
