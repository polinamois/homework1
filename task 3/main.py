# !/usr/bin/env python
# -*- coding: utf-8 -*-
from utils import get_data, save_data


def str_to_poem(string: str, symbol_nums: int) -> str:
    """
    Ставит перенос строки по необходимому количеству символов в строке symbol_nums
    """
    tmp = ''
    res = []
    for word in string.split():
        if len(tmp) <= symbol_nums:
            tmp += f'{word} '
        else:
            res.append(tmp)
            tmp = f'{word} '
    res.append(tmp)
    return '\n'.join(res)


def main():
    data = get_data('input.txt')[0]
    res = str_to_poem(data, symbol_nums=20)
    saved = save_data(res)
    if saved:
        print('Файл успешно сохранён! ->', saved)


if __name__ == '__main__':
    main()
