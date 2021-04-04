
from typing import List

def FastLIS(A) -> int:
    solver = Solution(A)
    solver.solve()
    return solver.res

class Solution:

    def __init__(self, A):

        self.n = len(A)
        self.A = [-1] + A
        self.res = 0
        self.dp = list()
        for _ in range(self.n+1):
            self.dp.append([0] * (self.n+2))

    def solve(self):

        for i in range(self.n+1):
            self.dp[i][self.n+1] = 0

        for j in range(self.n, 0, -1):
            for i in range(0, j):
                keep = self.dp[j][j+1] + 1
                skip = self.dp[i][j+1]
                
                if self.A[i] >= self.A[j]:
                    self.dp[i][j] = skip
                else:
                    self.dp[i][j] = max(skip, keep)

        self.res = self.dp[0][1]

