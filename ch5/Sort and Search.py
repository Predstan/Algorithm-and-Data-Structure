def binarysearch(thelist, target):

    # Start with the entire sequence of elements.
    low = 0
    high = len(thelist)-1

    # Repeatedly subdivide the sequence in half until the target is found.
    while low <= high:
        # Find the midpoint of the sequence.
        mid = (high + low) // 2

        # Does the midpoint contain the target?
        if thelist[mid] == target:
            return True

        # Or does the target precede the midpoint?
        elif thelist[mid] > target:
            high = mid - 1 
        # Or does it follow the midpoint?
        else:
            low = mid + 1

    # If the sequence cannot be subdivided further, we're done.
    return False


# Sorts a sequence in ascending order using the bubble sort algorithm.
def bubbleSort(thelist):
    n = 0

    # Perform n-1 bubble operations on the sequence
    for i in range(len(thelist)-1, 0, -1): 

        # Bubble the largest item to the end.   
        for j in range(i):
            # Replace if the value is larger than the next value
            if thelist[j] > thelist[j+1]:
                tmp = thelist[j]
                thelist[j] = thelist[j+1]
                thelist[j+1] = tmp
                n += 1

        # Terminates if there was no replacement of values in one bubbling  
        if n == 0:
            return thelist
        
    return thelist

# Sorts a sequence in ascending order using the selection sort algorithm.
def selectionSort(thelist):
    
    n = len(thelist)
    for i in range(n - 1):
        # Assume the ith element is the smallest.
        smallndx = i
        # Determine if any other element contains a smaller value.
        for j in range( i+1, n):
            # Swap the ith value and smallNdx value only if the smallest value is
            # not already in its proper position.
            if thelist[j] < thelist[smallndx]:
                smallndx = j


        if smallndx != i:
            tmp = thelist[i]
            thelist[i] = thelist[smallndx]
            thelist[smallndx] = tmp

    return thelist


# Sorts a sequence in ascending order using the insertion sort algorithm.
def insertionSort(thelist):

    # Starts with the first item as the only sorted entry.
    for i in range(1, len(thelist)):
        # Save the value to be positioned.
        value = thelist[i]

        # Find the position where value fits in the ordered part of the list.
        pos = i
        while pos > 0 and value < thelist[pos - 1]:
            # Shift the items to the right during the search.
            thelist[pos] = thelist[pos - 1]

            pos -= 1

        # Put the saved value into the open slot.
        thelist[pos] = value
    return thelist


# Modified version of the binary search that returns the index within
# a sorted sequence indicating where the target should be located.
def findSortedPostion(thelist, target):
    low = 0
    high = len(thelist) - 1

    while low < high:
        mid = (high + low) // 2

        if thelist[mid] == target:
            # Index of the target.
            return mid
        
        if thelist[mid] > target:
            high = mid - 1
        
        else:
            low = mid + 1
    # Index where the target value should be.
    return low

# Merges two sorted lists to create and return a new sorted list.
def MergeSortedLists(listA, listB):
    # Create the new list and initialize the list markers.
    newList = list()
    a = 0
    b = 0

    # Merge the two lists together until one is empty
    while a < len(listA) and b < len(listB):
        if listA[a] < listB[b]:
            newList.append(listA[a])
            a += 1

        else:
            newList.append(listB[b])
            b += 1
    # If listA contains more items, append them to newList.
    while a < len(listA):
        newList.append(listA[a])
        a += 1

    # Or if listB contains more items, append them to newList
    while b < len(listB):
        newList.append(listB[b])
        b += 1
    
    return newList
        


