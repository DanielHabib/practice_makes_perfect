class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        
        NOTES: We just need to find out if a palindrome is possible not what they actually are. We can loop through the dict, story the amount of times a value appears, and then search based off of some criterion. 
        
            If odd: all vals must have even counts, one should have an odd
            if even: all should have even counts
        
        DS: Dictionary
        
        BCR: O(N) - have to touch each once
        
        """
        adict = {}
        for letter in s:
            count = adict.get(letter, 0)
            count = count + 1
            adict[letter] = count
        """Tolerance, odd gives us one failure, even gives us 0 failures"""
        tolerance = bool(len(s) % 2)
        for val in adict.values():
            if val % 2:
                if tolerance:
                    tolerance = False
                else:
                    return False
        return True
            
