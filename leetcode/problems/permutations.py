'''
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:

[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
	if len(nums) <= 1:
            return [nums]
        final_result = []
        for index in range(len(nums)):
            sub_result = self.permute(nums[:index] + nums[index+1:])
            for result in sub_result:
                result.append(nums[index])
                final_result.append(result)
        return final_result
       
if __name__ == '__main__':
    sol = Solution()
    print sol.permute([1,3,4,5])

