'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
注意你不能在买入股票前卖出股票。

思路：
只需要遍历一次数组，用一个变量记录遍历过数中的最小值，然后每次计算当前值和这个最小值之间的差值最为利润，
然后每次选较大的利润来更新。当遍历完成后当前利润即为所求
'''


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        minPrice = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            minPrice = min(minPrice, prices[i])               # 求i前面的最小值
            maxProfit = max(maxProfit, prices[i] - minPrice)  # 求i前面的最大差值即利润
        return maxProfit


prices = [7, 1, 5, 3, 6, 4]
s = Solution()
maxP = s.maxProfit(prices)
print(maxP)
