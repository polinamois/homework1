# !/usr/bin/env python
# -*- coding: utf-8 -*-
from utils import get_data, save_data


def sort_data(data: list, key: (int, str) = 0) -> list:
	"""
	Сортировка списка data по ключу key
	"""
	return sorted(data, key=lambda x: x.split()[int(key)])


def format_data(data: list) -> str:
	"""
	Форматирует список data, прим. ['1. Иванов Иван: 5', '2. Петров Пётр: 4\n'] -> ['Иванов Иван,5\n', 'Петров Пётр,4\n']
	"""
	return '\n'.join([line.split('.')[-1].replace(': ', ',').strip() for line in data])


def main():
	data = get_data('data.txt')
	sorted_data = sort_data(data, key=1)
	formatted_data = format_data(sorted_data)
	saved = save_data(f'name,grade\n{formatted_data}', filename='output.csv')
	if saved:
		print('Файл успешно сохранён! ->', saved[1])


if __name__ == '__main__':
	main()
