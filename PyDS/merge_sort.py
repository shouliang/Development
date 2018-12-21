def merge_sort(alist):
    merge_sort_helper(alist, 0, len(alist) - 1)

def merge_sort_helper(alist, low, high):
    if low < high:
        mid = low + (high - low) // 2
        merge_sort_helper(alist, low, mid)
        merge_sort_helper(alist, mid + 1, high)
        merge(alist, low, mid, high)


def merge(alist, low, mid, high):
    i, j = low, mid + 1
    tmp = []

    while i <= mid and j <= high:
        if alist[i] <= alist[j]:
            tmp.append(alist[i])
            i += 1
        else:
            tmp.append(alist[j])
            j += 1
    # start = i if i <= mid else j
    # end = mid if i <= mid else high
    # tmp.extend(alist[start:end + 1])
    # alist[low:high + 1] = tmp


a1 = [3, 5, 6, 7, 8]
merge_sort(a1)
print(a1)