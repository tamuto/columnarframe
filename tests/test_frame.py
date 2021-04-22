import unittest
from io import StringIO

import columnarframe as colf


class TestFrame(unittest.TestCase):

    def setUp(self):
        self.cf = colf.read_csv('./data/test_data.csv')

    def test_getitem(self):
        cf2 = self.cf[['col1', 'col2']]
        self.assertEqual(cf2.columns, ['col1', 'col2'])

    def test_setitem(self):
        self.cf['abc'] = 5
        self.assertEqual(self.cf['abc'].to_list(), [5, 5, 5, 5, 5])

    def test_rename(self):
        cf2 = self.cf.rename(columns={'col2': 'renamed'})
        self.assertEqual(cf2['renamed'].to_list(), self.cf['col2'].to_list())

    def test_to_csv(self):
        f = StringIO()
        self.cf.to_csv(f, na_rep='\\N', index=False, header=True)
        # print(f.getvalue())

    def test_to_csv_file(self):
        self.cf.to_csv('./data/output.csv')

    def test_to_csv_file_tsv(self):
        self.cf.to_csv('./data/output.tsv', sep='\t', header=True)