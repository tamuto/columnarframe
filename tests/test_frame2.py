import unittest

import columnarframe as colf


class TestFrame2(unittest.TestCase):

    def test_init(self):
        cf = colf.ColumnarFrame({
            'col1': ['aaa', 'bbb', 'ccc'],
            'col2': '5',
        })
        self.assertEqual(cf['col2'].to_list(), ['5', '5', '5'])
