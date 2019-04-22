''' 
求众数: 数组中超过一半的数
169. Majority Element:https://leetcode.com/problems/majority-element/
解法一
思路
这题其实可以理解为一个配对问题，即将占大多数的那个元素和剩下的元素两两配对，占大多数的元素总是有剩下的
'''
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority,count = None,0
        
        for num in nums:
            if count ==0 :
                majority = num
            if num == majority:
                count +=1
            else:
                count -=1
        return majority


# test
nums = [3,2,3]
s = Solution()
majority = s.majorityElement(nums)
print(majority)