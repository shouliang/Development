def twoSum(nums, target):
    hash_map = {}
    for i, value in enumerate(nums):
        if target - value in hash_map:
            return hash_map[target - value], i
        hash_map[value] = i


nums, target = [8, 9, 14, 6, 20], 15
twoIndex = twoSum(nums, target)
print(twoIndex)

import heapq


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
    def __init__(self,k,nums):
        self.k = k
        self.nums = nums
        self.topNums = [] * k
        for num in nums:
            self.add(num)

    def add(self,val):
        if len(self.topNums) < self.k:
            heapq.heappush(self.topNums, val)
        elif self.topNums[0] < val:
            heapq.heappushpop(self.topNums,val)

        return self.topNums[0]
