

'''
Suppose we are given a sequence of integers and we need to find the
longest subsequence whose elements are in increasing order.
'''

from typing import List

def LongestIncreasingSubsequenceFirst(X: List[int]) -> int:
    solver = Solution(X)
    return solver.LIS(0)

class Solution:

    def __init__(self, X):
        self.X = X
        self.n = len(X)

    def LIS(self, i):
        best = 0
        for j in range(i+1,self.n):
            if self.X[j] > self.X[i]:
                best = max(best, self.LIS(j))
        return 1 + best