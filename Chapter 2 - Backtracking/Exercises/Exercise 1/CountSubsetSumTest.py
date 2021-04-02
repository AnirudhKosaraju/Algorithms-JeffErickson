
from CountSubsetSum import CountSubsetSum
import unittest

class TestCountSubsetSum(unittest.TestCase):

    def test_01(self):
        X = [8,6,7,5,3,10,9]
        T = 15
        self.assertEqual(CountSubsetSum(X, len(X)-1, T), 4)

if __name__ == '__main__':
    unittest.main()