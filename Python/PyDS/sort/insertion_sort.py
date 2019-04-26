# coding=utf-8
def insertionSort(nums):
    n = len(nums)
    for i in range(1, n):     # i从1开始，因为是从未排序的向已排序的部分插入，开始已排序的位数组第一个元素
        itemToInsert = nums[i]
        j = i - 1

        # 循环直到找到比itemToInsert要小的元素，将itemToInsert插入到j的后面一位，即j+1
        while j >= 0 and nums[j] > itemToInsert:
            nums[j + 1] = nums[j]  # 移动元素
            j = j - 1

        nums[j + 1] = itemToInsert


nums = [4, 5, 6, 1, 2, 3]
insertionSort(nums)
print(nums)
