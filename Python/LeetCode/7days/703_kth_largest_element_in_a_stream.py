'''
返回数据流中第K大元素  
703. Kth Largest Element in a Stream: https://leetcode.com/problems/kth-largest-element-in-a-stream/
'''
import heapq  # 引入堆栈

class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        self.nums = nums
        self.topNums = []
        for num in nums:
            self.add(num)

    def add(self, val):
        if len(self.topNums) < self.k :
            heapq.heappush(self.topNums,val)  # heaq. heappush
        elif self.topNums[0] < val:
            heapq.heappushpop(self.topNums,val)  # heapq.  heappushpop
        return self.topNums[0]


# Your KthLargest object will be instantiated and called as such:
k = 2
nums = [4, 5, 8, 2]
obj = KthLargest(k, nums)
print(obj.add(3))
obj.add(5)
obj.add(10)
obj.add(9)
obj.add(4)
