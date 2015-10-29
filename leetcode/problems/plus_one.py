class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        
        NOTES: It says number, not int. Not negative. Decimals? It can't be as easy as adding one to the last value of the array.
            I don't know how they would differentiate, would there be a period in therE? Wihtout seeing data it would be hard to tell.
            
            Assume ints for now.
            
            The only trick I can think of is if the values are all at 9, adding 1 will cause a cascasding 9->0.
            Some recursion may be neccesary in this one. 
            
            Instead of recursing, I could just loop through the reverse of the array.
            This could give me some fun exposure to looping through a reverse array while still maintaing the place in the actual array
            
        BigO
        """
        if not digits:
            return 1
        
        rev_dig = digits[::-1]
        for index, val in enumerate(rev_dig):
            if index == 0:
                if val == 9:
                    rev_dig[index] = 0
                    if len(rev_dig) - 1 == index:
                        rev_dig.append(1)
                        return rev_dig[::-1]
                    else:
                        rev_dig[index + 1] += 1
                else:
                    rev_dig[index] = val + 1
                    return rev_dig[::-1]
            else:
                if val == 10:
                    rev_dig[index] = 0
                    if len(rev_dig) - 1 == index:
                       rev_dig.append(1)
                       return rev_dig[::-1]
                    else:
                        rev_dig[index + 1] += 1
                else:
                    return rev_dig[::-1]
                
        return rev_dig[::-1]
