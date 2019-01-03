import math


# 求平方根，只返回整数部分
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1: return x    # 处理特殊情况
        left, right, result = 1, x, 0    # 套用二分模板
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid == x:
                return mid
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
                result = mid            # left= mid + 1 再平方后会超过x,为了取整故取result = mid
        return result


x = 4
x = 26
s = Solution()
sqrt = s.mySqrt(x)
print(sqrt)
