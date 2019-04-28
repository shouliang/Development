# coding=utf-8

# 二分查找: 返回的是待查找的值位于数组中的下标 
# 依赖顺序表结构，即数组，针对有序数据；
# 不太适用动态数组，因为插入删除都需要移动元素
# 不太适用数据小的数组，数据量少不如直接使用顺序查找
# 不太适用数据特别大的数组，因为需要使用连续的内存空间，太大内存可能不够分配
def binarySearch(nums, value):
    if not nums: return -1
       
    low = 0
    high = len(nums) - 1

    # 循环终止条件是 low > high
    while low <= high:
        # mid = (low + high) / 2 为防止low + high大于最大数导致溢出
        # 因为  (low + high) / 2  = low + (high - low)/2  = low + (high - low) >> 1
        # 但是右移一位比除以2速度要快
        mid = low + ((high - low) >> 1)
        if nums[mid] == value:
            return mid
        if nums[mid] > value:
            high = mid - 1
        if nums[mid] < value:
            low = mid + 1

    return -1


# test
nums = [2, 5, 6, 8, 9, 11, 20, 25]  # 二分查找 必须是已经排序好的数组
value = 6

# 返回在数组中的下标
index = binarySearch(nums, value)
print(index)
