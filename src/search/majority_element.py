'''
Given an array of size n, find the majority element.
The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and
the majority element always exist in the array.

'''

'''
Options:
    If a new element is hit, loop through the array and check to see if it appears enough
    times to be considered a majority element. * There may be an opportunity to optimize
        polynomial runtime worst case: O(N^2)
        Constant Space

    If we sort the list, we can then loop through keeping track of the current element
    and how many times it has appeared, to determine if it is a majority element
        runtime O(Nlog(N))
        Constant Space for an inplace sort

    If we loop through all of the elements, keeping track of how many times each
    element has appeared in a dictionary, we can determine if any of the elements are majority elements
        Linear runtime:  O(N)
        Linear Space: O(N)


'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counterDict = {}
        counterDict = len(nums) // 2
        for val in nums:
            counter = breakPoint.get(val, 0)
            counter += 1
            if counter > breakPoint:
                return val
            counterDict[val] = counter
        return False

'''
Majority Element 2
Given an integer array of size n,
find all elements that appear more than ⌊ n/3 ⌋ times.
The algorithm should run in linear time and in O(1) space.
'''
'''
Options:
    Since we want this to run in linear time, and constant space, we are implying
    we are going to loop through the array a fixed amount of times, keeping track of
    a limited number of things to build our solution

    ** I am Stuck **

    I don't know how I can do this in constant space and linear time....
    What are the steps I can take when I'm stuck?
        Simplify the problem
        Brute Force first.

    I don't know what information I can store that can tell me what values appear
    the most often in linear time and constant space.

    What information do I get out of the requirment of frequency of [n/3]
     - There may be a majority element, there may not be a majority element
     - There may be multiple majority elements
     - at most there are 2 majority elements

    Keep track of the majority element so far?
    Look at the solution, find a path from no info to the solution

    [1,2,3,4,5,1,1,1,1,1]
'''

''' Not In Constant Time '''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counterDict = {}
        results = set([])
        breakPoint = len(nums) // 3
        for val in nums:
            counter = breakPoint.get(val, 0)
            counter += 1
            if counter > breakPoint:
                results.add(val)
            breakPoint[val] = counter
        return False
