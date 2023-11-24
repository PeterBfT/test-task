from one_hot_encoder import fit_transform
import unittest


class TestOneHotEncoding(unittest.TestCase):
    def test1(self):
        actual = ['red', 'blue', 'red']
        expected = [
            ('red', [0, 1]),
            ('blue', [1, 0]),
            ('red', [0, 1])
        ]
        self.assertEqual(fit_transform(actual), expected)

    def test2(self):
        actual = fit_transform(['1', '2', '3', '2', '1', '3'])
        expected = [
            ('1', [0, 0, 1]),
            ('2', [0, 1, 0]),
            ('3', [1, 0, 0]),
            ('2', [0, 1, 0]),
            ('1', [0, 0, 1]),
            ('3', [1, 0, 0])
        ]
        self.assertEqual(actual, expected)

    def test3(self):
        actual = ['mama', 'mia', 'esh', 'dolmio', 'mama', 'nu', 'esh']
        expected = [
            ('mama', [0, 0, 0, 0, 1]),
            ('mia', [0, 0, 0, 1, 0]),
            ('esh', [0, 0, 1, 0, 0]),
            ('dolmio', [0, 1, 0, 0, 0]),
            ('mama', [0, 0, 0, 0, 1]),
            ('nu', [1, 0, 0, 0, 0]),
            ('esh', [0, 0, 1, 0, 0])
        ]
        self.assertTrue(fit_transform(actual) == expected)

    def test4(self):
        actual = 42
        self.assertRaises(TypeError, fit_transform, actual)


if __name__ == '__main__':
    TestOneHotEncoding()
