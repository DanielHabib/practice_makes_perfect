'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.


Desc: Find the optimal buying and selling point in an array that represtns stock prices throughout the day

Axium: Only one transaction, We can forgoe a transaction
Assumption: No Negative Values, Input is Valid, Input is integers, values can duplicat
 NOtes: not sorted, it is being processed in order, so position matters.
We cant change the position, meaning binary search could be useless in this case

We will have to touch each element at least once, so best case we could POTENTIALLY get a linear runtime with constant space.

Investigate:
    Greedy Algorithm - is there someway we can know the result if we add on one more value. Would be tightly bounded with a linear runtime
    Prefix Array Paired with a Binary Tree - would help us find the most profitable transaction at every position. Would be upper bounded with super linear runtime and lower bounded with a linear runtime
    Brute Force Approach - compare every element with every other element before it to find the best selling time.


I think now I'm ready to approach the problem


Greedy -> 
If I have the input [7,2,4] -> 2 (4 - 2)
If we add 5 [7,2,4,5] -> How can I tell whether 5 should or shouldnt be the new answer, well we know it is greater than the current greatest selling price.
If we add a 1 now -> [7,2,4,5,1] How can I tell that the result is unchanged but future values should reference this one, change the lowest found value but  dont change the highest profit

If at every point we subtract the current value from the lowest seen so far,  

'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type priczs: List[int]
        :rtype: int
        """
        max_profit_so_far = 0
        if prices == []:
            return max_profit_so_far
	lowest_val_so_far = prices[0]
        for price in prices:
            max_proft_so_far = max(max_profit_so_far, price - lowest_val_so_far)
            lowest_val_so_far = min(lowest_val_so_far, price)

        return max_profit_so_far


        
