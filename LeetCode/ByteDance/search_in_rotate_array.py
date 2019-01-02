'''
leetCode33. 搜索旋转排序数组
思路：二分查找，主要是确定单调递增的那一段区间
'''


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # mid左端是排好序的
            if nums[mid] >= nums[left]:
                # 因为前面第11行的判断已经说明A[mid] != target了，所以不再考虑A[mid] = target的情况
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # 下面的else等同于elif A[mid] <= A[right]
            else:
                if nums[mid] < target and nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


# nums = [4, 5, 6, 7, 0, 1, 2]
# target = 3

nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

nums = [3, 1]
target = 1

s = Solution()
posotion = s.search(nums, target)
print(posotion)
