import unittest

import columnarframe as colf


# FIXME: setup で Excel を作成するべき？
class TestReadExcel(unittest.TestCase):
    pass
    # def test_data_xlsx(self):
    #     print('test')
    #     cf = colf.read_excel('./data/test_data.xlsx')
    #     print(cf)
    #     self.assertEqual(len(cf), 5)

    # def test_header_xlsx(self):
    #     # TODO
    #     pass

    # def test_skiprows_xlsx(self):
    #     cf = colf.read_excel('./data/test_data.xlsx', skiprows=2)
    #     self.assertEqual(cf['0'].to_list(), ['CCC', 'CCC', 'DDD'])

    # def test_skipfooter_xlsx(self):
    #     cf = colf.read_excel('./data/test_data.xlsx', skipfooter=2)
    #     self.assertEqual(cf['col4'].to_list(), ['True', 'False', 'False'])

    # def test_data_xls(self):
    #     cf = colf.read_excel('./data/test_data.xls', file_type='xls')
    #     self.assertEqual(len(cf), 5)

    # def test_header_xls(self):
    #     # TODO
    #     pass

    # def test_skiprows_xls(self):
    #     cf = colf.read_excel('./data/test_data.xls', file_type='xls', skiprows=2)
    #     self.assertEqual(cf['0'].to_list(), ['CCC', 'CCC', 'DDD'])

    # def test_skipfooter_xls(self):
    #     cf = colf.read_excel('./data/test_data.xls', file_type='xls', skipfooter=2)
    #     self.assertEqual(cf['col4'].to_list(), ['True', 'False', 'False'])
