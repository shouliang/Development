'''
岛屿的最大面积
给定一个包含了一些 0 和 1的非空二维数组 grid , 一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地) 构成的组合。
你可以假设二维矩阵的四个边缘都被水包围着。
找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)

示例 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。

示例 2:
[[0,0,0,0,0,0,0,0]]
对于上面这个给定的矩阵, 返回 0。

注意: 给定的矩阵grid 的长度和宽度都不超过 50。
'''


class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxArea = 0
        rows = len(grid)
        cols = len(grid[0]) if rows else 0
        visited = [[0] * cols] * rows

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    maxArea = max(maxArea, dfs(
                        grid, i, j, rows, cols, visited, maxArea))
        return maxArea


def dfs(grid, i, j, rows, cols, visited, result):
    if not result:
        result = 1
    else:
        result += 1
    visited[i][j] = 1
    if i > 0 and i < rows and j > 0 and j < cols:
        if not visited[i-1][j] and grid[i-1][j] == 1:
            dfs(grid, i-1, j, rows, cols, visited, result)
        if not visited[i+1][j] and grid[i+1][j] == 1:
            dfs(grid, i+1, j, rows, cols, visited, result)
        if not visited[i][j-1] and grid[i][j-1] == 1:
            dfs(grid, i, j-1, rows, cols, visited, result)
        if not visited[i][j+1] and grid[i][j+1] == 1:
            dfs(grid, i, j+1, rows, cols, visited, result)

    return result


grid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1]
]

s = Solution()
res = s.maxAreaOfIsland(grid)
print(res)
