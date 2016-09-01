
def stairs(n, steps):
    arr = [0] * (n + 1)
    arr[0] = 1
    for current_step in range(n + 1):
        for step in steps:
            if step > current_step:
                continue
            arr[current_step] += arr[current_step - step]
    print arr
    return arr[-1]

def stairs_r(n, stairs):
    if n == 0:
        return 1
    total = 0
    for stair in stairs:
        if stair > n:
            continue
        total += stairs_r(n-stair, stairs)

    return total

if __name__ == '__main__':
    
    print 'iterative: {0}'.format(stairs(10, [1,2,3]))
    print 'recursive: {0}'.format(stairs_r(10, [1,2,3]))

                
