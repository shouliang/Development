''' 
三角形最小路径和
120. Triangle:https://leetcode.com/problems/triangle/
解释：
    给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
    例如，给定三角形：

    [
        [2],
        [3,4],
    [6,5,7],
    [4,1,8,3]
    ]
    自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

    说明：
    如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。

思路：动态规划： 自底向上
    minpath[k][i] = min( minpath[k+1][i], minpath[k+1][i+1]) + triangle[k][i];
    Or even better, since the row minpath[k+1] would be useless after minpath[k] is computed,
    we can simply set minpath as a 1D array, and iteratively update itself:

    For the kth level:
    minpath[i] = min( minpath[i], minpath[i+1]) + triangle[k][i]; 
'''


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        dp = triangle[-1]    # dp[j]定位为到第j层的最小和，因为自底向上，故初始化为最底一层，即为到自身的最小和为自身的值
        for i in range(len(triangle)-2, -1, -1):  # for each layer
            for j in range(len(triangle[i])):     # check its every 'node'
                # Find the lesser of its two children, and sum the current value in the triangle with it
                dp[j] = min(dp[j],  dp[j+1]) + triangle[i][j]
        return dp[0]


triangle = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]
s = Solution()
min_total = s.minimumTotal(triangle)
print(min_total)
