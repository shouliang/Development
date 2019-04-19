class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.find(nums, 0, len(nums) - 1)

    def find(self, nums, begin, end):
        if begin == end:
            return nums[begin]
        else:
            mid = begin + ((end - begin) >> 1)
            leftMajority = self.find(nums, begin, mid)
            rightMajority = self.find(nums, mid + 1, end)

            if leftMajority == rightMajority:
                return leftMajority
            else:
                leftCount, rightCount = 0, 0
                for i in range(begin, end):
                    if nums[i] == leftMajority:
                        leftCount += 1
                    elif nums[i] == rightMajority:
                        rightCount += 1
                if leftCount >= rightCount:
                    return leftMajority
                else:
                    return rightMajority


nums = [6, 5, 5]
s = Solution()
ma = s.majorityElement(nums)
print(ma)
