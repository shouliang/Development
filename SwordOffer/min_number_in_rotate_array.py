# coding=utf-8

# 旋转数组的最小数字： 如：1，2，3, 4, 5 旋转为3，4，5，1，2
class Solution:
    def findMin(self, nums):
        if not nums:
            return 0

        start = 0
        end = len(nums) - 1
        middle = start
        while nums[start] >= nums[end]:
            if end - start == 1:
                middle = end
                break

            middle = start + ((end - start) >> 1)

            if nums[middle] >= nums[start]:
                start = middle
            elif nums[middle] <= nums[start]:
                end = middle

        return nums[middle]


s = Solution()

num = s.findMin([3, 4, 5, 1, 2])
print(num)

# num = s.findMin([4, 5, 2, 3])
# print(num)
