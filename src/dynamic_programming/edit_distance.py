import math
from functools import lru_cache
from collections import defaultdict
"""
Find the Edit distance between two string a & b

Options:
    Delete
    Add
    Replace
Cost Function for all options are identical(1)
"""

rDict = lambda:defaultdict(defaultdict)
memo = defaultdict(rDict)
# @lru_cache(maxsize=39)

def editDistance(a, b):
    if a in memo and b in memo[a]:
        return memo[a][b]

    if len(a) == 0:
        return len(b)
    if len(b) == 0:
        return len(a)
    
    minDistance = math.inf
    if a[-1] == b[-1]:
        minDistance = min(minDistance, editDistance(a[:-1], b[:-1])) # Match
    minDistance = min(minDistance, editDistance(a[:-1], b) + 1) # Insertion
    minDistance = min(minDistance, editDistance(a, b[:-1]) + 1) # Deletion
    minDistance = min(minDistance, editDistance(a[:-1], b[:-1]) + 1) # Replace
    
    memo[a][b] = minDistance
    return minDistance


if __name__ == '__main__':
    print(editDistance('hello', 'hell'))
    print(editDistance('hello', 'jello'))
    print(editDistance('hell', 'hello'))



