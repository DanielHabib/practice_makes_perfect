


def cake_thief(max_capacity, cakes):
    arr = [0] * (max_capacity + 1)
    for current_capacity in range(max_capacity + 1):
        for weight, value in cakes:
            if weight > current_capacity:
                continue
            max_value = arr[current_capacity - weight] + value
            arr[current_capacity] = max(max_value, arr[current_capacity])

    return arr[-1]

if __name__ == '__main__':
    print 'cake thief iter: {0}'.format(cake_thief(10, [(2,5), (1,2), (4,10), (5,6),(3,15)]))
