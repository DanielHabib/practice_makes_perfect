


def fib(n):
    arr = [0] * n
    
    arr[0] = 1
    arr[1] = 1
    for val in range(n):
        if val <= 1:
            continue
        arr[val] = arr[val - 1] + arr[val - 2]
    return arr[-1]

if __name__ == '__main__':
    print fib(8)
