""" 1.5 """

"""
    Time: 20:06
    Problem: Given 2 strs, find if they are 1 or 0 edits away from each other

    Notes: Assuming whitespace matters, Unicode/ASCII doesn't matter

    valid edits: insert, remove, replace

    BCR: O(N)
"""

def oneAway(str1, str2):
    """
        Breakdown: This was a logic heavy problem, less effort in making it
            more efficient and more focus on separating the logic between
            the two different mutations, when trying to tackle both at the
            same time it feels near impossible. Once separated

    """
    if abs(len(str1) - len(str2)) > 1:
        return False

    if len(str1) - len(str2) == 0:
        mistake = 0
        """ replace case """
        for index, l1 in enumerate(str1):
            if l1 != str2[index]:
                if mistake == 1:
                    return False
                mistake = 1
    else:
        if len(str1) <= len(str2):
            small = str1
            big = str2
        else:
            small = str2
            big = str1
        for index, l1 in enumerate(small):
            if l1 != big[index + mistake]:
                if mistake == 1:
                    return False
                mistake = 1

