'''

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

EXAMPLE:
prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]



desc: Find the maximum value that can be achieved by buying and selling stocks, with the kicker being if there is a short cooldown of one step between selling and when you can buy again.
Axiums: there is a cooldown of 1 step, the array is valid(Contains exclusively numbers), all values in the array are integers, Can buy and sell multiple times
Assumptions: Not Interetsed in losing money, 


Examples:
    [1,2,3,4,5] => 4
    [1,2,3,2,1] => 2
    [5,2,3,6,2,30] => 29
    [] =>




Approach

    Greedy <= Seems too complicated for a greedy algorithm. moving from [5,2,3,6,2,30] => [5,2,3,6,2,30, 0,40]
    What if everytime a new local minima or maxima is found, we can try differnet taking it, or skipping it. XXXX Condition that breaks this => [1, 7, 8, 0, 8]
    *it seems like we may need to exhaustively try buying and selling at every point. I am coming to this conclusion because there are points that are not minima or maxima that we may need to buy/sell at. => this would work but would be very slow, specifically I think it would be O(3^n)

    BC:
        if currentIndex >= len(arr): return 0
    Recursion: #Try all 3 possibilities
        skip = recurse(n, currentIndex + 1, onCooldown=False, hasStock=hasStock, stockIndex=-1)
        transaction = 0
        if hasStock:
            transaction = recurse(n, currentIndex + 2, onCooldown=False, hasStock=True, stockIndex=-1) + n[0] - n[stockIndex]
        else:
            transaction = recurse(n, currentIndex + 1, onCooldown=True, hasStock=False)
        return max(skip, transaction)
 
     Memoize:
         Base memo off of currentIndex

'''
'''

        :type prices: List[int]
        :rtype: int
        """
        self.memo = [-1] * len(prices)
        return self.recurse(prices, 0, onCooldown=False, hasStock=False, stockIndex=-1)

    def _recurse(self, prices, currentIndex, onCooldown=False, hasStock=False, stockIndex=-1):
        if memo[currentIndex] != -1:
            return memo[-1]

        if currentIndex >= len(prices):
            return 0

        skip = self.recurse(n, currentIndex +1, onCooldown=False, hasStock, stockIndex)
        transaction = 0
        if hasStock:
'''



class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        self.hasStockMemo = [-1] * len(prices)
        self.doesntHaveStockMemo = [-1] * len(prices)
        self.count = 0
        value = self.recurse(prices, 0, hasStock=False, stockIndex=-1)
        
        return value

    def recurse(self, prices, currentIndex, hasStock=False, stockIndex=-1):
            
        self.count += 1
        if currentIndex >= len(prices):
            return 0
            
        if hasStock and self.hasStockMemo[currentIndex] != -1:
            return self.hasStockMemo[currentIndex]
        if not hasStock and self.doesntHaveStockMemo[currentIndex] != -1:
            return self.doesntHaveStockMemo[currentIndex]
            
            
        skip = self.recurse(prices, currentIndex +1,  hasStock, stockIndex)
        transaction = 0
        if hasStock:
            transaction = self.recurse(prices, currentIndex + 1, hasStock=False, stockIndex=-1) + prices[currentIndex] - prices[stockIndex]
                
        else:
            transaction = self.recurse(prices, currentIndex + 1, hasStock=True, stockIndex=currentIndex)
               
        result = max(skip, transaction) 
        '''
        if hasStock:
            self.hasStockMemo[currentIndex] = result
        else:
            self.doesntHaveStockMemo[currentIndex] = result 
        # self.memo[currentIndex] = max(skip, transaction)
        '''
        return result
   
if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([48,12,60,93,97,42,25,64,17,56,85,93,9,48,52,42,58,85,81,84,69,36,1,54,23,15,72,15,11,94]))
