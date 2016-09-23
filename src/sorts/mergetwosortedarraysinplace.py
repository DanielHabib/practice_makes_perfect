'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n)
to hold additional elements from nums2. The number of elements initialized in nums1 and nums2
are m and n respectively.

'''

'''
    Simplify

'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        sortedList = []
        count1 = 0
        count2 = 0
        while count1 < m and count2 < n:
            if nums1[count1] < nums[count2]:
                sortedList.append(nums1[count1])
                count1 += 1
            else:
                sortedList.append(nums2[count1])
                count2 += 1

        while count1 < m:
            sortedList.append(nums1[count1])
            count1 += 1

        while count2 < n:
            sortedList.append(nums1[count2])
            count2 += 1

        return sortedList


    def mergeInPlace(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        sortedList = []
        count1 = 0
        count2 = 0
        while count1 < m and count2 < n:
            if nums1[count1] < nums[count2]:
                sortedList.append(nums1[count1])
                count1 += 1
            else:
                sortedList.append(nums2[count1])
                count2 += 1

        while count1 < m:
            sortedList.append(nums1[count1])
            count1 += 1

        while count2 < n:
            sortedList.append(nums1[count2])
            count2 += 1

        return sortedList
