from unittest import TestCase
from main import format_str, count_words


class Test(TestCase):
    def test_format_str_and_count_words(self):
        test_text = ('She married a very nice young architect from Belfast, whom she met on a bus. '
                     'I don\'t know when the decision was made. If I had gone to university '
                     'I would have studied medicine.')
        words_count_dict = count_words(test_text)
        result = format_str(words_count_dict)
        print(result)
        self.assertEqual(result, ('i,3\n'
                                  'she,2\n'
                                  'a,2\n'
                                  'married,1\n'
                                  'very,1\n'
                                  'nice,1\n'
                                  'young,1\n'
                                  'architect,1\n'
                                  'from,1\n'
                                  'belfast,,1'))

