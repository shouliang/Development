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
            minPrice = min(minPrice, prices[i])
            maxProfit = max(maxProfit, prices[i] - minPrice)
        return maxProfit


prices = [7, 1, 5, 3, 6, 4]
s = Solution()
maxP = s.maxProfit(prices)
print(maxP)
