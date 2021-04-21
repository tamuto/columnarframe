import unittest

import columnarframe as colf


class TestReadCSV(unittest.TestCase):

    def test_data(self):
        cf = colf.read_csv('./data/test_data.csv')
        self.assertEqual(len(cf), 5)

    def test_header(self):
        cf = colf.read_csv('./data/test_data.csv', header=False)
        self.assertEqual(len(cf), 6)

    def test_delimiter(self):
        pass

    def test_skiprows(self):
        cf = colf.read_csv('./data/test_data.csv', header=False, skiprows=3)
        self.assertEqual(cf['0'].to_list(), ['CCC', 'CCC', 'DDD'])

    def test_skipfooter(self):
        cf = colf.read_csv('./data/test_data.csv', skipfooter=2)
        self.assertEqual(cf['col4'].to_list(), ['True', 'False', 'False'])
