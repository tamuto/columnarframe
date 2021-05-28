import unittest

import columnarframe as colf


class TestFrame2(unittest.TestCase):

    def test_init(self):
        cf = colf.ColumnarFrame({
            'col1': ['aaa', 'bbb', 'ccc'],
            'col2': '5',
        })
        self.assertEqual(cf['col2'].to_list(), ['5', '5', '5'])

    def test_remove(self):
        cf = colf.read_csv('./data/test_data.csv')
        cf2 = cf.remove(lambda x: x['col1'] == 'CCC')
        self.assertEqual(cf2['col1'].to_list(), ['AAA', None, 'DDD'])
