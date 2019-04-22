''' 
乱序数组中寻找第一个未出现的正整数
41. First Missing Positive:https://leetcode.com/problems/first-missing-positive/
这道题让我们找缺失的首个正数，由于限定了O(n)的时间，所以一般的排序方法都不能用，最开始我没有看到还限制了空间复杂度，
所以想到了用HashSet来解，这个思路很简单，第一遍遍历数组把所有的数都存入HashSet中，并且找出数组的最大值，
下次循环从1开始递增找数字，哪个数字找不到就返回哪个数字，如果一直找到了最大的数字，则返回最大值+1

但是上面的解法不是O(1)的空间复杂度，所以我们需要另想一种解法，既然不能建立新的数组，那么我们只能覆盖原有数组，
我们的思路是把1放在数组第一个位置nums[0]，2放在第二个位置nums[1]，即需要把nums[i]放在nums[nums[i] - 1]上，
那么我们遍历整个数组，如果nums[i] != nums[nums[i] - 1], 而nums[i]为整数且不大于n，
我们将两者位置调换，如果不满足上述条件直接跳过，最后我们再遍历一遍数组，如果对应位置上的数不正确则返回正确的数

参考：
https://www.cnblogs.com/grandyang/p/4395963.html
https://www.cnblogs.com/AnnieKim/archive/2013/04/21/3034631.html

我们的思路是把1放在数组第一个位置nums[0]，2放在第二个位置nums[1]，即需要把nums[i]放在nums[nums[i] - 1]上
'''
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            while (nums[i]>0 and nums[i]<=n) and (nums[i]!=nums[ nums[i] -1]) :
                tmp = nums[i]
                nums[i] = nums[nums[i] -1]
                nums[tmp -1]= tmp        
        
        for i in range(n):
            if nums[i] !=i +1:
                return i +1

        return n + 1

   

nums = [3,4,-1,1]
s = Solution()
firstPositive = s.firstMissingPositive(nums) 
print(firstPositive)


