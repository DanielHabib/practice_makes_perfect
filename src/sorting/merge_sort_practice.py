""" Merge Sort Practice """

unsorted = [1,23,4,57,2,5,345,12,43,234,543,244,233,52536,12]

def merge_sort(unsorted):
    """ Merge Sort Algorithm
        ** Without help """
    if len(unsorted) > 1:
        mid = len(unsorted)//2
        left = unsorted[:mid]
        right = unsorted[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0 # Left
        j = 0 # Right
        k = 0 # Full

        while len(left) > i and len(right) > j:
            if left[i] < right[j]:
                unsorted[k] = left[i]
                i = i + 1
            else:
                unsorted[k] = right[j]
                j = j + 1
            k = k + 1
        while len(left) > i:
            unsorted[k] = left[i]
            i = i + 1
            k = k + 1
        while len(right) > j:
            unsorted[k] = right[j]
            j = j + 1
            k = k + 1

        print 'Merge Complete'


def merge_sort_2(unsorted):
    """ Merge Sort Round 2, extra practice

        Mistakes::
            I made a second  `if` statement instead of the else,
            this causes a tie to not act correctly
    """

    if len(unsorted)>1:
        mid = len(unsorted)//2
        left = unsorted[:mid]
        right = unsorted[mid:]
        merge_sort_2(left)
        merge_sort_2(right)
        i = 0
        j = 0
        k = 0
        while len(left) > i and len(right) > j:
            if left[i] < right[j]:
                unsorted[k] = left[i]
                i = i + 1
            else:
                unsorted[k] = right[j]
                j = j + 1
            k = k + 1

        while len(left) > i:
            unsorted[k] = left[i]
            i = i + 1
            k = k + 1
        while len(right) > j:
            unsorted[k] = right[j]
            j = j + 1
            k = k + 1


if __name__=='__main__':
    merge_sort_2(unsorted)
    print unsorted
