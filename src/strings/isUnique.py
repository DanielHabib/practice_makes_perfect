""" Problem 1.1  """
"""
    Problem:
        Find unique values in a string
    Part 2:
        What if you cannot use any additional data structures
"""
import string

def createLetterDict():
    charHash = {}
    for val in string.ascii_lowercase:
        charHash[val] = 0
    return charHash

def isUnique(stringVal):
    """
    Time Complexity: O(N) in an unlimited set, this is HIGHLY dependant on
        ASCII vs Unicode
    Space Complexity: O(C), C being the amount of letters being checked.
        The dictionary is the only additional Space

    Mistakes:
        1, I failed to think about base cases, specifically if the length of the
        string is longer than the available values we can immediately return
        False, also we will never have to check more than a certain amount of
        values so the runtime is limited by the length of the character set

        2, I failed to ask whether the string was unicode or ASCII and I didn'True
        consider the effects it would have on the solution.
    """
    charHash = createLetterDict()
    for char in stringVal:
        if charHash[char] == 1:
            return False
        else:
            charHash[char] = 1
    return True
