import unittest

import columnarframe as colf


class TestFrame3(unittest.TestCase):

    def test_sort(self):
        cf = colf.read_csv('./data/test_data.csv')
        sorted_cf = cf.sort(lambda x: str(x['col3']) + str(x['col1']))

        self.assertEqual(sorted_cf['col3'].to_list(), ['2020-05-03', '2020-05-25', '2020-07-03', '2021-05-03', None])
