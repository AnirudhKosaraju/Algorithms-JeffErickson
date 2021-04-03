
'''
Given an array of A[1...n] characters, compute the number of partitions of A
into words. For example, given the string ARTISTOIL, you algorithm should return
2 for the partitions ARTIST|OIL and ART|IS|TOIL
'''

def TextSegmentataionNumPartitions(s: str, wordSet: set) -> int:
    solver = Solution(s, wordSet)
    solver.solve(0)
    return solver.count

class Solution:

    def __init__(self, s: str, wordSet: set):
        self.s = s
        self.n = len(s)
        self.wordSet = wordSet
        self.count = 0

    def solve(self, i):
        if i == self.n:
            self.count += 1
        else:
            for j in range(i, self.n+1):
                if s[i:j] in self.wordSet:
                    self.solve(j)
  


s = 'ARTISTOIL'
wordSet = {'ART','IS','TOIL','ARTIST','OIL'}
print(TextSegmentataionNumPartitions(s, wordSet))
