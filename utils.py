def save_data(data: any, filename: str = None) -> (bool, str):
	"""
	Запись данных data в файл ./output.txt, если filename не определен
	"""
	if filename is None:
		filename = './output.txt'
	with open(file=filename, mode='w') as f:
		f.write(str(data))
	return filename


def get_data(filename: str) -> list:
	"""
	Чтение данных по строкам из файла filename
	"""
	with open(file=filename, mode='r', encoding='utf-8') as f:
		data = f.readlines()
	return data
