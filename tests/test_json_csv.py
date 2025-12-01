from pathlib import Path
import pytest

from src.lab_04.io_text_csv import write_csv
from src.lab_05.json_csv import json_to_csv, csv_to_json
from src.lib.text import csv_reader, json_reader, write_json


@pytest.mark.parametrize(
    "input_path, output_path, expected",
    [
        (
            "tmp/input.json",
            "tmp/output.csv",
            [["name", "age"], ["Alice", "22"]],
        ),
        ("tmp/empty_json.json", "tmp/output.csv", None),
        ("tmp/not_exist.json", "tmp/output.csv", None),
    ],
)
def test_json_to_csv(input_path, output_path, expected):
    if input_path == "tmp/empty_json.json":
        with pytest.raises(ValueError, match="Your json is empty"):
            json_to_csv(input_path, output_path)
    elif input_path == "tmp/not_exist.json":
        with pytest.raises(FileNotFoundError, match="Cant find your file"):
            json_to_csv(input_path, output_path)
    else:
        write_json([{"name": "Alice", "age": 22}], input_path)
        json_to_csv(input_path, output_path)
        write_content = csv_reader(output_path)
        assert write_content == expected


@pytest.mark.parametrize(
    "input_path, output_path, expected",
    [
        (
            "tmp/input.csv",
            "tmp/output.json",
            [{"name": "Max", "age": "18"}],
        ),
        (
            "tmp/empty_csv.csv",
            "tmp/output.json",
            [{"name": "Max", "age": "18"}],
        ),
        (
            "tmp/not_exist.csv",
            "tmp/output.json",
            [{"name": "Max", "age": "18"}],
        ),
    ],
)
def test_csv_to_json(input_path, output_path, expected):
    if input_path == "tmp/empty_csv.csv":
        with pytest.raises(ValueError, match="Your csv is empty"):
            csv_to_json(input_path, output_path)
    elif input_path == "tmp/not_exist.csv":
        with pytest.raises(FileNotFoundError, match="Cant find your file"):
            csv_to_json(input_path, output_path)
    else:
        write_csv([["Max", "18"]], input_path, tuple(["name", "age"]))
        csv_to_json(input_path, output_path)
        write_content = json_reader(output_path)
        assert write_content == expected
