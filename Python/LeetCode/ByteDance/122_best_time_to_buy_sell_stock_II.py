''' 
买卖股票的最佳时机(最大利润)：可以交易多次
122. Best Time to Buy and Sell Stock II:https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
解释：
    给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
    设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
    注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
思路：
    贪心法：既然能买卖任意次，那最大收益的方法就是尽可能多的低入高抛。只要明天比今天价格高，就应该今天买入明天再卖出。
'''


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                # 贪心算法：只要明天比今天价格高，就应该今天买入明天再卖出。
                maxProfit += prices[i] - prices[i - 1]
        return maxProfit


prices = [7, 1, 5, 3, 6, 4]
s = Solution()
mp = s.maxProfit(prices)
print(mp)


# 动态规划的解法
# dp[i][0]，dp[i][1]代表 the i day, have or not stock，即第i天是否拥有股票哟，0代表没有，1代表当天持有股票。
# dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
# #即第i天没股票的最大收益，dp[i-1][0]代表前一天没有股票，dp[i-1][1]+prices[i]前一天有股票并卖出，而第i天的最大收益会是这两者之间的最大值。
# dp[i][1] = max(dp[i - 1][0] - prices[i], dp[i - 1][1])
# #即第i天持有股票时的最大收益，dp[i-1][0]-prices[i]代表前一天没有股票并买入，dp[i-1][1]表示前一天持有股票的最大收益
class Solution2:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0      # 错误处理
        dp = [[0, 0]] * len(prices)  # 初始化
        dp[0][0] = 0                 # 第0天没有股票，收益为0
        dp[0][1] = -prices[0]        # 第0天有股票，  收益为负数
        for i in range(1, len(prices)):
            # 第i天没有股票：取（第i-1天也没有股票） 和 （第i-1天有股票并卖出的收益之和，因为卖出故收益需要加上当天股票价格）的最大值
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            # 第i天有股票 : 取（第i-1天也有股票）   和 （第i-1天没有股票并买入的收益之和，因为买入故收益需要减去当天股票价格）的最大值
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + (-prices[i]))

        return dp[len(prices) - 1][0]  # 返回最后一天没有股票的情况


prices = [7, 1, 5, 3, 6, 4]
s = Solution2()
mp = s.maxProfit(prices)
print(mp)
