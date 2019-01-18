import heapq


def twoSum(nums, target):
    hash_map = {}
    for i, value in enumerate(nums):
        if target - value in hash_map:
            return hash_map[target - value], i
        hash_map[value] = i


nums, target = [8, 9, 14, 6, 20], 15
twoIndex = twoSum(nums, target)
print(twoIndex)


class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.nums = nums
        self.topNums = [] * k
        for num in nums:  # 初始化调用自身的add方法来模拟实现向数据流中一个一个添加数字
            self.add(num)

    def add(self, val):
        if len(self.nums) < self.k:
            heapq.heappop(self.nums, val)
        elif self.nums[0] < val:
            heapq.heappushpop(self.nums, val)

        return self.nums[0]


class KthLargest_01:
    def __init__(self, k, nums):
        self.k = k
        self.nums = nums
        self.topNums = [] * k
        for num in nums:
            self.add(num)

    def add(self, val):
        if len(self.topNums) < self.k:
            heapq.heappush(self.topNums, val)
        elif self.topNums[0] < val:
            heapq.heappushpop(self.topNums, val)

        return self.topNums[0]


def quick_sort(alist):
    qucik_sort_helper(alist, 0, len(alist) - 1)


def qucik_sort_helper(alist, low, high):
    print(low,high)
    if low >= high:
        return
    pivot = partition(alist, low, high)
    qucik_sort_helper(alist, low, pivot-1)
    qucik_sort_helper(alist, pivot+1, high)


def partition(alist, low, high):
    pivot_value = alist[high]
    i = low
    for j in range(low, high):
        if alist[j] < pivot_value:
            swap(alist, i, j)
            i += 1
    swap(alist, i, high)
    return i


def swap(alist, i, j):
    alist[i], alist[j] = alist[j], alist[i]


alist = [5, 4, 8, 7, 1, 2, 9]
quick_sort(alist)
print('after quick_sort')
print(alist)


def merge_sort(alist):
    merge_sort_helper(alist, 0, len(alist) - 1)


def merge_sort_helper(alist, low, high):
    if low >= high:
        return
    mid = low + (high - low) // 2
    merge_sort_helper(alist, low, mid)
    merge_sort_helper(alist, mid+1, high)
    merge(alist, low, mid, high)


def merge(alist, low, mid, high):
    i, j = low, mid+1
    temp = []
    while i <= mid and j <= high:
        if alist[i] <= alist[j]:
            temp.append(alist[i])
            i += 1
        else:
            temp.append(alist[j])
            j += 1
    start, end = i, mid
    if j <= high:
        start, end = j, high
    while start <= end:
        temp.append(alist[start])
        start += 1
    alist[low:high+1] = temp

alist = [5, 4, 8, 7, 1, 2, 9]
merge_sort(alist)
print('after merge_sort')
print(alist)