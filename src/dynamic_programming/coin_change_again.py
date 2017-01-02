"""
Coin Change Recursively then iteratively
"""
from collections import defaultdict
import numpy


def make_change(amount, coins, cache=None):
    if cache is None: cache = defaultdict(dict)
    if cache[amount].get(len(coins), False):
        return cache[amount][len(coins)]

    if amount < 0:
        return 0
    if amount == 0:
        return 1
    if coins == []:
        return 0

    numberOfCoins = 0
    currentCoin = coins[0]
    total = 0 
    while currentCoin * numberOfCoins <= amount:
        total += make_change(amount - currentCoin*numberOfCoins, coins[1:])
        numberOfCoins += 1
    cache[amount][len(coins)] = total
    return total


def make_change_iter(amount, coins):
    cache = numpy.zeros([len(coins), amount + 1])
    cache[:, 0] = 1

    x = 0
    y = 1
    
    while x < cache.shape[0]: # Coins
        y = 1
        while y < cache.shape[1]: # Value
            coin = coins[x]
            top = cache[x - 1, y] if x > 0 else 0
            left = cache[x, y - coin] if y >= coin else 0
            cache[x, y] += left + top
            y += 1
        x += 1
    return cache[-1, -1]


if __name__ == '__main__':
    print(make_change(200, [2, 5]))
    print(make_change_iter(200, [2, 5]))
