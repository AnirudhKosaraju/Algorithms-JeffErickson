
# Variant of SubsetSum that constructs a subset of X that sums to T

# Z = set of positive integers
# X = list of positive integers
# T = target sum

def ContstructSubset(Z, T) -> set:

    i = len(Z)-1
    X = list()
    for z in Z:
        X.append(z)
    return solve(X, T, i)

def solve(X, T, i) -> set:

    if T == 0:
        return set()
    if T < 0 or i < 0:
        return None

    Y = solve(X, T, i-1)
    if Y != None:
        return Y

    Y = solve(X, T-X[i], i-1)
    if Y != None:
        Z = set()
        Z.add(X[i])
        return Y.union(Z)

    return None


