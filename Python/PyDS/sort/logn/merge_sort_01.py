# 归并排序：先分解再合并
def mergeSort(nums):
    if not nums:
        return []
    helper(nums, 0, len(nums) - 1)


def helper(nums, low, high):
    # 一般写法的递归终止条件，实际上当low == high，递归即终止
    # if low>=high: return
    if low == high:  # 递归终止条件,low == high,表明指向同一个元素，一个元素本身就是有序的，递归结束，而后开始进行合并
        return

    # 将原数组分成两半
    mid = low + ((high - low) >> 1)

    # 分别进行递归调用
    helper(nums, low, mid)      # 递归调用直到递归终止条件为止，其间会产生一个调用的函数栈，后调用的先返回
    # 为什么递归会产生调用的函数栈尼，就像多个普通函数一层一层嵌套调用，调用到最后一层再逐步返回
    helper(nums, mid + 1, high)

    # 合并数组
    merge(nums, low, mid, high)


# 合并两个已经排序的数组到一个数组，仍使其有序
# 通过low,mid,high可以将原数组分成两个有序的数组，然后循环比较，将较小的插入临时数组，最后再复制到原数组，达到使原数组有序的目的
def merge(nums, low, mid, high):
    i, j = low, mid + 1
    temp = []

    while i <= mid and j <= high:   # 因为都是实际的数组下下标，故循环条件均为小于等于
        if nums[i] <= nums[j]:
            temp.append(nums[i])
            i += 1
        else:
            temp.append(nums[j])
            j += 1

    # 将剩余的全部存入临时数组
    while i <= mid:
        temp.append(nums[i])
        i += 1
    while j <= high:
        temp.append(nums[j])
        j += 1

    # 将剩余的全部存入临时数组的另外一种写法
    # start, end = i, mid
    # if j <= high:
    #     start, end = j, high
    # while start <= end:
    #     temp.append(nums[start])
    #     start += 1

    # 临时数组的数据赋值到原数组, 切片a[l:r]为a[l] 到 a[r - 1]
    nums[low:high + 1] = temp


# 在原数组上进行排序
nums = [3, 5, 6, 7, 8, 1]
mergeSort(nums)
print(nums)

nums = [3, 5, 6, 7, 8, 1, 2]
mergeSort(nums)
print(nums)
