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

思路1：动态规划:O(n^2)
    首先想到用动态规划解决该问题，维护数组 dp , dp[i] 表示以第i个元素为结尾的增长序列的长度，
    则递归式为：dp[i]= max(dp[i], dp[j] + 1) 其中 j 0..i-1 && nums[i] > nums[j]

思路2：Θ(nlgn)的方案，二分查找
    建立一个辅助数组tails，依次读取数组元素 x 与数组末尾元素 top比较：
    如果 x > top，将 x 放到数组末尾；
    如果 x < top，则二分查找数组中第一个 大于等于x 的数，并用 x 替换它。
'''


class Solution(object):
    def _lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 1
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            result = max(result, dp[i])
        return result

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tails = []
        for x in nums:
            if len(tails) == 0 or tails[-1] < x:
                tails.append(x)
            else:
                low, high = 0, len(tails) - 1
                while low <= high:
                    mid = (low + high) // 2
                    if tails[mid] >= x:
                        high = mid - 1
                    else:
                        low = mid + 1
                tails[low] = x       # 找的是第一个大于等于目标的数，又数组是升序的，即从小到大，故取low
        return len(tails)


s = Solution()
nums = [10, 9, 2, 5, 3, 7, 101, 18]
lenLIS = s.lengthOfLIS(nums)
print(lenLIS)

lenLIS = s._lengthOfLIS(nums)
print(lenLIS)
