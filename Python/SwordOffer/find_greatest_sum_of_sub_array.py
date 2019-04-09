# -*- coding:utf-8 -*-
import sys


class Solution:
    def FindGreatestSumOfSubArray(self, array):
        greatestSum = -sys.maxsize - 1  # 设置为python中的最小值，针对数组和都是负数的情况
        curSum = 0
        for value in array:
            if curSum <= 0:  # 当前和小于0，则从当前元素重新计算当前和
                curSum = value
            else:
                curSum += value
            if curSum > greatestSum:
                greatestSum = curSum

        return greatestSum


array = [1, -2, 3, 10, -4, 7, 2, -5]
# array = [-2, -8, -1, -5, -9]
s = Solution()
gsum = s.FindGreatestSumOfSubArray(array)
print(gsum)
