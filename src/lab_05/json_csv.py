from pathlib import Path

from lib.text import json_reader, csv_reader, write_json
from lab_04.io_text_csv import write_csv

def json_to_csv(json_path: str | Path, csv_path: str | Path) -> None:
    content_read = json_reader(Path(json_path))
    if content_read is not []:
        content_read = list(content_read)
    rows, headers = [], set()
    for one in content_read:
        headers = headers.union(headers, one.keys())

    for one in content_read:
        row = list(one.values())
        while len(row) < len(headers):
            row.append("")
        rows.append(row)

    write_csv(rows, csv_path, headers)

def csv_to_json(csv_path: Path | str, json_path: Path | str) -> None:
    content = csv_reader(csv_path)
    result = []
    keys = content[0]
    for one in content[1:]:
        while len(one) < len(keys):
            one.append("")
        row = {
            keys[i]: one[i]
            for i in range(len(keys))
        }
        result.append(row)
    write_json(result, json_path)

