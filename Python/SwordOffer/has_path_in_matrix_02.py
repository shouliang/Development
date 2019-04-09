''' 矩阵中的路径
题目：请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个
格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则该路
径不能再进入该格子。 例如 a b c e s f c s a d e e 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含
"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
'''

'''
思路：优化版回溯法
1.将matrix字符串模拟映射为一个字符矩阵(但并不实际创建一个矩阵)
2.取一个boolean[matrix.length]标记某个字符是否已经被访问过,用一个布尔矩阵进行是否存在该数值的标记。
3.如果没找到结果，需要将对应的boolean标记值置回false,返回上一层进行其他分路的查找。
'''
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
        # 递归比较下一个，下一个的可能位置为当前位置的上下左右四个位置
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
