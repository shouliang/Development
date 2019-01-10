'''
最大子序和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

思路1： 动态规划
设sum[i]为以第i个元素结尾且和最大的连续子数组。假设对于元素i，所有以它前面的元素结尾的子数组的长度都已经求得，
那么以第i个元素结尾且和最大的连续子数组实际上，要么是以第i-1个元素结尾且和最大的连续子数组加上这个元素，要么是只包含第i个元素，
即sum[i] = max(sum[i-1] + a[i], a[i])。可以通过判断sum[i-1] + a[i]是否大于a[i]来做选择，而这实际上等价于判断sum[i-1]是否大于0。
由于每次运算只需要前一次的结果，因此并不需要像普通的动态规划那样保留之前所有的计算结果，只需要保留上一次的即可，因此算法的时间和空间复杂度都很小

当我们加上一个正数时，和会增加；当我们加上一个负数时，和会减少。
如果当前得到的和是个负数，那么这个和在接下来的累加中应该抛弃并重新清零，不然的话这个负数将会减少接下来的和。
'''


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum, sub_sum = 0, 0
        if len(nums):
            max_sum = nums[0]
        for i in range(len(nums)):
            sub_sum = sub_sum + nums[i]
            max_sum = max(max_sum, sub_sum)
            if sub_sum < 0:  # 累积和为负数，则抛弃并归零，否则负数会减少接下来的和
                sub_sum = 0
        return max_sum


class Solution2:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * len(nums)  # 动态规划
        dp[0] = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            dp[i] = nums[i] + (dp[i-1] if dp[i-1] > 0 else 0)  # 动态规划递推公式
            max_sum = max(max_sum, dp[i])

        return max_sum    

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums = [-2, -1]
nums = [1, 2]
s = Solution()
maxsum = s.maxSubArray(nums)
print(maxsum)

s2 = Solution2()
maxsum = s2.maxSubArray(nums)
print(maxsum)
