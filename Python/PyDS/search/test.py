def binarySearch(nums,value):
    if not nums: return -1
    
    low, high = 0,len(nums) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] == value:
            return mid 
        elif nums[mid] > value:
            high = mid - 1
        else:
            low = mid + 1
    return - 1


# test
nums = [2, 5, 6, 8, 9, 11, 20, 25]  # 二分查找 必须是已经排序好的数组

# 返回在数组中的下标
for value in nums:
    index = binarySearch(nums,value)
    print(index)