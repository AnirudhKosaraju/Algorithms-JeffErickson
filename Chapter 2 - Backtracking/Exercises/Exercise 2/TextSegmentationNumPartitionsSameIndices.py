
'''
Given two arrays A[1..n] and B[1..n] of characters, compute the 
number of different ways that A and B can be partitioned into
words at the same indices.
'''

def TextSegmentationNumPartitionsSameIndices(A: str, B: str, wordSet: set) -> int:
    solver = Solution(A, B, wordSet)
    solver.solve(0)
    return solver.count


class Solution:

    def __init__(self, A: str, B: str, wordSet: set):
        self.A = A
        self.B = B
        self.n = len(A)
        self.wordSet = wordSet
        self.count = 0

    def solve(self, i):
        if i == self.n:
            self.count += 1
        else:
            for j in range(i, self.n+1):
                if self.A[i:j] in self.wordSet and self.B[i:j] in self.wordSet:
                    self.solve(j)


wordSet = {
    'BOT',
    'HEART',
    'HAND',
    'SAT',
    'URNS',
    'PIN',
    'START',
    'RAPS',
    'AND',
    'RAGS',
    'LAP'
}

A = 'BOTHEARTHANDSATURNSPIN'
B = 'PINSTARTRAPSANDRAGSLAP'

print(TextSegmentationNumPartitionsSameIndices(A, B, wordSet))

