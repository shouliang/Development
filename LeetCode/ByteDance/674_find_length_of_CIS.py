'''
最长连续递增序列
674. Longest Continuous Increasing Subsequence:https://leetcode.com/problems/longest-continuous-increasing-subsequence/
'''


class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_len, cur_len = 1, 1
        # 遍历数组：若nums[i] < nums[i+1],累积当前长度,并记录最大值长度，否则当前长度重新归1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i+1]:
                cur_len = cur_len + 1
                if max_len < cur_len:
                    max_len = cur_len
            else:
                cur_len = 1
        return max_len


s = Solution()
nums = [1, 3, 5, 4, 7]
max_len = s.findLengthOfLCIS(nums)
print(max_len)

# nums = [2, 2, 2, 2, 2]
# max_len = s.findLengthOfLCIS(nums)
# print(max_len)
