'''
最长上升子序列
300. Longest Increasing Subsequence:https://leetcode.com/problems/longest-increasing-subsequence/
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.

思路：
    首先想到用动态规划解决该问题，维护数组 dp , dp[i] 表示以第i个元素为结尾的增长序列的长度，
    则递归式为：dp[i]= Math.max(dp[i], dp[j] + 1) 其中 j < i && nums[j] < nums[i]
'''


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


s = Solution()
nums = [10, 9, 2, 5, 3, 7, 101, 18]
lenLIS = s.lengthOfLIS(nums)
print(lenLIS)
