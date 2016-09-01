
def max_subarray(a_list):
    if len(a_list) == 1:
        return [a_list[0], [0, 0]]
    mid = len(a_list) // 2
    left_result, left_indices = max_subarray(a_list[:mid])
    right_result, right_indices = max_subarray(a_list[mid:])
    middle_result, middle_indices = calc_middle_max(a_list, mid)

    if left_result >= right_result & left_result >= middle_result:
        return left_result, left_indices
    elif right_result >= middle_result:
        return right_result, [right_indices[0] + mid, right_indices[1] + mid]
    else:
        return middle_result, middle_indices

def calc_middle_max(a_list, mid):
    i = mid - 1
    j = mid
    max_j = len(a_list) - 1
    highest_left = float('-inf')
    highest_left_index = 0
    highest_right_index = 0
    left_total = 0

    highest_right = float('-inf')
    right_total = 0

    while i >= 0:
        left_total += a_list[i]
        if left_total > highest_left:
            highest_left = left_total
            highest_left_index = i
        i -= 1

    while j <= max_j:
        right_total += a_list[j]
        if right_total > highest_right:
            highest_right = right_total
            highest_right_index = j
        j += 1
    return highest_left + highest_right, [highest_left_index, highest_right_index]


if __name__ == '__main__':
    print max_subarray([-10, 6,8,-9,20,-10,-30,80,9])
