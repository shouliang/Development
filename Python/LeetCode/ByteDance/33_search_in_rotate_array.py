'''
搜索旋转排序数组
33. Search in Rotated Sorted Array:https://leetcode.com/problems/search-in-rotated-sorted-array/
思路：二分查找，主要是确定单调递增的那一段区间
'''


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums) - 1  # 套用二分查找的模板
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:     # nums[mid]==target则直接返回
                return mid

            # 确定有序区间是在左半区域还是右半区域，nums[mid]>= nums[low]，则有序在左半区域，否则一定在右半区域，因为数组是旋转的
            if nums[mid] >= nums[low]:
                # 若target是在有序区域，则继续在左半部分进行二分查找
                # target < nums[mid]而不是target <= nums[mid]是因为前面已经判断过 nums[mid]== target
                # 若target在有序区域外，则在右半部分，右半部分仍为旋转数组,则继续查询后半部分的旋转数组
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target and nums[high] >= target:  
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

# nums = [4, 5, 6, 7, 0, 1, 2]
# target = 3


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

# nums = [3, 1]
# target = 1

s = Solution()
posotion = s.search(nums, target)
print(posotion)
