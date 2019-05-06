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
        self.di = [-1, 1, 0, 0]
        self.dj = [0, 0, -1, 1]
        self.rows, self.cols = len(grid), len(grid[0])
        self.grid = grid
        self.visited = set()

        return sum([self.DFS(i, j) for i in range(self.rows) for j in range(self.cols)])

    def DFS(self, i, j):
        if not self.isValid(i, j):
            return 0

        self.visited.add((i, j))

        # 向前后左右四周扩散
        for k in range(4):
            self.DFS(i + self.di[k], j + self.dj[k])
        return 1

    def isValid(self, i, j):
        if i < 0 or i >= self.rows or j < 0 or j >= self.cols or self.grid[i][j] == '0' or ((i, j) in self.visited):
            return False
        return True
