# coding=utf-8
# 通常做法
def partition(array, low, high):
    middle = (low + high) // 2
    pivot_value = array[middle]
    swap(array, middle, high)

    # 两端向中间扫描，然后交换
    while low < high:
        while low < high and array[high] >= pivot_value:
            high -= 1
        swap(array, low, high)

        while low < high and array[low] < pivot_value:
            low += 1
        swap(array, low, high)

    return low


def quicksort(array, low, high):
    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index - 1)
        quicksort(array, pivot_index + 1, high)


def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


arr = [3, 7, 8, 5, 2, 1, 9, 5, 4]
quicksort(arr, 0, len(arr) - 1)
print(arr)
