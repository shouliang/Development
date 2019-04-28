# coding=utf-8
''' 该方法的基本思想是：
1．先从数列中取出一个数作为基准数。
2．分区过程，将比这个数大的数全放到它的右边，小于或等于它的数全放到它的左边。
3．再对左右区间重复第二步，直到各区间只有一个数。
'''


def quickSort(nums):
    if not nums:
        return []
    helper(nums, 0, len(nums)-1)


def helper(nums, low, high):
    if low >= high:                     # 亦可写成 low < high 的条件下，对low到high之间的元素进行排序
        return
    # 获取分区点
    pivot = partition(nums, low, high)

    # 获取分区点后，递归调用分区点的前后半部分
    helper(nums, low, pivot - 1)
    helper(nums, pivot + 1, high)


# 分区点获取函数：分区点的左边都小于分区点所在位置的值，分区点右边都大于分区点所在位置的值，另这只是其中一趟排序情况
def partition(nums, low, high):
    # 通常选择最后一个位置high作为临时分区点，当然也可以选择中间位置，然后再与最后一个位置交换亦可
    pivot_value = nums[high]
    i = low

    # 遍历low至high-1,将小于分区点的值，放在合适的位置i上，i从low开始，每次交换后，i自增1，代表下一个可能交换的位置
    # 遍历完毕后，将high与正确的分区点交换，达到分区点左边都比其小，右边都比其大的目的
    for j in range(low, high):
        if nums[j] < pivot_value:
            swap(nums, i, j)
            i += 1  # 交换i,j后自增1，代表下一个可能交换的位置

    # 将分区点放到最后正确的位置上
    swap(nums, i, high)
    return i


# 交换数组中两个下标对应的元素
def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]


nums = [3, 7, 8, 5, 2, 1, 9, 5, 4]
quickSort(nums)
print(nums)

# nums = [3, 7, 8, 5, 2, 1, 9, 6, 4]
# quickSort(nums)
# print(nums)

# nums = [3, 7, 8, 5, 2, 1, 6, 4]
# quickSort(nums)
# print(nums)
