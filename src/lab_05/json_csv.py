from pathlib import Path
import json, csv

from lib.text import json_reader, csv_reader
from lab_04.io_text_csv import ensure_parent_dir, write_csv

def json_to_csv(json_path: str | Path, csv_path: str | Path) -> None:
    content_read = json_reader(Path(json_path))
    rows, header = [], []
    for one in content_read:
        header.extend(set(one.keys()))
        rows.append(list(one.values()))
    ensure_parent_dir(csv_path)
    write_csv(rows, csv_path, header)

def csv_to_json(csv_path: Path | str, json_path: Path | str) -> None:
    content = csv_reader(csv_path)
    print(content)

p1 = Path('data/samples/people.json')
p = Path('data/samples/people.csv')
csv_to_json(p, p1)
print(json.loads('[{"name": "Alice", "age": 22}, {"name": "Bob", "age": 25}]'))
