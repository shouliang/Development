# coding=utf-8
# 标准做法
def quicksort(array, low, high):
    if low < high:
        pivot_index = partition(array, low, high)
        # 找到中间位置后，分别递归调用前半部分和后半部分
        quicksort(array, low, pivot_index - 1)
        quicksort(array, pivot_index + 1, high)


# 数组分区函数：左大右小，这是一趟排序情况
def partition(array, low, high):
    # Find the pivot and exchange it with the last item
    middle = (low + high) // 2
    pivot_value = array[middle]
    swap(array, middle, high)

    # Set stored_index point to first position
    stored_index = low

    # Move items less than pivot to the low
    for index in range(low, high):
        if array[index] < pivot_value:
            swap(array, index, stored_index)
            stored_index += 1  # 交换位置后自增1，代表下一个可能交换的位置

    # 将基准位置放到最后正确的位置上
    swap(array, stored_index, high)
    return stored_index


# 交换数组中两个下标对于的元素
def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


arr = [3, 7, 8, 5, 2, 1, 9, 5, 4]
quicksort(arr, 0, len(arr) - 1)
print(arr)
