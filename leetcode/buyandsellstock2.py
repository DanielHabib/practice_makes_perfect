'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). 
However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Examples: 
    [1,6] -> 5
    [1,3,6] -> 5
    [5,3,1] -> 0
    [5,2,3,4,1,6] -> 7
    [4,2,5,6,16,7,4] -> 14
    [3,5,4,10] -> 8
    [1,0,0,1] -> 1 
    
    
Desc: Given an array with the price of a stock on a sequence of days. Find the maximum profit, there may be multiple solutions that yield the same results
Axiums: Arrays can be of any length, We only want to return positive values,
Assumptions: Input is Valid, We will not receve negative prices on days since that doesnt exist, consecutive duplicates are available

Approaches:
    Find local Maxima and subtract them from previous local minima to find local profits. Add all of these profits together to get a result.
    How to find local minia and maxima:

    
    Greedy : One a single pass, create an array of local minima and local maxima array. Then subtract every local maxima from the local minima being tightly bounded by a linear time complexity
    Brute Force: Try every possible combination of solutions, potentially being bounded by a factorial time complexity

	
   [4,2,5,6,16,7,4] -> []
   [8,3,7] -> 4
   keeping track of current slope
   keeping track of previous 
if the slope switches we have found either a minima or a maxima
'''


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if len(prices) < 2:
            return 0

	localArray = []
	
        prev = prices[0]
        prevIndex = 0
	i = 0
	while i < len(prices):
            value = prices[i]
	    if i == 0 or i == (len(prices) - 1):
                localArray.append(value)
	        continue
            if value == prev:
                continue
            if value < prices[prevIndex] and value < prices[i + 1]:
                localArray.append(value)
            elif value > prices[prevIndex] and value > prices[i + 1]:
		localArray.append(value)
            elif value == prices[i + 1]:
                j = i
		while value == prices[j + 1] and j < len(prices):
                    j += 1
                if j < len(prices):
                    if value < prices[i - 1] and value < prices[j]:
                        localArray.append(value)
                    if value > prices[i - 1] and value > prices[j]:
                        localArray.append(value)
		i = j
                continue
            prev = value 
            prevIndex = i
            i += 1
            
            
	total = 0
        for index, value in enumerate(localArray):
            if index == 0:
                continue
            if value > localArray[index - 1]:
      	        total += value - localArray[index-1]
	return localArray

   
'''
Local Minima => arr[i -1] > arr[i] < arr[i + 1]
Local Maxima => arr[i-1] < arr[i] >arr[i + 1]
'''













        




