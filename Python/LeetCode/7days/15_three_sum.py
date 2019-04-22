'''
三数之和
简单版：先排序，固定第1个，找出第2个、第3个，通过双指针的方式，逐渐缩小范围，中间涉及到相邻元素判重的问题等细节
'''
class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort() # 必须要先排序，才能进行双指针
 
        target = 0  
        for i in range(len(nums)-2):
            if i >0 and nums[i] == nums[i-1]:  # 相邻元素相等，跳过当前循环
                continue
            left,right = i +1, len(nums) - 1
            while left < right:
                diff = ( nums[i] + nums[left] + nums[right] ) - target
                if diff < 0:
                    left +=1
                elif diff >0:
                    right -=1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    while left < right and nums[left] == nums[left +1]:
                        left +=1
                    while left < right and nums[right] == nums[right -1]:
                        right -=1
                    # diff == 0时，left大一点，right小一点，还是有可能等于target的
                    left +=1
                    right -=1
        return res



nums = [-1, 0, 1, 2, -1, -4]
s = Solution()
res = s.threeSum(nums)
print(res)

