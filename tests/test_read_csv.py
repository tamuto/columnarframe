import unittest

import columnarframe as colf


class TestReadCSV(unittest.TestCase):

    def test_data(self):
        cf = colf.read_csv('./data/test_data.csv')
        self.assertEqual(len(cf), 5)

    def test_header(self):
        pass

    def test_delimiter(self):
        pass

    def test_skiprows(self):
        pass

    def test_skipfooter(self):
        pass

