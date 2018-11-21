# coding=utf-8

def quicksort(arr, left, right):
    if left < right:
        pivotLocation = partition(arr, left, right)
        # 找到中间位置后，分别递归调用前半部分和后半部分
        quicksort(arr, left, pivotLocation - 1)
        quicksort(arr, pivotLocation + 1, right)


# 数组分区函数：左大右小，这是一趟排序情况
def partition(arr, left, right):
    # Find the pivot and exchange it with the last item
    middle = (left + right) // 2
    pivot = arr[middle]
    swap(arr, middle, right)
    # Set boundary point to first position
    boundary = left

    # Move items less than pivot to the left
    for index in range(left, right):
        if arr[index] < pivot:
            swap(arr, index, boundary)
            boundary += 1  # 交换位置后自增1，代表下一个可能交换的位置
    # 将基准位置放到最后正确的位置上
    swap(arr, right, boundary)
    return boundary


# 交换数组中两个下标对于的元素
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


arr = [3, 7, 8, 5, 2, 1, 9, 5, 4]
quicksort(arr, 0, len(arr) - 1)
print(arr)
