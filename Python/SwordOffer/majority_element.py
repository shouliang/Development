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
            left = self.find(nums, begin, mid)
            right = self.find(nums, mid + 1, end)

            if left == right:
                return left
            else:
                countleft, countright = 0, 0
                for i in range(begin, end):
                    if nums[i] == left:
                        countleft += 1
                    elif nums[i] == right:
                        countright += 1
                if countleft >= countright:
                    return left
                else:
                    return right


nums = [6, 5, 5]
s = Solution()
ma = s.majorityElement(nums)
print(ma)
