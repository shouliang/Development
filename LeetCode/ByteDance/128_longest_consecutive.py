''' 
128. Longest Consecutive Sequence:https://leetcode.com/problems/longest-consecutive-sequence/
'''


class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_len, cur_len = 1, 1
        hash_map = {}
        # 遍历列表将num放入hash表
        for i in range(len(nums)):
            hash_map[nums[i]] = True

        # 遍历列表，对每个元素判断其向上和向下相邻的是否在hash表中，在则cur_len自增1
        for i in range(len(nums)):
            temp = nums[i] + 1
            while temp in hash_map:
                cur_len = cur_len + 1
                temp = temp + 1

            temp = nums[i] - 1
            while temp in hash_map:
                cur_len = cur_len + 1
                temp = temp - 1
            if max_len < cur_len:
                max_len = cur_len
            cur_len = 1

        return max_len


s = Solution()
nums = [100, 4, 200, 1, 3, 2]
max_len = s.longestConsecutive(nums)
print(max_len)
