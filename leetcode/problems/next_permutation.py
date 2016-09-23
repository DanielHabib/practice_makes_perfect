'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
[1,3,2] -> [2,3,1]


given a list, must find the next greatest permutation, if that doesnt exist, find the smallest
Axium: No Guarentees about the range, No Guarentees about unique numbers, ascending order is the smallest possible, while descending order is the greatest possible, swapping must not use and extra memory.
Notes:
    unable to use python `sorted` because timsort creates a sorted copy of the lsit
   
'''


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        if len(nums) > 1:
            prev = None
            smallest_value_past_right = 0
            smallest_index_past_right = 0
            farthest_right_index = 0
            
            for index,element in enumerate(nums):
                if index == 0:
                    prev = element
                    continue
                if element > prev:
                    farthest_right_index = index - 1
                    smallest_value_past_right = element
                    smallest_index_past_right = index
                else:
                    if element < smallest_value_past_right:
                        smallest_value_past_right = element
                        smallest_index_past_right = index    
                prev = element
    
            if farthest_right_index > 0:
                nums[farthest_right_index], nums[smallest_index_past_right] = nums[smallest_index_past_right], nums[farthest_right_index]
		left = farthest_right_index + 1
                sortedLeftHalf = sorted(nums[left:])
                nums[left:] = sortedLeftHalf

            else:
                i = 0
                j = len(nums) - 1
        
                while i <= j:
                    nums[j], nums[i] = nums[i], nums[j]
                    i += 1
                    j -= 1


























