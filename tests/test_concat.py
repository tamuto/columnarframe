import unittest

import columnarframe as colf


class TestConcat(unittest.TestCase):

    def setUp(self):
        self.cf1 = colf.ColumnarFrame({
            'col1': ['AAA', None, 'CCC', 'CCC', 'DDD'],
            'col2': ['1', '5', '8', '3', None],
            'col4': ['True', 'False', 'False', None, 'True'],
        })
        self.cf2 = colf.ColumnarFrame({
            'col1': ['QQQ'],
            'col2': [None],
            'col4': ['Test']
        })

    def test_concat(self):
        cf = colf.concat(self.cf1, self.cf2)
        self.assertEqual(
            cf['col1'].to_list(),
            ['AAA', None, 'CCC', 'CCC', 'DDD', 'QQQ']
        )

    def test_column_diff1(self):
        self.cf1['abc'] = 'A'

        with self.assertRaises(RuntimeError):
            colf.concat(self.cf1, self.cf2)

    def test_column_diff2(self):
        self.cf2['abc'] = 'A'

        with self.assertRaises(RuntimeError):
            colf.concat(self.cf1, self.cf2)
