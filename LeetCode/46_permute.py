'''
全排列
46. Permutations:https://leetcode.com/problems/permutations/
解释：
    Given a collection of distinct integers, return all possible permutations.

    Example:

    Input: [1,2,3]
    Output:
    [
    [1,2,3],
    [1,3,2],
    [2,1,3],
    [2,3,1],
    [3,1,2],
    [3,2,1]
    ]

思路： 深度遍历+回溯

'''


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        path, result = [], []
        visited = set()

        def dfs(nums, visited, start, path, result):
            if start == len(nums):      # 递归终止条件
                result.append(path[:])

            for i in range(len(nums)):
                if nums[i] not in visited:
                    visited.add(nums[i])
                    path.append(nums[i])
                    # 深度遍历，每遍历一次，将未访问的nums[i]加入path,直到start == len(nums)
                    dfs(nums, visited, start + 1, path, result)
                    visited.remove(nums[i])
                    path.pop()           # 回溯:弹出队尾元素

        dfs(nums, visited, 0, path, result)
        return result


class Solution2:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        path, result = [], []
        visited = set()

        def dfs(nums, visited, path, result):
            if len(path) == len(nums):    # 递归终止条件
                result.append(path[:])

            for i in range(len(nums)):
                if nums[i] not in visited:
                    visited.add(nums[i])
                    path.append(nums[i])
                    # 深度遍历，每遍历一次，将未访问的nums[i]加入path,直到len(path) == len(nums)
                    dfs(nums, visited, path, result)
                    visited.remove(nums[i])
                    path.pop()             # 回溯,弹出队尾元素

        dfs(nums, visited, path, result)
        return result


s = Solution()
nums = [1, 2, 3]
ret = s.permute(nums)
print(ret)

s = Solution2()
ret = s.permute(nums)
print(ret)
