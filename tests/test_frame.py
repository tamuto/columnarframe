import unittest

import columnarframe as colf


class TestFrame(unittest.TestCase):

    def setUp(self):
        self.cf = colf.read_csv('./data/test_data.csv')

    def test_getitem(self):
        print(self.cf)
        
        print(self.cf[['col1', 'col2']])
