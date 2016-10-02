'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Solve iteratively and recursively
'''

'''
At any Step I can take 1 or 2 steps || I have to  reach the nth step. || Count the way sto reach the nth step
Axiums: ""
'''
Iterative
O:(N)
class Solution(object):
    def climbStairs(self, n):
	arr = [0] * (n + 1)
        arr[0] = 1
        i = 1
        options = [1, 2]
	while i <= len(n):
            for option in options:
                if option <= i:
                    arr[i] += arr[i - option]
	    i += 1
        return arr[-1]

'''
	return self.climb(n, {})
    Recursive
    def climb(self,n ,memo):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return 0
        if n == 0:
            return 1
	if memo.get(n, False):
            return memo[n]

	options = [1,2]	
        total = 0
	for option in options:
   	    total += self.climb(n-option, memo) 
        
        memo[n] = total
        return total
'''     



