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


# matrix = [
#     ['A', 'B', 'C', 'E'],
#     ['S', 'F', 'C', 'S'],
#     ['A', 'D', 'E', 'E']
# ]

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
