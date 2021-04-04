
import time

def AdditionChain(n: int) -> list:
    solver = Solution(n)
    solver.solve(0)
    return solver.best

class Solution:

    def __init__(self, n):
        self.A = [None] * n
        self.A[0] = 1
        self.n = n
        self.best = self.A

    def solve(self, x):
        if self.A[x] == self.n:
            if x < len(self.best):
                self.best = self.A.copy()
            
        else:
            for i in range(x+1):
                if 2 * self.A[i] > self.A[x]:
                    for j in range(x+1):
                        k = self.A[i] + self.A[j]
                        if k > self.A[x] and k <= self.n:
                            self.A[x+1] = k
                            self.solve(x+1)
                            self.A[x+1] = None



start = time.time()
print(AdditionChain(14))
end = time.time()
print(end - start)

