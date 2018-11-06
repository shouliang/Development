# coding=utf-8
# 回溯法
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        if not matrix and rows <= 0 and cols <= 0 and not path:
            return False
        # 初始化字符是否被访问的标记数组
        visited = [False] * (rows * cols)
        for row in range(rows):
            for col in range(cols):
                if self.hasPathCore(matrix, rows, cols, row, col, path, 0, visited):  # 从第一个(下标0)字符开始判断
                    return True

    def hasPathCore(self, matrix, rows, cols, row, col, path, currentPathLength, visited):
        if len(path) == currentPathLength:
            return True

        hasPath = False
        # 判断当前字符是否与数组里面的匹配，匹配则比较下一个
        # 递归比较下一个，下一个的可能位置为当前位置的上下左右
        # 如果不匹配回溯到上一个位置，并将当前位置设置为没有访问过
        if row >= 0 and row < rows and col >= 0 and col < cols \
                and matrix[row * cols + col] == path[currentPathLength] and not visited[row * cols + col]:
            currentPathLength += 1
            visited[row * cols + col] = True

            hasPath = self.hasPathCore(matrix, rows, cols, row - 1, col, path, currentPathLength, visited) or \
                      self.hasPathCore(matrix, rows, cols, row, col + 1, path, currentPathLength, visited) or \
                      self.hasPathCore(matrix, rows, cols, row + 1, col, path, currentPathLength, visited) or \
                      self.hasPathCore(matrix, rows, cols, row, col - 1, path, currentPathLength, visited)

            if not hasPath:
                currentPathLength -= 1
                visited[row * cols + col] = 0

        return hasPath


# matrix = [
#     ['A', 'B', 'C', 'E'],
#     ['S', 'F', 'C', 'S'],
#     ['A', 'D', 'E', 'E']
# ]

matrix = ['A', 'B', 'C', 'E', 'S', 'F', 'C', 'S', 'A', 'D', 'E', 'E']
s = Solution()

path = "ABCCED"
flag = s.hasPath(matrix, 3, 4, path)
print(flag)

path = "ASEE"
flag = s.hasPath(matrix, 3, 4, path)
print(flag)

path = "ABCESCEE"
flag = s.hasPath(matrix, 3, 4, path)
print(flag)
