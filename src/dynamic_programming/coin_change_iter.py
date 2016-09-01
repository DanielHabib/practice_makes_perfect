
def make_change(n, coins, verbose=False):
    arr = [[0] * len(coins)] * (n + 1)
    # set the base case
    arr[0] = [1] * len(coins)
    for value in range(n + 1):
        for index, coin in enumerate(coins):
            if coin > value:
                continue
            if value % coin == 0:
                current_combinations = arr[value - coin][index]
            if index > 0:
                current_combinations  += arr[value][index - 1]
            if verbose:
                print "Coin {0} Value {1} Current Combo{2}".format(coin, value, current_combinations)
            arr[value][index] = current_combinations
    return arr[-1][-1]

if __name__ == '__main__':
    print make_change(10, [1 , 2, 3])
    # print make_change(10, [1, 5,  ])
