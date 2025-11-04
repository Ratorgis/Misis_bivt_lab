from lib.text import tokenize, count_freq, top_n

def stdin_info(text: str) -> list[int, int, dict[str: int]]:
    tokens = tokenize(text)
    words = len(tokens)
    uniq_words = len(set(tokens))
    top_words = top_n(count_freq(tokens))
    return [words, uniq_words, top_words]

def stdout_text_info(info: list[int, int, dict[str, int]], prettie: bool) -> str:
    words, uniq, top = info
    if prettie:
        max_len_word = max(len(word[0]) for word in top)
        max_len_word = 5 if max_len_word < 5 else max_len_word
        print('слово' + ' ' * (2 * max_len_word - 5) + '| частота')
        print('-' * (2 * max_len_word + 9))
        for word, count in top:
            print(word + ' ' * (2 * max_len_word - len(word)) + '| ' + str(count))
    else:
        print(f'Всего слов: {words}')
        print(f'Уникальных слов: {uniq}')
        print('Топ-5')
        for word, count in top:
            print(f'{word}: {count}')

if __name__ == '__main__':
    info = stdin_info(input())
    ask = True if input('Do you wanna see pretie output ? (Yes or No): ') == 'Yes' else False
    stdout_text_info(info, ask)
