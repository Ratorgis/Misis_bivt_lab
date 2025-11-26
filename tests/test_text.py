import pytest

from src.lib.text import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
    ],
)
def test_normalize_basic(source, expected):
    assert normalize(source) == expected


@pytest.mark.parametrize(
    "source, expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("hello,world!!!", ["hello", "world"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),
    ],
)
def test_tokenize_basic(source, expected):
    assert tokenize(source) == expected


@pytest.mark.parametrize(
    "source, expected",
    [
        (["a", "b", "a", "c", "b", "a"], {"a": 3, "b": 2, "c": 1}),
        (["bb", "aa", "bb", "aa", "cc"], {"aa": 2, "bb": 2, "cc": 1}),
        ([], {}),
        (["one"], {"one": 1}),
        (["x", "x", "x", "x"], {"x": 4}),
    ],
)
def test_count_freq(source, expected):
    assert count_freq(source) == expected


@pytest.mark.parametrize(
    "source, option, expected",
    [
        ({"a": 3, "b": 2, "c": 1}, 1, [("a", 3)]),
        ({"aa": 2, "bb": 2, "cc": 1}, 2, [("aa", 2), ("bb", 2)]),
        ({"x": 5, "y": 1}, 5, [("x", 5), ("y", 1)]),
        ({}, 3, []),
        ({"m": 2, "n": 2, "k": 2}, 2, [("k", 2), ("m", 2)]),
    ],
)
def test_top_n(source, option, expected):
    assert top_n(source, n=option) == expected
