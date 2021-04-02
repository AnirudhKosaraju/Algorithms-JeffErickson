
from MaxWeightSubsetSum import MaxWeightSubsetSum
import unittest

class TestSubsetSum(unittest.TestCase):

    def test_01(self):

        X = [1,2,8,9]
        W = [1,3,9,9]
        T = 10
        self.assertEqual(MaxWeightSubsetSum(X,W,T), 12)

    def test_02(self):

        X = [1,2,8,9]
        W = [3,2,8,11]
        T = 10
        self.assertEqual(MaxWeightSubsetSum(X,W,T), 14)

    def test_03(self):
        X = [1,2,8,9]
        W = [1,1,1,1]
        T = 20
        self.assertEqual(MaxWeightSubsetSum(X,W,T), 4)

    def test_04(self):
        X = [1,2,8,9]
        W = [1,1,1,1]
        T = 5
        self.assertEqual(MaxWeightSubsetSum(X,W,T), -1)

if __name__ == '__main__':
    unittest.main()