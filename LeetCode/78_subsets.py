''' 
子集合
78. Subsets:https://leetcode.com/problems/subsets/
'''


def subsets(nums):
    if not nums:
        return None
    subset, results = [], []
    dfs(nums, 0, subset, results)
    return results


def dfs(nums, start, subset, results):
    results.append(subset[:])
    for i in range(start, len(nums)):
        subset.append(nums[i])
        dfs(nums, i + 1, subset, results)
        subset.pop()


nums = [1, 2, 3, 4, 5]
res = subsets(nums)
print(res)
