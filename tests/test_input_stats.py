import pytest

from src.lab_03.text_stats import stdin_info


@pytest.mark.parametrize(
    "text, expected",
    [
        ("apple banana apple", [3, 2, [("apple", 2), ("banana", 1)]]),
        ("", [0, 0, []]),
        ("one two three", [3, 3, [("one", 1), ("three", 1), ("two", 1)]]),
        ("Word word", [2, 2, [("Word", 1), ("word", 1)]]),
    ],
)
def test_stdin_info(text, expected):
    assert stdin_info(text) == expected
