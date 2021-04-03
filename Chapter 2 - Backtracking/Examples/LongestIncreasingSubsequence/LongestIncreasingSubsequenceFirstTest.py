
from LongestIncreasingSubsequenceFirst import LongestIncreasingSubsequenceFirst
import unittest

class TestCountSubsetSum(unittest.TestCase):

    def test_01(self):
        X = [1,2,3,4,5,6,7,8,9,10]
        self.assertEqual(LongestIncreasingSubsequenceFirst(X), 10)

    def test_02(self):
        X = [1,2,1,3,1,4,1,5]
        self.assertEqual(LongestIncreasingSubsequenceFirst(X), 5)

    def test_03(self):
        X = [5,4,3,2,1]
        self.assertEqual(LongestIncreasingSubsequenceFirst(X), 1)

    def test_04(self):
        X = [1,3,2,5,4,6,5,7,6,8,7,9,8,10,9]
        self.assertEqual(LongestIncreasingSubsequenceFirst(X), 8)

if __name__ == '__main__':
    unittest.main()