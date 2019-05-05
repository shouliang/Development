'''
岛屿的个数 
200. Number of Islands: https://leetcode.com/problems/number-of-islands/
'''


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype:
        """
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        # self.visited = set()

        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    res += 1
                    self.DFS(grid, i, j, cols, rows)
        return res

    def DFS(self, grid, i, j, rows, cols):
        if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == '0' :
            return
        # self.visited.add((i, j))
        grid[i][j] = '0'
        self.DFS(grid, i + 1, j, rows, cols)
        self.DFS(grid, i - 1, j, rows, cols)
        self.DFS(grid, i, j + 1, rows, cols)
        self.DFS(grid, i, j - 1, rows, cols)
