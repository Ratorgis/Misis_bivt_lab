from pathlib import Path
import pytest

from src.lab_05.json_csv import json_to_csv, csv_to_json
from src.lib.text import csv_reader, json_reader


@pytest.mark.parametrize(
    "input_path, output_path, expected",
    [
        (
            "src/data/samples/people.json",
            "tmp/output.csv",
            [["name", "age"], [" Alice", "22"], [""]],
        ),
        ("src/data/samples/empty_json.json", "tmp/output.csv", "[]"),
        ("src/data/samples/not_exist.json", "tmp/output.csv", "[]"),
    ],
)
def test_json_to_csv(input_path, output_path, expected):
    if input_path == "src/data/samples/empty_json.json":
        with pytest.raises(ValueError, match="Your json is empty"):
            json_to_csv(input_path, output_path)
    elif input_path == "src/data/samples/not_exist.json":
        with pytest.raises(FileNotFoundError, match="Cant find your file"):
            json_to_csv(input_path, output_path)
    else:
        json_to_csv(input_path, output_path)
        write_content = csv_reader(output_path)
        assert write_content == expected


@pytest.mark.parametrize(
    "input_path, output_path, expected",
    [
        (
            "src/data/samples/people.csv",
            "tmp/output.json",
            [{"name": " Max", " age": " 18"}],
        ),
        (
            "src/data/samples/empty_csv.csv",
            "tmp/output.json",
            "[{'name': ' Max', ' age': ' 18'}]",
        ),
        (
            "src/data/samples/not_exist.csv",
            "tmp/output.json",
            "[{'name': ' Max', ' age': ' 18'}]",
        ),
    ],
)
def test_csv_to_json(input_path, output_path, expected):
    if input_path == "src/data/samples/empty_csv.csv":
        with pytest.raises(ValueError, match="Your csv is empty"):
            csv_to_json(input_path, output_path)
    elif input_path == "src/data/samples/not_exist.csv":
        with pytest.raises(FileNotFoundError, match="Cant find your file"):
            csv_to_json(input_path, output_path)
    else:
        csv_to_json(input_path, output_path)
        write_content = json_reader(output_path)
        assert write_content == expected
