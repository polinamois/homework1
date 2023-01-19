import unittest
from main import sort_data, format_data


class MyTestCase(unittest.TestCase):
    def test_format_text(self):
        test_text = (
            ['1. Иванов Иван: 7\n',
             '2. Петров Петр: 4\n',
             '3. Алексеев Алексей: 2\n',
             '4. Шишкин Юрий: 3'
             ]
        )
        sorted_data = sort_data(test_text, key=1)
        formatted_data = format_data(sorted_data)
        self.assertEqual(f'name,grade\n{formatted_data}', ("name,grade\n"
                                                           "Алексеев Алексей,2\n"
                                                           "Иванов Иван,7\n"
                                                           "Петров Петр,4\n"
                                                           "Шишкин Юрий,3"
                                                           )
                         )

