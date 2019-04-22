''' 
两数之和
解释：
    求数组中的俩数之和为指定目标数值的下标
思路：遍历数组将其值存储在哈希表中，
    遍历过程中判断target - value是否在其中，在则返回下标，不在返回None
''' 
class Solution:
    def twoSum(self,nums,target):
        hash_map = dict()
        for i,value in enumerate(nums):
            if target - value in hash_map:
                return [hash_map[target - value], i] # 返回的是下标
            hash_map[value] = i


nums = [2, 7, 11, 15]
target = 9
solution = Solution()
print(solution.twoSum(nums, target))