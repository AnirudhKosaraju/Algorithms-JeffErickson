
from NQueens import NQueens
import unittest

class TestNQueens(unittest.TestCase):

    def setUp(self):
        self.solver = NQueens()

    def test_1x1(self):
        self.assertEqual(self.solver.solve(1), 1)

    def test_2x2(self):
        self.assertEqual(self.solver.solve(2), 0)

    def test_3x3(self):
        self.assertEqual(self.solver.solve(3), 0)

    def test_4x4(self):
        self.assertEqual(self.solver.solve(4), 2)

    def test_5x5(self):
        self.assertEqual(self.solver.solve(5), 10)

    def test_6x6(self):
        self.assertEqual(self.solver.solve(6), 4)

    def test_7x7(self):
        self.assertEqual(self.solver.solve(7), 40)

    def test_8x8(self):
        self.assertEqual(self.solver.solve(8), 92)

if __name__ == '__main__':
    unittest.main()