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

        self.rows, self.cols = len(grid), len(grid[0])
        self.grid = grid
        self.visited = set()  # 创建集合：不允许有重复元素

        res = 0
        # 遍历所有节点
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == '1' and ((i, j) not in self.visited):
                    self.DFS(i, j)
                    res += 1       # 每深度遍历一次，就是一个岛屿，将结果加1
        return res

    def DFS(self, i, j):
        # 检测索引i和j的合法性 以及是否为1和是否已被访问过
        if i < 0 or i >= self.rows or j < 0 or j >= self.cols or self.grid[i][j] == '0' or ((i, j) in self.visited):
            return

        self.visited.add((i, j))

        # 访问所有的邻居，即前后上下
        self.DFS(i - 1, j)
        self.DFS(i + 1, j)
        self.DFS(i, j - 1)
        self.DFS(i, j + 1)


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "1"],
    ["0", "0", "0", "1", "1"]
]

s = Solution()
nums = s.numIslands(grid)
print(nums)
