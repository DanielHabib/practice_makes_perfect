""" Merge Sort Practice """

unsorted = [1, 23, 4, 57, 2, 5, 345, 12, 43, 234, 543, 244, 233, 52536, 12]


def merge_sort(unsorted):
    """ Merge Sort Algorithm
        ** Without help """
    if len(unsorted) > 1:
        mid = len(unsorted) // 2
        left = unsorted[:mid]
        right = unsorted[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0  # Left
        j = 0  # Right
        k = 0  # Full

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


def merge_sort_2(unsorted):
    """ Merge Sort Round 2, extra practice

        Mistakes::
            I made a second  `if` statement instead of the else,
            this causes a tie to not act correctly
    """

    if len(unsorted) > 1:
        mid = len(unsorted) // 2
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


def merge_sort_3(alist):
    """ Round 3 """
    if len(alist) > 1:
        mid = len(alist) // 2
        left = alist[: mid]
        right = alist[mid:]

        merge_sort_3(left)
        merge_sort_3(right)

        i = 0
        j = 0
        k = 0

        while len(left) > i and len(right) > j:
            if left[i] < right[j]:
                alist[k] = left[i]
                i = i + 1
            else:
                alist[k] = right[j]
                j = j + 1
            k = k + 1

        while len(left) > i:
            alist[k] = left[i]
            i = i + 1
            k = k + 1

        while len(right) > j:
            alist[k] = right[j]
            j = j + 1
            k = k + 1


def mergesort4(alist):
    """ Round four Leggos """
    """
        Written Perfectly on the first try in 3 minutes w0000000t
    """
    if len(alist) > 1:
        mid = len(alist) // 2
        left = alist[:mid]
        right = alist[mid:]

        mergesort4(left)
        mergesort4(right)

        i = 0
        j = 0
        k = 0

        while len(left) > i and len(right) > j:
            if left[i] < right[j]:
                alist[k] = left[i]
                i = i + 1
            else:
                alist[k] = right[j]
                j = j + 1
            k = k + 1

        while len(left) > i:
            alist[k] = left[i]
            i += 1
            k += 1

        while len(right) > j:
            alist[k] = right[j]
            j += 1
            k += 1


def mergesort5(alist):
    """
        First time practicing in two weeks, lets see how it goes
        args:
            alist: list, an unsorted list
        result:
            alist that is sorted
    """
    if len(alist) > 1:
        mid = len(alist) // 2
        left = alist[: mid]
        right = alist[mid:]

        mergesort5(left)
        mergesort5(right)

        i = 0
        j = 0
        k = 0

        while len(left) > i and len(right) > j:
            if left[i] < right[j]:
                alist[k] = left[i]
                i = i + 1
            else:
                alist[k] = right[j]
                j = j + 1
            k = k + 1
        while len(left) > i:
            alist[k] = left[i]
            k = k + 1
            i = i + 1
        while len(right) > j:
            alist[k] = right[j]
            k = k + 1
            j = j + 1

    return alist


def mergesort6(alist):
    """ Merge sort attempt 6 """
    if len(alist) > 1:
        mid = len(alist) // 2
        left = alist[: mid]
        right = alist[mid:]

        mergesort6(left)
        mergesort6(right)

        i = 0
        j = 0
        k = 0

        while len(left) > i and len(right) > j:
            if left[i] < right[j]:
                alist[k] = left[i]
                i = i + 1
            else:
                alist[k] = right[j]
                j = j + 1
            k = k + 1
        while len(left) > i:
            alist[k] = left[i]
            i = i + 1
            k = k + 1
        while  len(right) > j:
            alist[k] = right[j]
            j = j + 1
            k = k + 1


def mergesort7(alist):
    """ Round 7 """
    if len(alist) > 1:
        mid = len(alist)//2
        left = alist[: mid]
        right = alist[mid:]

        mergesort7(left)
        mergesort7(right)

        i = 0 # left
        j = 0 # right
        k = 0 # Full list

        while len(left) > i and len(right) > j:
            if left[i] < right[j]:
                alist[k] = left[i]
                i = i + 1
            else:
                alist[k] = right[j]
                j = j + 1
            k = k + 1
        while len(left) > i:
            alist[k] = left[i]
            i = i + 1
            k = k + 1
        while len(right) > j:
            alist[k] = right[j]
            j = j + 1
            k = k + 1

def mergesort8(alist):
    """
        time:
            2:41
        errors:
            I accidentally ordered them in descending order because
            I used the wrong conditional

    """
    if len(alist) > 1:
        mid = len(alist)//2
        left = alist[: mid]
        right = alist[mid:]

        mergesort8(left)
        mergesort8(right)

        i = 0
        j = 0
        k = 0

        while len(left) > i and len(right) > j:
            if left[i] < right[j]:
                alist[k] = left[i]
                i = i + 1
            else:
                alist[k] = right[j]
                j = j + 1
            k = k + 1
        while len(left) > i:
            alist[k] = left[i]
            i = i + 1
            k = k + 1
        while len(right)> j:
            alist[k] = right[j]
            j = j + 1
            k = k + 1


if __name__ == '__main__':
    mergesort8(unsorted)
    print(unsorted)
