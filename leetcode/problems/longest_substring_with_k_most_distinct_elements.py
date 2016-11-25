"""
Given a string, find the length of the longest substring T that contains at most k distinct characters.

For example, Given s = “eceba” and k = 2,

T is "ece" which its length is 3.




Axiums:
    pass
   
Assumptions:
    valid string, ASCII, k cannot be negative

Options:
    1. Starting at every element in the array, find the longest possible substring with k distinct elements in it. 
        Runtime: O(n^2) quadratic upper bound 
        Space: O(n^2)
    2. Leveraging a dynammic programming approach with a cache. Observing that strings are left-to-right structures we can recursively solve smaller and smaller problems
        Runtime: Number of Partial solutions * time to complete each partial solution = kn * 1 = O(kn)
        Space: Call Stack + Memo 
    3. Define an initial strip of k distinct element substring, the increment this chunk along, move the starting index over until it hits a new value and do the same for the last value. This way we can find the longest kth distinct set

Any recursive solution needs its own base cases to terminate it
BC:
    if k == 0:
        return ''
    if string == '':
        return ''

Recursion:
    Either start a new substring or include 


Greedy solution didnt pan out as I hped usually greedy works when there is a little strucutre among the values, lets revisit the recursive solution

That moment when your boy makes that mofo'in linear time solution work! WOOOT WOOOTO OOOWWWWWOOOOOOOOOT

My problem with this one was I initially thought up a brute force solution. I let my mind jump a little to quickly to dynammic programming and I got excited. Instead what I should have done was think up a brute force, then try to think up a greedy solution. If that



Substrings lend themselves to greedy algorithms a little more than subsequences, because we know the impact of adding one more possible value onto the end alot easier than we would if we tried to leverage a subsequence

"""
class Solution(object):
    """
        This solution exceeds the maximum time limit, favor a recursive solution with a memo
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        longestSubstringLength = 0
        for index, letter in enumerate(s):
            currentSubstringLength = self.calc_longest_distance(s, index, k)
            longestSubstringLength = max(currentSubstringLength, longestSubstringLength)
        return longestSubstringLength
    
    def calc_longest_distance(self, string, index, k):
        currentStr = ''
        while index < len(string):
            letter = string[index]
            if letter not in currentStr:
                if k == 0:
                    return len(currentStr)
                k -= 1
            currentStr += letter
            index += 1
        return len(currentStr)
          

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        i, j = 0, 0
        if k == 0 or s == '':
            return 0
        # Set initial J offest
        for value in s:
            if value not in s[:j]:
                if k == 0:
                    break
                k -= 1
            j += 1
        currentLongest = j

        # increment j & i One unique Char at a time
        while j < len(s):
            # Find first new distinct value
            currentString = s[i:j]
            currentI = s[i]
            while i < j:
                i += 1
                if s[i - 1] not in s[i: j]:
                    break

            while j < len(s):
                j += 1
                if j == len(s):
                    break
                if s[j] not in s[i:j]:
                    break
            print(i, j)
            currentLongest = max(currentLongest, j - i)
        return currentLongest



            









