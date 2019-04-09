'''
组合总和II
40. Combination Sum II:https://leetcode.com/problems/combination-sum-ii/
解释：
    给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
    candidates 中的每个数字在每个组合中只能使用一次。
思路：
    leetcode39那道题给定数组中的数字可以重复使用，而这道题不能重复使用，只需要在之前的基础上修改两个地方即可，
    首先在递归的for循环里加上if (i > cur && num[ii] == num[i - 1]) continue; 这样可以防止res中出现重复项，
    然后就在递归调用的参数换成i+1，这样就不会重复使用数组中的数字了
'''


class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: L st[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()  # 先排序，方便后来剪枝
        result = []  # 最终解的集合
        path = []  # 其中一个解
        self.DFS(candidates, 0, target, path, result)
        return result

    def DFS(self, candidates, cur, target, path, result):
        if target == 0:
            result.append(path[:])  # 满足条件将其中的一个解加入结果集，此处需要注意Python的语法是解的一个副本
            return
        if target < 0:  # 剪枝
            return

        for i in range(cur, len(candidates)):  # 从这个数的后面即：i + 1 开始进行搜索
            if i > cur and candidates[i] == candidates[i - 1]:
                continue  # 同一层中，后面的数和前面相同的时候，会出现重复，直接continue。
            path.append(candidates[i])  # 向path中加入元素
            self.DFS(candidates, i + 1, target -
                     candidates[i], path, result)  # 递归遍历下一层，每次修改target
            path.pop()  # pop()目的是为了回溯


candidates, target = [10, 1, 2, 7, 6, 1, 5], 8
s = Solution()
res = s.combinationSum2(candidates, target)
print(res)
