from pathlib import Path
import json, csv

from lib.text import json_reader, csv_reader, write_json
from lab_04.io_text_csv import write_csv
from lib.text import read_text

def json_to_csv(json_path: str | Path, csv_path: str | Path) -> None:
    content_read = list(json_reader(Path(json_path)))
    rows, headers = [], set()
    for one in content_read:
        headers.update(one.keys())

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


if __name__ == "__main__":
    path_in = 'data/samples/people.csv'
    path_out = 'data/out/people_from_csv.json'
    print(csv_reader(path_in))
    # [{"name": Max, "age": 18, "city": Novosibirsk}]


