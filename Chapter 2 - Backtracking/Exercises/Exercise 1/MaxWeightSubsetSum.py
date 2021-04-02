

'''
Given two arrays X[1...n] and W[1...n] of positive integers and an integer T,
where each W[i] denotes the weight of the corresponding element X[i], compute
the maximum weight subset of X whose elements sum to T. If no subset of X sums
to T, your algorithm should return -1
'''

from typing import List





def MaxWeightSubsetSum(X, W, T):
    return solve(X, W, T, len(X)-1, 0)



def solve(X, W, T, index, weight):
    if T == 0:
        return weight
    elif T < 0 or index == -1:
        return -1
    else:
        a = solve(X, W, T, index-1, weight)
        b = solve(X, W, T-X[index], index-1, weight+W[index])
        return max(a,b)