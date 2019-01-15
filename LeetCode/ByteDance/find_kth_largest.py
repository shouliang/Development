''' 
数组中的第K个最大元素
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:
你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
''' 
import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        top_nums = []
        for i in range(len(nums)):            # 遍历list
            if len(top_nums) < k:             # 数量未到k个，直接插入小顶堆，Python会自动维护     
                heapq.heappush(top_nums, nums[i])
            elif top_nums[0] < nums[i]:       # 小顶堆已满，若栈顶小于nums[i]，则更新小顶堆
                heapq.heappushpop(top_nums, nums[i])
        return top_nums[0] # 最后返回小顶堆堆顶，即为第k个大小的元素


s = Solution()

nums, k = [3, 2, 1, 5, 6, 4], 2
kth = s.findKthLargest(nums, k)
print(kth)

nums, k = [3, 2, 3, 1, 2, 4, 5, 5, 6], 4
kth = s.findKthLargest(nums, k)
print(kth)
