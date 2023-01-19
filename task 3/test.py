from unittest import TestCase
from main import str_to_poem


class Test(TestCase):
    def test_str_to_poem_20_chars(self):
        test_text = ('I have a theory about British cooking, and I was interested to read that several famous cookery '
                     'writers agree with me. My theory is this. Our basic ingredients, when fresh, '
                     'are so full of flavor that we haven\'t had to invent sauces and complex recipes '
                     'to disguise their natural taste')
        result = str_to_poem(test_text, 20)
        print(result)
        self.assertEqual(result, ('I have a theory about \n'
                                  'British cooking, and \n'
                                  'I was interested to read \n'
                                  'that several famous cookery \n'
                                  'writers agree with me. \n'
                                  'My theory is this. Our \n'
                                  'basic ingredients, when \n'
                                  'fresh, are so full of \n'
                                  "flavor that we haven't \n"
                                  'had to invent sauces \n'
                                  'and complex recipes to \n'
                                  'disguise their natural \n'
                                  'taste '))

    def test_str_to_poem_40_chars(self):
        test_text = ('I have a theory about British cooking, and I was interested to read that several famous cookery '
                     'writers agree with me. My theory is this. Our basic ingredients, when fresh, '
                     'are so full of flavor that we haven\'t had to invent sauces and complex recipes '
                     'to disguise their natural taste')
        result = str_to_poem(test_text, 40)
        self.assertEqual(result, ('I have a theory about British cooking, and \n'
                                  'I was interested to read that several famous \n'
                                  'cookery writers agree with me. My theory \n' 
                                  'is this. Our basic ingredients, when fresh, \n'
                                  "are so full of flavor that we haven't had \n"
                                  'to invent sauces and complex recipes to disguise \n'
                                  'their natural taste '))
