# !/usr/bin/env python
# -*- coding: utf-8 -*-
from utils import get_data, save_data


def get_nums(data: list) -> list:
    """
    Формирует список чисел для последующей сортировки
    """
    return [list(map(int, line[2:].replace('-', '.').split('.')[:-1])) for line in data]


def prepare_data(nums: list, data: list) -> str:
    """
    Подготавливает данные для записи в файл. Сортировка по возрастанию и сбор всей строки целиком
    """
    return '\n'.join(item[1].strip() for item in sorted(list(zip(nums, data))))


def main():
    data = get_data('data.txt')
    nums = get_nums(data)
    prepared_data = prepare_data(nums=nums, data=data)
    saved = save_data(prepared_data)
    if saved:
        print('Файл успешно сохранён! ->', saved)


if __name__ == '__main__':
    main()
