# coding=utf-8

# 二分查找
def binary_search(numbers, key):
    if not numbers:
        return -2
    # 初始化start和end下标
    start = 0
    end = len(numbers) - 1
    # 循环中改变start或者end指针，但是循环条件始终start<=end,最坏情况是查询的数字是最后一个，终止条件为start=end
    while start <= end:
        # mid = (start + end) / 2 为防止start + end大于最大数导致溢出
        # 因为(end - start) >> 1 = start + (end - start)/2 = (start + end) / 2
        # 但是右移一位比除以2速度要快
        middle = start + ((end - start) >> 1)
        if numbers[middle] == key:
            return middle
        if numbers[middle] > key:
            end = middle - 1
        if numbers[middle] < key:
            start = middle + 1

    return -1

# test
numbers = [2, 5, 6, 8, 9, 1, 0, 11]
key = 8
# 返回在数组中的下标
key_index = binary_search(numbers, key)
print(key_index)
