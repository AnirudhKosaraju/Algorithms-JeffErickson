

'''
Given an array X[1...n] of positive integers and an integer T, compute the number of subsets
of X whose elements sum to t.
'''

from typing import List

def CountSubsetSum(X, i, T):
    if T == 0:
        return 1
    elif T < 0 or i == -1:
        return 0
    else:
        return CountSubsetSum(X, i-1, T-X[i]) + CountSubsetSum(X, i-1, T)
