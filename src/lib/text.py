from pathlib import Path
import re, json


def file_check(path: Path) -> None:
    if path is not Path:
        raise TypeError("Your enter not the path to check file")
    elif str(path) == ".":
        raise ValueError("Your path is empty")
    else:
        l = len(path.name)
        check = Path(str(path)[:-l])
        check = list(check.iterdir())
        if path not in check:
            raise ValueError


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")
    text = text.replace("\t", " ").replace("\r", " ").replace("\n", " ")
    text = " ".join(text.split())
    return text


def tokenize(text: str) -> list[str]:
    reg = r"(\w+(?:-\w+)*)"
    return re.findall(reg, text)


def count_freq(tokens: list[str]) -> dict[str, int]:
    result = {i: tokens.count(i) for i in set(tokens)}
    return result


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:n]


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    file = Path(path)
    with file.open("r", encoding=encoding) as f:
        text = f.read()
    return normalize(text)


def json_reader(path_to_json: Path | str) -> list[dict]:
    path_to_json = Path(path_to_json)
    if not path_to_json.exists():
        raise FileNotFoundError("Cant find your file")
    if path_to_json.suffix.lower() != ".json":
        raise ValueError("It is not .json formate")
    with path_to_json.open(encoding="utf-8") as f:
        content = " ".join(f.readlines())
    if content == "":
        raise ValueError("Your json is empty")
    content = json.loads(content)
    if not (isinstance(content, list)):
        raise ValueError("Expected a list of dictionaries")
    if not all(isinstance(one, dict) for one in content):
        raise ValueError("List conteins non-dict items")
    return content


def csv_reader(path_to_csv: Path | str) -> list[str]:
    path_to_csv = Path(path_to_csv)
    if not path_to_csv.exists():
        raise FileNotFoundError("Cant find your file")
    if path_to_csv.suffix.lower() != ".csv":
        raise ValueError("It is not .csv formate")
    with path_to_csv.open(encoding="utf-8") as f:
        content = "".join(f.readlines())
    if content == "":
        raise ValueError("Your csv is empty")
    result = [list(one.split(",")) for one in content.split("\n")]
    result.remove([''])
    return result


def write_json(content: list[dict], json_path: str | Path) -> None:
    json_path = Path(json_path)
    if not json_path.exists():
        raise FileNotFoundError("Cant find your file")
    if content is None:
        raise ValueError("Input content is empty")
    with json_path.open("w", encoding="utf-8") as f:
        f.write(json.dumps(content))


if __name__ == "__main__":
    ...


