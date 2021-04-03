
'''
Given two arrays A[1...n] and B[1...n] of characters, decide
whether A and B can be partitioned into words at the same indices.
For example, the following strings can be partitioned into words
at the same indices
    BOT HEART HAND SAT URNS PIN
    PIN START RAPS AND RAGS LAP
'''

def TextSegmentationSameIndices(A: str, B: str, wordSet: set) -> bool:
    solver = Solution(A, B, wordSet)
    return solver.solve(0)



class Solution:

    def __init__(self, A: str, B: str, wordSet: set):
        self.A = A
        self.B = B
        self.n = len(A)
        self.wordSet = wordSet

    def solve(self, i) -> bool:
        if i == self.n:
            return True
        else:
            for j in range(i, self.n+1):
                if self.A[i:j] in self.wordSet and self.B[i:j] in self.wordSet:
                    if self.solve(j):
                        return True
        return False


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

print(TextSegmentationSameIndices(A, B, wordSet))

