import unittest

import columnarframe as colf


class TestColumn(unittest.TestCase):

    def setUp(self):
        self.cf = colf.read_csv('./data/test_data.csv')

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
        self.cf['col1'] = self.cf['col1'].apply(
            lambda x: x if x != 'AAA' else None
        )
        self.assertEqual(
            self.cf['col1'].to_list(),
            [None, None, 'CCC', 'CCC', 'DDD']
        )
