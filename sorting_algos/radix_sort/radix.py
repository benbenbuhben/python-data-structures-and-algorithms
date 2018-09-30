def radix_sort(arr):
    most_sd = 0

    for el in arr:
        curr_sd = len(str(el))
        if curr_sd > most_sd:
            most_sd = curr_sd

    for i in range(len(arr)):
        curr = str(arr[i])
        while(len(curr) < most_sd):
            curr = '0' + curr
            arr[i] = curr

    radices = [None] * most_sd

    for i in range(most_sd-1, 0, -1):

        for el in arr:
            radix = int(list(el)[i])
            if not radices[radix]:
                radices[radix] = []
            radices[radix].append(el)

        index = 0
        for radix in radices:
            if radix:
                while len(radix):
                    arr[index] = radix.pop(0)
                    index += 1

    for i in range(len(arr)):
        arr[i] = int(arr[i])

    return arr
