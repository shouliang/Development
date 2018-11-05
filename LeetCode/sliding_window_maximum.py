# 窗口的最左边保持最大值
class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        # window保存下标，window最左边window[0]是最大值
        # result保存结果
        window, res = [], []
        for i, x in enumerate(nums):
            # 保持滑动的大小k，每次移出队首元素
            if i >= k and i - window[0] >= k:
                window.pop(0)

            # 从队尾移除弹出比当前x要小的元素
            while window and nums[window[-1]] <= x:
                window.pop()

            # 将元素下标压入window
            window.append(i)

            # 当 i >= k + 1才开始写入最大值
            if i >= k - 1:
                res.append(nums[window[0]])
        return res


s = Solution()
res = s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
print(res)
