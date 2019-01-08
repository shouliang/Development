''' leetcode39,组合总和I
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 canddates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。

思路：
本题采用回溯算法，即深度遍历DFS
1. 基本思路是先排好序，这样做的目的是为了对数组后面不可能出现的情况进行排除，有利于减少查找时间，即剪枝操作
2. 外层循环对数组元素依次进行遍历，依次将 nums 中的元素加入中间集，一旦满足条件，就将中间集加入结果集
3. 然后每次递归中把剩下的元素一一加到结果集合中，并且把目标减去加入的元素，
然后把剩下元素（包括当前加入的元素）放到下一层递归中解决子问题。


'''


class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: L st[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()  # 先排序，方便后来剪枝
        results = []  # 最终解的集合
        path = []  # 其中一个解
        self.DFS(candidates, 0, target, path, results)
        return results

    def DFS(self, candidates, cur, target, path, results):
        if target == 0:  # 递归终止条件：1.找到一个解添加到结果集返回，或者2.不满足条件即：target<0，也起到剪枝的作用，直接返回
            results.append(path[:])  # 满足条件将其中的一个解加入结果集，此处需要注意Python的语法是解的一个副本
            return
        if target < 0:
            return  # 剪枝

        for i in range(cur, len(candidates)):  # 从这个数本身开始进行搜索，即从i开始
            path.append(candidates[i])  # 向path中加入元素
            self.DFS(candidates, i, target - candidates[i], path, results)  # 递归遍历下一层，每次修改target
            path.pop()  # pop()目的是为了回溯


candidates, target = [2, 3, 6, 7], 7
s = Solution()
res = s.combinationSum(candidates, target)
print(res)
