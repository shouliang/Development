# coding=utf-8
# 从未排序部分选择第1个位置，插入到已排序部分的合适位置，初始化时已排序的部分就是第0个元素，故未排序的从第1个位置开始
def insertionSort(nums):
    n = len(nums)
    for i in range(1, n):     # i从1开始，因为是从未排序的向已排序的部分插入，开始已排序的位数组第一个元素, 另range函数的右边是开区间的
        itemToInsert = nums[i]

        # 从 i - 1 到 0 找一个位置插入，同时移动元素，找出合适的插入位置，插入的位置为 j + 1
        j = i - 1

        # 循环直到找到比itemToInsert要小的元素，并移动元素，从而空出位置
        while j >= 0 and nums[j] > itemToInsert:
            nums[j + 1] = nums[j]  # 移动元素 j 覆盖了 j + 1 ,故空出了j的位置
            j = j - 1              # 而后 j = j - 1 ,故空出的位置此时变成了 j + 1 

        nums[j + 1] = itemToInsert


nums = [4, 5, 6, 1, 2, 3]
insertionSort(nums)
print(nums)
