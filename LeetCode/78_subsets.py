''' 
子集合
78. Subsets:https://leetcode.com/problems/subsets/
'''


def subsets(nums):
    if not nums:
        return None
    subset, result = [], []
    dfs(nums, 0, subset, result)
    return result


def dfs(nums, start, path, result):
    result.append(path[:])
    for i in range(start, len(nums)):
        path.append(nums[i])
        dfs(nums, i + 1, path, result)
        path.pop()


nums = [1, 2, 3, 4, 5]
res = subsets(nums)
print(res)
