class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                if target > nums[left]:
                    right = mid
                elif target < nums[left]:
                    if target < nums[right]:
                        left = mid
                    else:
                        return -1
            else:
                left = mid
        return -1


# nums = [4, 5, 6, 7, 0, 1, 2]
# target = 3

nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

nums = [1]
target = 0

s = Solution()
posotion = s.search(nums, target)
print(posotion)
