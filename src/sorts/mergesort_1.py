def mergesort(a):
    
    if len(a) <= 1:
        return a

    mid = len(a) // 2
    left = mergesort(a[: mid])
    right = mergesort(a[mid:])

    i = 0 # left
    j = 0 # right
    k = 0 # total

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1
    
    return a

if __name__ == '__main__':
    import random
    
    print(mergesort([random.randint(0, 100) for x in range(20)]))
    



