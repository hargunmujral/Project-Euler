import math

def latticePaths(n):
    return math.comb(2 * n, n)

print(latticePaths(20))