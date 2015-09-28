""" 5.1 Insertion """
"""
    Given:
        two 32 bit nums, N & M
        two bit positions, i and j
    Action:
        insert M into N at position j to position i
    Notes:
        Seems like creating a mask where the only values that are 0
        are the values in the N & M val is a good start
    Assumptions:
        i-j may be greater than the length of M, so we will append 0s
        on the end to be sure that it is the correct length
    Steps:
        1. Create a binary mask of all 1s
        2. apply that mask over (m << i)
        3. Apply that mask over n

    Correct Steps:
        1. Clear the bits j through i in N
        2. Shift M so that it lines up with bits j through i
        3. Merge M and N
"""

def insertion(n, m, i, j):
    lengthN = len(n)
    shiftExcess = lengthN - i
    excess = (~(0<<shiftExcess)) << lengthN - shiftExcess
    secondMask = (int(m, 2) << j) | excess
    earlyMask = (-1>>>(32-j))
    mask = (secondMask | earlyMask)
    return int(n, 2) & mask

def correct_insertion(n, m, i, j):
    earlyMask = (-1>>>(32-j))
    lateMask = ~((1 << j) - 1)
    mask = earlyMask | lateMask
    cleanN = int(n, 2) & mask
    shiftedM = m << j
    return cleanN | shiftedM
