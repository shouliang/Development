import heapq
# 返回数据流中第K大元素
class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        self.nums = nums
        self.topNums = [] 
        for num in nums:
            self.add(num)

    def add(self, val):
        # 维护一个k个元素的小顶堆
        # Python中小顶堆的第一个元素就是小顶堆的最小值
        # 每次add新元素num时，只有当 num > 小顶堆堆顶值的，将其插入小顶堆
        # Python中heapq会自动维护，使小顶堆最小值在堆顶
        if len(self.topNums) < self.k:
            heapq.heappush(self.topNums, val)
        elif self.topNums[0] < val:
            heapq.heappushpop(self.topNums, val)

        return self.topNums[0]


# Your KthLargest object will be instantiated and called as such:
k = 2
nums = [4, 5, 8, 2]
obj = KthLargest(k, nums)
obj.add(3)
obj.add(5)
obj.add(10)
obj.add(9)
obj.add(4)
