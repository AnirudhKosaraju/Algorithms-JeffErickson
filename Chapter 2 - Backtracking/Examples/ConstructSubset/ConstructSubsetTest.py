
from ConstructSubset import ContstructSubset
import unittest

class TestSubsetSum(unittest.TestCase):

    def test_01(self):
        Z = {1, 25, 50, 100}
        T = 1
        expected = {1}
        self.assertEqual(ContstructSubset(Z, T), expected)

    def test_02(self):
        Z = {1, 25, 50, 100}
        T = 26
        expected = {1, 25}
        self.assertEqual(ContstructSubset(Z, T), expected)

    def test_03(self):
        Z = {1, 25, 50, 100}
        T = 76
        expected = {1, 25, 50}
        self.assertEqual(ContstructSubset(Z, T), expected)

    def test_04(self):
        Z = {1, 25, 50, 100}
        T = 2
        expected = None
        self.assertEqual(ContstructSubset(Z, T), expected)
        


if __name__ == '__main__':
    unittest.main()