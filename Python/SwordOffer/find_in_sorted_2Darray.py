# 二维数组每一行从左到右递增，每一列从上到下递增
# 从有以上特性的二维数组中查询目标数字
# 思路：是从右上角开始，发现规律：比它小则此列不用搜索，比它大则此行不用搜索

class Solution:
    # array 二维列表
    def Find(self, target, array):
        found = False
        if not len(array):
            return False
        # 初始化
        rows = len(array)
        columns = len(array[0])
        row = 0
        column = columns - 1

        while row < rows and column >= 0:
            if array[row][column] == target:
                found = True
                break
            elif array[row][column] > target:
                column -= 1
            else:
                row += 1
        return found


s = Solution()

flag = s.Find(6, [[1, 2, 3], [4, 5, 6]])
print(flag)

flag = s.Find(7, [])
print(flag)
