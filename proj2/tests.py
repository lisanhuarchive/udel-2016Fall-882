import unittest
from letter_predict import *


class MyTests(unittest.TestCase):
    def test_training(self):
        file = open('SanhuLi.txt')
        text = ''.join(file.readlines())
        file.close()
        stat = dict()
        training(text, stat)
        print(stat[('w', '')])

    def test_training2(self):
        text = 'the big brown fox jumped over the lazy dog.the big brown fox jumped over the lazy dog'
        stat = {}
        training(text, stat)
        print(stat)

    def test_prediction(self):
        file = open('SanhuLi.txt')
        text = ''.join(file.readlines())
        file.close()
        stat = dict()
        training(text, stat)
        print(stat)
        predict(text, stat)


if __name__ == '__main__':
    unittest.main()