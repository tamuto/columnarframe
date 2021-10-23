import unittest
import collections

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

    def test_len(self):
        cf = colf.ColumnarFrame({})
        self.assertEqual(len(cf), 0)

    def test_counter(self):
        cf = colf.read_csv('./data/titanic.csv')
        cnt = cf.counter(['Pclass', 'Sex'])
        self.assertEqual(
            cnt,
            collections.Counter({
                ('3', 'male'): 146,
                ('3', 'female'): 72,
                ('2', 'male'): 63,
                ('1', 'male'): 57,
                ('1', 'female'): 50,
                ('2', 'female'): 30
            })
        )

    def test_unique(self):
        cf = colf.read_csv('./data/titanic.csv')
        keys = cf.unique(['Pclass', 'Sex'])
        self.assertEqual(
            keys,
            {
                ('2', 'male'),
                ('2', 'female'),
                ('1', 'male'),
                ('1', 'female'),
                ('3', 'male'),
                ('3', 'female')
            }
        )

    def test_tree(self):
        cf = colf.read_csv('./data/titanic.csv')
        keys = cf.unique(['Pclass', 'Sex'])
        tcf = cf.tree(keys, ['Pclass', 'Sex'])
        self.assertEqual(len(tcf[('3', 'male')]), 146)

    def test_summary(self):
        def test(val):
            return val[0]['Name']

        cf = colf.read_csv('./data/titanic.csv')
        keys = cf.unique(['Pclass', 'Sex'])
        smry = cf.summary(keys, ['Pclass', 'Sex'], test=test)
        self.assertEqual(len(smry), 6)
