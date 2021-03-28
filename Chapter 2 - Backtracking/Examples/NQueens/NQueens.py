
from typing import List

class NQueens():

    def __init__(self):
        self.numSolutions = 0


    def solve(self, n: int) -> int:
        self.Q = [None] * n
        self.n = n
        self.PlaceQueens(0)
        return self.numSolutions


    def PlaceQueens(self, r):
        
        if r == self.n:
            self.numSolutions += 1
        else:
            for j in range(self.n):
                legal = True
                for i in range(r):
                    if self.Q[i] == j or self.Q[i] == j + r - i or self.Q[i] == j - r + i:
                        legal = False
                if legal:
                    self.Q[r] = j
                    self.PlaceQueens(r+1)