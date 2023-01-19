from unittest import TestCase
from main import find_needed_words


class Test(TestCase):
    def test_find_needed_words(self):
        result = find_needed_words(["eat", "tea", "tan", "ate", "nat", "bat"])
        self.assertEqual(result, [['ate', 'eat', 'tea'], ['bat'], ['nat', 'tan']])

