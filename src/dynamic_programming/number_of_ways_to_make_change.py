'''
Correct order of operations for the maximum number of ways coin change problem, recursive, recursive memoized, bottom up

'''



def make_change(coins, amount, memo):
    if amount < 0:
	return -1
    if amount == 0:
	return 0
    if amount > 0:    
	if memo.get(amount, False):
	    return memo[amount]
	total = 0
	for value in coins:
	    result = make_change(coins, amount - value, memo)
 	    if amount != -1:
                total += result + 1
	memo[amount] = total
        return total

'''
Why is this incorrect? The issue here is that the order in which a coin shows up doesn't matter.
It is asking for the total number of possible combinations, where order doesn't matter.
'''

def change_possibilities_top_down(amount_left, denominations_left):

    # base cases:
    # we hit the amount spot on. yes!
    if amount_left == 0: return 1
    # we overshot the amount left (used too many coins)
    if amount_left < 0: return 0
    # we're out of denominations
    if len(denominations_left) == 0: return 0

    print "checking ways to make %i with %s" % (amount_left, denominations_left)

    # choose a current coin
    current_coin, rest_of_coins = denominations_left[0], denominations_left[1:]

    # see how many possibilities we can get
    # for each number of times to use current_coin
    num_possibilities = 0
    while amount_left >= 0:
        num_possibilities += change_possibilities_top_down(amount_left, rest_of_coins)
        amount_left -= current_coin

    return num_possibilities

if __name__ == '__main__':  
    print(change_possibilities_top_down(5, [1, 3]))
