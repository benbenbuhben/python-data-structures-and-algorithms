def insert_shift_array(arr, n):

    arr = arr + [0]

    for i in range(len(arr)//2, len(arr) - 1):
        reverse_index = len(arr) + (len(arr)//2 - i)
        arr[reverse_index - 1] = arr[reverse_index - 2]

    arr[len(arr)//2] = n

    return arr
