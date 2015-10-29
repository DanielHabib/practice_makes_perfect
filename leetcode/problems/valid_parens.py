class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool

        NOTES: Valid Parens Problems come up rather frequently. The behavior we need to acheive is a almost wrapping effect. 
            In this case I htink a stack will solve the problem at hand. By adding values to a stack, we can ensure we unwrap those values i nthe correct order. {[( Would then require a LIFO mentality in order to unwrap the parens.

        BCR: O(N) we have to touch every value of the string to ensure it is valid
        Solution:
            Create a stack that appends values if they belong to the opening set.
            If the value is part of the closing stack however, we need to pop the next value off the stack and it must correspond to the opener.
            We should use a dictionary of valid pairs for this.

        EDGE CASES:
            What if a closer is passed in first?
            What if the end value is an opener?
        """
        amap = {"{": "}", "[": "]", "(":")" }
        stack = []

        for char in s:
            if char in amap:
                """I assumed that `in amap` only searches the keys """
                stack.append(char)
            elif char in amap.values():
                """The Reason I left this as amap.values is if I wanted to expand the problem to have extra character I would need this here to disregard extra characters """
                if len(stack) > 0:
                    opener = stack.pop()
                    if amap[opener] != char:
                        return False
                else: return False
        return not len(stack)

