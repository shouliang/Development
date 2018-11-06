# coding=utf-8
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        for i in range(rows):
            for j in range(cols):
                if matrix[i * cols + j] == path[0]:
                    if self.findPath(list(matrix), rows, cols, path[1:], i, j):
                        return True

    def findPath(self, matrix, rows, cols, path, i, j):
        if not path:
            return True
        matrix[i * cols + j] = 0
        if j + 1 < cols and matrix[i * cols + j + 1] == path[0]:
            return self.findPath(matrix, rows, cols, path[1:], i, j + 1)
        elif j - 1 >= 0 and matrix[i * cols + j - 1] == path[0]:
            return self.findPath(matrix, rows, cols, path[1:], i, j - 1)
        elif i + 1 < rows and matrix[(i + 1) * cols + j] == path[0]:
            return self.findPath(matrix, rows, cols, path[1:], i + 1, j)
        elif i - 1 >= 0 and matrix[(i - 1) * cols + j] == path[0]:
            return self.findPath(matrix, rows, cols, path[1:], i - 1, j)
        else:
            return False


# matrix 为一维数组的形式
matrix = ['A', 'B', 'C', 'E', 'S', 'F', 'C', 'S', 'A', 'D', 'E', 'E']
s = Solution()

path = "ABCCED"
flag = s.hasPath(matrix, 3, 4, path)
print(flag)

path = "SEEDE"
flag = s.hasPath(matrix, 3, 4, path)
print(flag)

path = "ABCESCEE"
flag = s.hasPath(matrix, 3, 4, path)
print(flag)
