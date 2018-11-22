# 求数组中的俩数之和为指定目标数值的下标
# 思路：遍历数组将其值存储在哈希表中，
# 遍历过程中判断target - x是否在其中，在则返回下标，不在返回None

class Solution:
    def twoSum(self, nums, target):
        hash_map = dict()
        for i, x in enumerate(nums):
            if target - x in hash_map:
                return [hash_map[target - x], i]
            hash_map[x] = i  # key为数值，value为下标


# test
nums = [2, 7, 11, 15]
target = 18
solution = Solution()
print(solution.twoSum(nums, target))
