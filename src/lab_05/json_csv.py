from pathlib import Path

from src.lib.text import json_reader, csv_reader, write_json
from src.lab_04.io_text_csv import write_csv


def json_to_csv(json_path: str | Path, csv_path: str | Path) -> None:
    content_read = json_reader(Path(json_path))
    headers = []
    for one in content_read:
        for header in one.keys():
            if header not in headers:
                headers.append(header)
    rows = []
    for one in content_read:
        row = [one.get(header, "") for header in headers]
        rows.append(row)
    print(headers, rows)
    write_csv(rows, csv_path, tuple(headers))


def csv_to_json(csv_path: Path | str, json_path: Path | str) -> None:
    content = csv_reader(csv_path)
    if len(content) < 2:
        raise ValueError("CSV file must have a header and at least one row")
    keys = content[0]
    result = []
    for one in content[1:]:
        while len(one) < len(keys):
            one.append("")
        row = {keys[i]: one[i] for i in range(len(keys))}
        result.append(row)
    write_json(result, json_path)


if __name__ == "__main__":
    print(csv_reader("tmp/output.csv"))
