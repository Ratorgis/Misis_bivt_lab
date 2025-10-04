import csv
from pathlib import Path
from collections import Counter

from lib.text import normalize, tokenize
from lab_03.text_stats import stdout_text_info, stdin_info
from lab_04.io_text_csv import read_text, write_csv

def frequencies_from_text(text: str) -> dict[str, int]:
    tokens = tokenize(normalize(text))
    return Counter(tokens) 

def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key = lambda kv: (-kv[1], kv[0]))

if __name__ == '__main__':
    stdin_file = Path(input('input stdin_file path: '))
    text = read_text(stdin_file)
    freq_text = frequencies_from_text(text)
    p = Path(input('Entrie output path: '))
    write_csv(sorted_word_counts(freq_text), p, ('write', 'count'))
    info_text = stdin_info(read_text(stdin_file))
    stdout_text_info(info_text)

