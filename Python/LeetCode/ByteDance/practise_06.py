import heapq


class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        minPrice = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            minPrice = min(prices, prices[i])
            maxProfit = max(maxProfit, prices[i] - minPrice)
        return maxProfit

    def maxProfit_m(self, prices):
        if not prices:
            return 0
        dp = [[0, 0]] * len(prices)
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + (-prices[i]))
        return dp[len(prices) - 1][0]

    def mySqrt(self, x):
        if x == 0 or x == 1:
            return x
        low, high = 1, x
        result = 0
        while low <= high:
            mid = low + ((high - low) >> 1)
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                high = mid - 1
            else:
                low = mid + 1
                result = mid
        return result

    def validUtf8(self, data):
        count = 0
        for dt in data:
            if count == 0:
                if dt >> 5 == 0b110:
                    count = 1
                elif dt >> 4 == 0b1110:
                    count = 2
                elif dt >> 3 == 0b11110:
                    count = 3
                elif dt >> 7 != 0:
                    return False
            else:
                if dt >> 6 != 0b10:
                    return False
                else:
                    count -= 1
        return count == 0


class MinStack:
    def __init__(self):
        self.stack_data = []
        self.heap = []

    def push(self, x):
        self.stack_data.append(x)
        heapq.heappush(self.heap, x)

    def pop(self):
        if len(self.stack_data):
            data = self.stack_data.pop()
            if len(self.heap) and data == self.heap[0]:
                heapq.heappop(self.heap)

    def top(self):
        if len(self.stack_data):
            return self.stack_data[-1]

    def getMin(self):
        if len(self.heap):
            return self.heap[0]

import collections
class LRUCache:
    def __init__(self,capacity):
        self.dict = collections.OrderedDict()
        self.remain = capacity
    
    def get(self,key):
        if key not in self.dict:
            return -1
        value = self.dict.pop(key)
        self.dict[key] = value
        return value
    
    def set(self,key,value):
        if key in self.dict:
            self.dict.pop(key)
        else:
            if self.remain > 0:
                self.remain -=1
            else:
                self.dict.popitem(last=False)

        self.dict[key] = value