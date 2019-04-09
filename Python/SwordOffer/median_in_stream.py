'''
数据流中的中位数
题目描述
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。

思路：利用大顶堆和小顶堆，大顶堆里面的所有元素要小于小顶堆里面的元素
    当大顶堆和小顶堆的数目为偶数，插入大顶堆，这时候总的数目为奇数，中位数就是大顶堆的堆顶元素
        插入：比较和调整
             比较:新的num比大顶堆堆顶元素小，则直接插入
                        比大顶堆顶元素大，若比小顶堆堆顶元素小，则直接插入大顶堆
                                       若比小顶堆堆顶元素大，则小顶堆堆顶元素弹出压入大顶堆，而后将num压入小顶堆，从而保证大顶堆一直小于小顶堆
    当大顶堆和小顶堆的数目为奇数，插入小顶堆，这时候总的数目为偶数，中位数就是大顶堆的堆顶元素和小顶堆的堆顶元素的平均值

'''

import heapq
class Solution:
    def __init__(self):
        self.maxheap = Maxheap()
        self.minHeapArray = []

    def Insert(self, num):
        if (self.maxheap.len() + len(self.minHeapArray)) & 1 == 0:
            if self.maxheap.len() == 0 or num <= self.maxheap.gettop():
                self.maxheap.heappush(num)
            if num > self.maxheap.gettop():
                if num <= self.minHeapArray[0]:
                    self.maxheap.heappush(num)
                else:
                    minTop = heapq.heappop(self.minHeapArray)
                    self.maxheap.heappush(minTop)
                    heapq.heappush(self.minHeapArray, num)
        else:
            if len(self.minHeapArray) == 0 or num >= self.minHeapArray[0]:
                heapq.heappush(self.minHeapArray, num)
            if num < self.minHeapArray[0]:
                if num >= self.maxheap.gettop():
                    heapq.heappush(self.minHeapArray, num)
                else:
                    maxTop = self.maxheap.heappop()
                    heapq.heappush(self.minHeapArray, maxTop)
                    self.maxheap.heappush(num)

    def GetMedian(self):
        median = 0
        if (len(self.minHeapArray) + self.maxheap.len()) & 1 == 1:
            median = self.maxheap.gettop()
        else:
            median = (self.minHeapArray[0] + self.maxheap.gettop()) / 2.0
        return median


'''
python默认的heapq模块只支持最小堆的构建。
python的heapq不支持大根堆，在stackoverflow上看到了一个巧妙的实现：
我们还是用小根堆来进行逻辑操作，在做push的时候，我们把最大数的相反数存进去，
那么它的相反数就是最小数，仍然是堆顶元素，在访问堆顶的时候，再对它取反，就获取到了最大数
'''
# 自定义的大顶堆
class Maxheap:
    def __init__(self):
        self.arr = list()

    def len(self):
        return len(self.arr)

    def heappush(self, val):
        heapq.heappush(self.arr, -val)

    def heapify(self):
        heapq.heapify(self.arr)

    def heappop(self):
        return -heapq.heappop(self.arr)

    def gettop(self):
        if not self.arr:
            return
        return -self.arr[0]


s = Solution()
s.Insert(3)
print(s.GetMedian())

s.Insert(8)
print(s.GetMedian())

s.Insert(6)
s.Insert(4)
s.Insert(1)
print(s.GetMedian())
