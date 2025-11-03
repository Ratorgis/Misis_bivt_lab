from pathlib import Path
import csv

from lib.text import normalize

def read_text(path: str | Path, encoding: str = 'utf-8') -> str:
    file = Path(path)
    with file.open('r', encoding = encoding) as f:
        text = f.read()
    return normalize(text)

def write_csv(rows: list[tuple | list], path: str | Path, 
            header: tuple[str, ...] | None = None, *, file_name: str = None) -> None: 

    p = Path(path)
    ensure_parent_dir(p)
    if not rows and header is None:
        raise ValueError('Нельзя создать пустой CVS без заголовка и данных')

    row_length = len(rows[0]) if rows else len(header)
    for r in rows:
        if len(r) != row_length:
            raise ValueError(f"Несовпадение длины строк: ожидалось {row_length}, а получено {len(r)}")

    if header is not None and len(header) != row_length:
        raise ValueError('Длина header не совпадает с длиной строки')

    with p.open('w', encoding = 'utf-8') as f:
        writer = csv.writer(f)
        if header is not None:
            writer.writerow(header)
        writer.writerows(rows)

def ensure_parent_dir(path: str | Path) -> None:
    p = Path(path)
    parent = p.parent
    if not parent.exists():
        parent.mkdir(parents = True, exist_ok = True)


