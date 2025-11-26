from src.lib.text import tokenize, count_freq, top_n


def stdin_info(text: str) -> list[int, int, tuple[str]]:
    tokens = tokenize(text)
    words = len(tokens)
    uniq_words = len(set(tokens))
    top_words = top_n(count_freq(tokens))
    return [words, uniq_words, top_words]


def stdout_text_info(
    info: list[int, int, tuple[str]], prettie: bool = False
) -> list[str]:
    words, uniq, top = info
    result = []
    if prettie:
        max_len_word = max(len(word[0]) for word in top)
        max_len_word = 5 if max_len_word < 5 else max_len_word
        result.append(f'слово {" " * (2 * max_len_word - 5)} | частота')
        result.append("-" * (2 * max_len_word + 9))
        for word, count in top:
            result.append(
                word + " " * (2 * max_len_word - len(word)) + "| " + str(count)
            )
    else:
        result.append(f"Всего слов: {words}")
        result.append(f"Уникальных слов: {uniq}")
        result.append("Топ-5")
        for word, count in top:
            result.append(f"{word}: {count}")
    return result
