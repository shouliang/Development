def merge_sort(alist):
    merge_sort_helper(alist, 0, len(alist) - 1)


def merge_sort_helper(alist, low, high):
    if low >= high:
        return
    mid = low + (high - low) // 2
    merge_sort_helper(alist, low, mid)
    merge_sort_helper(alist, mid+1, high)
    merge(alist, low, mid, high)


def merge(alist, low, mid, high):
    i, j = low, mid+1
    temp = []
    while i < low and j < high:
        if alist[i] < alist[j]:
            temp.append(alist[i])
            i += 1
        else:
            temp.append(alist[j])
            j += 1
    start, end = i, mid
    if j < high:
        start, end = j, high
    while start < end:
        temp.append(alist[start])
        start += 1
    for i in range(low, high+1):
        alist[i] = temp[i]


alist = [5, 4, 1, 3, 7, 9, 8]
merge_sort(alist)
print(alist)
