# coding=utf-8

# 二分查找
def binary_search(numbers, key):
    if not numbers:
        return -2
    # 初始化low和high下标
    low = 0
    high = len(numbers) - 1
    # 循环中改变low或者high指针，但是循环条件始终low<=high,最坏情况是查询的数字是最后一个，终止条件为low=high
    while low <= high:
        # mid = (low + high) / 2 为防止low + high大于最大数导致溢出
        # 因为(high - low) >> 1 = low + (high - low)/2 = (low + high) / 2
        # 但是右移一位比除以2速度要快
        middle = low + ((high - low) >> 1)
        if numbers[middle] == key:
            return middle
        if numbers[middle] > key:
            high = middle - 1
        if numbers[middle] < key:
            low = middle + 1

    return -1

# test
numbers = [2, 5, 6, 8, 9, 1, 0, 11]
key = 8

# 返回在数组中的下标
key_index = binary_search(numbers, key)
print(key_index)
