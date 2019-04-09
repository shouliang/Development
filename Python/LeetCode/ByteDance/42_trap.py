'''
接雨水
42. Trapping Rain Water:https://leetcode.com/problems/trapping-rain-water/
解释:
    给定n 个非负整数表示每个宽度为 1的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

思路:
    这道题对每一个柱子需要考虑它左右两侧的高度，从而确定这个柱子处能接多少雨水。有三种解法

    方法一
    从两端往中间逼近，记录左右两端高度最高值，那么对于这两端最高值中间部分，如果高度低于两端最高值，
    能接的雨水取决于两端最高值中的最小值。
'''


class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        areas = 0
        left_max, right_max = 0, 0
        while left < right:                            # 两端向中间逼近
            left_max = max(left_max, height[left])     # 左端最大值
            right_max = max(right_max, height[right])  # 右端最大值
            if left_max < right_max:                   # 但是雨水量取决于两端的最高值中的较小值于自身的差值
                areas += left_max - height[left]
                left = left + 1
            else:
                areas += right_max - height[right]
                right = right - 1
        return areas


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
s = Solution()
area = s.trap(height)
print(area)
