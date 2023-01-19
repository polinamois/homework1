from unittest import TestCase
from main import get_nums, prepare_data


class Test(TestCase):
    def test_get_nums_and_prepare_data(self):
        test_text = ('KP2.2-20.2 - Vedomost\n'
                     'KP2.2-03 - Schema rapolozheniya\n'
                     'KP2.2-12.10 - Schema rapolozheniya\n'
                     'KP2.2-01.1 - Schema rapolozheniya\n'
                     'KP2.2-2.2 - Schema')
        text = test_text.split('\n')
        nums = get_nums(text)
        res = prepare_data(nums=nums, data=text)
        self.assertEqual(res, ('KP2.2-01.1 - Schema rapolozheniya\n'
                               'KP2.2-2.2 - Schema\n'
                               'KP2.2-03 - Schema rapolozheniya\n'
                               'KP2.2-12.10 - Schema rapolozheniya\n'
                               'KP2.2-20.2 - Vedomost'))

