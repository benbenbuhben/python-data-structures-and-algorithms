def binary_search(arr, k):
    """This function uses the binary search algorithm to split up the array in such a way that half of it can be discarded at each iteration."""
    if not len(arr):
        return -1

    lowest = 0
    highest = len(arr)-1
    middle = (highest + lowest)//2

    while(arr[middle] != k):
        if(lowest > highest):
            return -1
        elif(arr[middle] > k):
            highest = middle - 1
        elif(arr[middle] < k):
            lowest = middle + 1
        middle = (highest + lowest)//2

    return middle
