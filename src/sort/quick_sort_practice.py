""" Just Practicing my quick sort """

""" Perks:
        Quicksort gains the same advantages as Mergesort while not using
        not using the additional storage that Mergesort uses
    Trade-offs:
        There is a chance that quicksort will not split the list in half,
        which will result in a performance hit

    Pivot, Leftmark, Rightmark

    Notes::: If a list length is <=1 it is sorted by definition
"""

def quick_sort(alist):
    """ First Quicksort Practice """
    """ This Method simply starts the sort by passing in the full list
        and supplying the proper indices
    """
    quick_sort_helper(alist, 0, len(alist) - 1)

def quick_sort_helper(alist, first, last):
    """ Quicksort helper """
    """ This method calls quicksort on the proper parts of itself
        This method handles the recursion
    """
    if first<last: # Ensure first position doesn't match
        split_point = partition(alist, first, last)

        quick_sort_helper(alist, first, split_point - 1)
        quick_sort_helper(alist, split_point + 1, last)

def partition(alist, first, last):
    """ This is where the meat of the function lies """
    """
        1. First we declare the first value in the array to be the
           pivot_value and we also set the left and right marks
        2. We create the first while loop, this while loop is there to tell
           the partition process to run again if it doesn't satisfy the
           necessary condition
        3. then we apply the partition process
        4. after both partition processes have ran, we check to see if it
           satisfies the proper condition. If it does, we mark it as done,
           if not we switch the left and right values and apply it again
        5. Once its done switch the left and right values and return the
           split_point
    """
    pivot_value = alist[first] # Choose a pivot

    leftmark = first + 1 # set the left mark
    rightmark = last # set the right mark

    done = False
    while not done:
        # Apply Conditions
        while leftmark <= rightmark and alist[leftmark] <= pivot_value:
            leftmark = leftmark + 1
        while alist[rightmark] >= pivot_value and rightmark >= leftmark:
            rightmark = rightmark - 1
        # Check if the applied conditions are complete, or if they have to
        # be applied again
        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

alist = [1,2,3,45,5,36,45,65,47,45,7645,7,457,54,6,456,45,6,2,34]
if __name__ == '__main__':
    quick_sort(alist)
    print(alist)

