""" 4.12 Paths With Sum """

"""
    Given A b-tree, each node contains an integer. Design an algorithm
    to count the numer of paths that sum to a given value. The path does
    not need to start or end at the root or a ;leaf, but it must go downwards

    Notes:
        Where to start and where to end? Is it a bst?
        Can start anywhere, can end anywhere on its path.

        Seems like a DFS problem with a runtime of O(N)

        Would keeping track of the sum up to a certain node make any sense?

        I need to effectively maintain a record of all sums up to this
        specific node and then apply this node against all of those specific
        sums to see if it adds up, and add +1 to the counter


    BCR:O(N)
"""
def paths_with_sum(tree, val):
    """Time Complexity: O(Nlog(N))"""
    paths_with_sum_helper(node, [], 0, val)

def paths_with_sum_helper(node, sums_array, counter, check_val):
    for index, val in enumerate(sums_array):
        new_val = val + node.val
        sums_array[index] = new_val
        if new_val == check_val:
            counter = counter + 1
    sums_array.append(node)

    paths_with_sum_helper(node.leftChild, sums_array, counter, check_val)
    paths_with_sum_helper(node.rightChild, sums_array, counter, check_val)
