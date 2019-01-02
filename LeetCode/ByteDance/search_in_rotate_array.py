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
            # mid左端是排好序的
            if nums[mid] >= nums[left]:
                # 因为前面第11行的判断已经说明nums[mid] != target了，所以不再考虑nums[mid] = target的情况
                if nums[mid] > target and nums[left] <= target:
                    right = mid - 1
                else:
                    left = mid + 1
            # 下面的else等同于elif nums[mid] <= nums[right]
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

# nums = [1]
# target = 0

s = Solution()
posotion = s.search(nums, target)
print(posotion)
