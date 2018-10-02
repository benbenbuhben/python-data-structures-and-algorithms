def merge(arr, front, mid, back):
    print(arr)
    n1 = mid - front + 1
    n2 = back - mid

    L = [0] * n1
    R = [0] * n2

    for i in range(0, n1):
        L[i] = arr[front + i]

    for j in range(0, n2):
        R[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = front

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, front, back):
    if front < back:
        mid = (front + (back - 1))//2

        merge_sort(arr, front, mid)
        merge_sort(arr, mid + 1, back)

        merge(arr, front, mid, back)

