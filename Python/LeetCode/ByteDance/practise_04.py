class Solution:
    def validUtf8(self, data):
        count = 0
        for dt in data:
            if count == 0:
                if (dt >> 5) == 0b110:
                    count = 1
                elif (dt >> 4) == 0b1110:
                    count = 2
                elif (dt >> 3) == 0b11110:
                    count = 3
                elif (dt >> 7 != 0):
                    return False
            else:
                if (dt >> 6) != 0b10:
                    return False
                else:
                    count -= 1
        return count == 0

    def validUtf8_01(self, data):
        count = 0
        for dt in data:
            if count == 0:
                if (dt >> 5 == 0b110):
                    count = 1
                elif (dt >> 4 == 0b1110):
                    count = 2
                elif (dt >> 3 == 0b11110):
                    count = 3
                elif (dt >> 7 != 0):
                    return False
            else:
                if (dt >> 6 != 0b10):
                    return False
                else:
                    count -= 1

    def validUtf8_02(self, data):
        count = 0
        for dt in data:
            if (count == 0):
                if (dt >> 5 == 0b110):
                    count = 1
                elif(dt >> 4 == 0b1110):
                    count = 2
                elif (dt >> 3 == 0b11110):
                    count = 3
                elif (dt >> 7 != 0):
                    return False
            else:
                if (dt >> 6 != 0b10):
                    return False
                else:
                    count -= 1
        return count == 0

        def maxProfit(self, prices):
            if not prices:
                return 0
            minPrice = prices[0]
            maxProfit = 0
            for i in range(1, len(prices)):
                minPrice = min(minPrice, prices[i])
                maxProfit = max(maxProfit, prices[i] - minPrice)
            return maxProfit

        def maxProfit_01(self, prices):
            if not prices:
                return 0
            minPrice, maxProfit = prices[0], 0
            for i in range(1, len(prices)):
                minPrice = min(minPrice, prices[i])
                maxProfit = max(maxProfit, prices[i] - minPrice)
            return maxProfit

        def maxProfit_02(self, prices):
            if not prices:
                return 0
            minPrice, maxProfit = prices[0], 0
            for i in range(1, len(prices)):
                minPrice = min(minPrice, prices[i])
                maxProfit = max(maxProfit, prices[i] - minPrice)
        return maxProfit

        def maxProfit_multi(self, prices):
            if not prices:
                return 0
            dp = [[0, 0]] * len(prices)
            dp[0][0] = 0
            dp[0][1] = -prices[0]
            for i in range(1, len(prices)):
                dp[i][0] = max(dp[i - 1][0], dp[i-1][1] + prices[i])
                dp[i][1] = max(dp[i - 1][1], dp[i-1][0] + (-prices[i]))
            return dp[len(prices) - 1][0]

        def maxProfit_multi_01(self, prices):
            if not prices:
                return 0
            dp = [[0, 0]] * len(prices)
            dp[0][0] = 0
            dp[0][1] = -prices[0]
            for i in range(1, len(prices)):
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            return dp[len(prices) - 1][0]

        def maxProfit_multi_02(self, prices):
            if not prices:
                return 0
            dp = [[0, 0]] * len(prices)
            dp[0][0] = 0
            dp[0][1] = -prices[0]
            for i in range(1, len(prices)):
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            return dp[len(prices) - 1][0]

        def mySqrt(self, x):
            if x == 0 or x == 1:
                return x
            result = 0
            low, high = 1, x
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

        def mySqrt_01(self, x):
            if x == 0 or x == 1:
                return x
            result = 0
            low, high = 1, x
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

        def mySqrt_02(self, x):
            if x == 0 or x == 1:
                return x
            result = 0
            low, high = 1, x
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
