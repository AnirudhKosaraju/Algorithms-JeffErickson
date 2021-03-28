
from SubsetSum import SubsetSum
import unittest

class TestSubsetSum(unittest.TestCase):

    def test_01(self):
        X = [8,6,7,5,3,10,9]
        T = 15
        self.assertTrue(SubsetSum(X,len(X)-1, T))

    def test_02(self):
        X = [11,6,5,1,7,13,12]
        T = 15
        self.assertFalse(SubsetSum(X,len(X)-1, T))

    def test_03(self):
        X = [1,2,3,4,5]
        T = 0
        self.assertTrue(SubsetSum(X,len(X), T))

    def test_04(self):
        X = [1,2,3,4,5]
        T = -1
        self.assertFalse(SubsetSum(X,len(X), T))

if __name__ == '__main__':
    unittest.main()