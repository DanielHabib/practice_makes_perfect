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


    BCR:O(N)
"""
def paths_with_sum()
