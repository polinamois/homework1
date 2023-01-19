# !/usr/bin/env python
# -*- coding: utf-8 -*-
from utils import get_data, save_data
from collections import Counter


def count_words(string: str) -> dict:
    """
    Возвращает словарь с парой значений {слово:сколько раз встретилось}
    """
    return dict(Counter(line.lower() for line in string.split()).most_common(10))


def format_str(dict_fmt: dict) -> str:
    return '\n'.join([f'{word},{count}' for word, count in dict_fmt.items()])


def main():
    str_data = ''.join(get_data('input.txt'))
    data = count_words(str_data)
    saved = save_data(format_str(data))
    if saved:
        print('Файл успешно сохранён!Топ 10 встречаемых слов ->', saved)


if __name__ == '__main__':
    main()
