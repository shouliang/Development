# coding=utf-8
# 通常做法


def partition(alist, low, high):
    middle = (low + high) // 2
    pivot_value = alist[middle]
    swap(alist, middle, high)

    # 两端向中间扫描，然后交换
    while low < high:
        while low < high and alist[high] >= pivot_value:
            high -= 1
        swap(alist, low, high)

        while low < high and alist[low] < pivot_value:
            low += 1
        swap(alist, low, high)

    return low


def quick_sort(alist, low, high):
    if low < high:
        pivot_index = partition(alist, low, high)
        quick_sort(alist, low, pivot_index - 1)
        quick_sort(alist, pivot_index + 1, high)


def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


alist = [3, 7, 8, 5, 2, 1, 9, 5, 4]
quick_sort(alist, 0, len(alist) - 1)
print(alist)
