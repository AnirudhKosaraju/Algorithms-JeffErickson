
from typing import List

'''
Given a set X of positive integers and target integer T, is there
a subset of elements in X that add up to T?
'''

def SubsetSum(X, i, T):
    if T == 0:
        return True
    elif T < 0 or i == -1:
        return False
    else:
        return SubsetSum(X, i-1, T-X[i]) or SubsetSum(X, i-1, T)