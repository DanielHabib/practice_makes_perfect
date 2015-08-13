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



def quicksort2(alist):
    """ User facing quicksort """
    quick_sort_helper(alist, 0, alist[-1])


def quicksort_helper(alist, first, last):
    """  Recursive portion of the quick sort """
    if first < last:
        split_point = partition(alist, first, last)

        quicksort_helper(alist, first, split_point - 1)
        quicksort_helper(alist, split_point + 1, last)

def partition2(alist, first, last):
    """ Most of the logic in the quicksort 

        THIS IS WRONG, THE SWITCH AT THE END IS INCORRECT
    """
    pivot_value = alist[0]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:
        # What do we check now?
        while alist[leftmark] < pivot_value and leftmark<=rightmark:
            leftmark = leftmark + 1
        while alist[leftmark] < pivot_value and leftmark<=rightmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else :
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[leftmark]
    alist[leftmark] = alist[rightmark]
    alist[rightmark] = temp
    return rightmark





def quicksort3(alist):
    """ 3rd Round of Quicksort practice """
    quicksort_helper(alist, 0, len(alist)-1)



def quicksort_helper(alist, first, last):
    """ Handles the Recursive aspect of quicksort """
    if first < last:
        split_point = partition3(alist, first, last)
        quicksort_helper(alist, first, split_point - 1)
        quicksort_helper(alist, split_point + 1, last)


def partition3(alist, first, last):
    """ Run the actual quick sort partition process """
    pivot_value = alist[first]
    leftmark = alist[first + 1]
    rightmark = alist[last]

    done = False
    while not done:
        while alist[leftmark] < pivot_value and leftmark < rightmark:
            leftmark += 1
        while alist[rightmark] > pivot_value and leftmark < rightmark:
            rightmark -= 1
        # Why is this the complete condiditon
        if rightmark < leftmark:
            done = True
        else:
            temp = alist[rightmark]
            alist[rightmark] = alist[leftmark]
            alist[leftmark] = temp
    temp = alist[rightmark]
    alist[rightmark] = pivot_value
    alist[first] = temp
    return rightmark


def quicksort4(alist):
    """ Round 4 """
    """ First call the starting point for the recursion """
    quicksort_helper4(alist, 0, len(alist)-1)

def quicksort_helper4(alist, first, last):
    """ This function handles the recursion

    """
    if first < last:
        split_point = partition4(alist, first, last)
        quicksort_helper4(alist, first, split_point - 1)
        quicksort_helper4(alist, split_point + 1, last)


def partition4(alist, first, last):
    """ This handles the actual quick sort logic of the algorithm
        Starting with a left mark and a right mark we slowly move them inward
        constantly comparing and if we find that one is on the wrong side,
        then we switch them.
    """

    pivot_value = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False
    print 'new'
    print 'leftmark: ' + str(leftmark)
    print 'rightmark:' + str(rightmark)
    while not done:
        """ This handles the moving of the left and right marks """
        """ The ORDER CONDITIONALS COME IN IN THE AND STATEMENTS MATTERS """
        while leftmark <= rightmark and alist[leftmark] <= pivot_value :
            leftmark = leftmark + 1
            print leftmark
        while alist[rightmark] >= pivot_value and rightmark >= leftmark:
            rightmark = rightmark - 1

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


def quicksort5(alist):
    quicksort_helper5(alist, 0, len(alist)-1)


def quicksort_helper5(alist, first, last):
    if len(alist) > 1:
        split_point = partition5(alist, first, last)
        quicksort_helper5(alist, first, split_point - 1)
        quicksort_helper5(alist, split_point + 1, last)

def partition5(alist, first, last):
    done = False
    pivot_value = alist[first]
    leftmark = first + 1
    rightmark = last
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivot_value:
            leftmark = leftmark + 1
        while leftmark <= rightmark and alist[rightmark] >= pivot_value:
            rightmark = rightmark - 1

        if leftmark > rightmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
    temp = alist[rightmark]
    alist[rightmark] = pivot_value
    alist[first] = temp
    return rightmark


def quicksort7(alist):
    """
        time: 5:40
        error: 
            Bad implementation on quicksort_helper7
            The conditional in quicksort_helper7 should be first < last
    """
    quicksort_helper7(alist, 0, len(alist) - 1)

def quicksort_helper7(alist, first, last):
    if first < last:
        split_point = partition7(alist, first, last)
        quicksort_helper7(alist, first, split_point - 1)
        quicksort_helper7(alist, split_point + 1, last)

def partition7(alist, first, last):
    done = False
    pivot_value = alist[first]
    leftmark = first + 1
    rightmark = last
    print 'start' + str(rightmark)
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivot_value:
            leftmark = leftmark + 1
        while leftmark <= rightmark and alist[rightmark] >= pivot_value:
            rightmark = rightmark - 1

        if leftmark > rightmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
    print rightmark
    temp = alist[rightmark]
    alist[rightmark] = pivot_value
    alist[first] = temp
    return rightmark



alist = [1,2,3,45,5,36,45,65,47,45,7645,7,457,54,6,456,45,6,2,34]

if __name__ == '__main__':
    quicksort7(alist)
    print(alist)

