import unittest

import columnarframe as colf


class TestColumn(unittest.TestCase):

    def setUp(self):
        self.cf = colf.ColumnarFrame({
            'col1': ['AAA', None, 'CCC', 'CCC', 'DDD'],
            'col2': ['1', '5', '8', '3', None],
            'col4': ['True', 'False', 'False', None, 'True'],
        })

    def test_to_list(self):
        self.assertEqual(
            self.cf['col1'].to_list(),
            ['AAA', None, 'CCC', 'CCC', 'DDD'])

    def test_unique(self):
        self.assertEqual(
            self.cf['col1'].apply(
                lambda x: x if x != 'AAA' else None).unique().to_list(),
            [None, 'CCC', 'DDD'])

    def test_apply(self):
        self.assertEqual(
            self.cf['col1'].apply(
                lambda x: x if x != 'AAA' else None).to_list(),
            [None, None, 'CCC', 'CCC', 'DDD'])

    def test_apply2(self):
        self.cf['test1'] = self.cf['col1'].apply(
            lambda x: x if x != 'AAA' else None
        )
        self.assertEqual(
            self.cf['col1'].to_list(),
            ['AAA', None, 'CCC', 'CCC', 'DDD']
        )
        self.assertEqual(
            self.cf['test1'].to_list(),
            [None, None, 'CCC', 'CCC', 'DDD']
        )

    def test_apply3(self):
        def conv(value, target):
            return value if value == target else None

        self.cf['col1'] = self.cf['col1'].apply(
            (conv, 'CCC'),
            lambda x: x if x is not None else ''
        )
        self.assertEqual(
            self.cf['col1'].to_list(),
            ['', '', 'CCC', 'CCC', '']
        )

    def test_fillin(self):
        self.cf['col1'] = self.cf['col1'].fillin(self.cf['col2'], lambda x, val: x if x is not None else val)
        self.assertEqual(
            self.cf['col1'].to_list(),
            ['AAA', '5', 'CCC', 'CCC', 'DDD'])
