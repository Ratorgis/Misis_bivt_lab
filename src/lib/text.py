import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    text = text.replace('\t', ' ').replace('\r', ' ').replace('\n', ' ')    
    text = ' '.join(text.split())
    return text


def tokenize(text: str) -> list[str]:
    reg = r'(\w+(?:-\w+)*)'
    return re.findall(reg, text)

def count_freq(tokens: list[str]) -> dict[str, int]:
    d = {
        i: tokens.count(i)
        for i in set(tokens)
    }
    return d

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    dic = sorted(list(freq.items()))
    return dic[:n]

