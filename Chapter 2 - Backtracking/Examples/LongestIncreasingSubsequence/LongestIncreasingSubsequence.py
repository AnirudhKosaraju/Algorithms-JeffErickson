
'''
Suppose we are given a sequence of integers and we need to find the
longest subsequence whose elements are in increasing order.
'''

from typing import List

def LongestIncreasingSubsequence(X: List[int]) -> int:
    return solve(X, 0, 0, len(X))

def solve(X, prev, i, n) -> int:
    if i == n:
        return 0
    elif X[i] <= prev:
        return solve(X, prev, i+1, n)
    else:
        skip = solve(X, prev, i+1, n)
        take = solve(X, X[i], i+1, n) + 1
        return max(skip, take)
