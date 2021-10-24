import unittest

import columnarframe as colf


class TestReadExcel(unittest.TestCase):
    def test_data_xlsx(self):
        cf = colf.read_excel('./data/test_data.xlsx')
        self.assertEqual(len(cf), 5)
        self.assertEqual(
            cf['col1'].to_list(),
            ['AAA', None, 'CCC', 'CCC', 'DDD'])

    def test_header_xlsx(self):
        cf = colf.read_excel('./data/test_data.xlsx', header=False)
        self.assertEqual(len(cf), 6)
        self.assertEqual(
            cf['0'].to_list(),
            ['col1', 'AAA', None, 'CCC', 'CCC', 'DDD'])

    def test_skiprows_xlsx(self):
        cf = colf.read_excel('./data/test_data.xlsx', skiprows=2)
        self.assertEqual(cf['0'].to_list(), ['CCC', 'CCC', 'DDD'])

    def test_skipfooter_xlsx(self):
        cf = colf.read_excel('./data/test_data.xlsx', skipfooter=2)
        self.assertEqual(cf['col4'].to_list(), ['True', 'False', 'False'])

    def test_other_xslx(self):
        cf = colf.read_excel('./data/test_data2.xlsx', datefmt='%Y-%m-%d')
        self.assertEqual(
            cf['col1'].to_list(),
            ['0.5', None, '0.3333', '4']
        )
        self.assertEqual(
            cf['col2'].to_list(),
            ['2021-05-26', '2021-05-26', None, '2021-05-26']
        )

    def test_data_xls(self):
        cf = colf.read_excel('./data/test_data.xls', file_type='xls')
        self.assertEqual(len(cf), 5)

    def test_header_xls(self):
        cf = colf.read_excel('./data/test_data.xls', file_type='xls', header=False)
        self.assertEqual(len(cf), 6)
        self.assertEqual(
            cf['0'].to_list(),
            ['col1', 'AAA', None, 'CCC', 'CCC', 'DDD'])

    def test_skiprows_xls(self):
        cf = colf.read_excel('./data/test_data.xls', file_type='xls', skiprows=2)
        self.assertEqual(cf['0'].to_list(), ['CCC', 'CCC', 'DDD'])

    def test_skipfooter_xls(self):
        cf = colf.read_excel('./data/test_data.xls', file_type='xls', skipfooter=2)
        self.assertEqual(cf['col4'].to_list(), ['True', 'False', 'False'])
