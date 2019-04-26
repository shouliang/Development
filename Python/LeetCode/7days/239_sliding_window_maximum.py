''' 
窗口的最左边保持最大值
239. Sliding Window Maximum:https://leetcode.com/problems/sliding-window-maximum/
思路：利用双端队列
'''


class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        window, res = [], []

        for i, value in enumerate(nums):
            if i >= k and i - window[0] >= k:
                window.pop(0)
            while window and nums[window[-1]] <= value:
                window.pop()

            window.append(i)

            if i >= k - 1:
                res.append(nums[window[0]])
        return res


s = Solution()
res = s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
print(res)
