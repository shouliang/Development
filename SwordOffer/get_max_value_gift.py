'''
礼物的最大值
'''


class Solution:
    def getMaxValue(self, values, rows, cols):
        if not values or not rows or not cols:
            return 0

        left, up = 0, 0
        max_values = [0] * cols
        for i in range(rows):
            for j in range(cols):
                if i > 0:
                    up = max_values[j - 1]
                if j > 0:
                    up = max_values[j]
                max_values[j] = max(left, up) + values[i][j]
        return max_values[cols - 1]


values = [
    [1, 10, 3, 8],
    [12, 2, 9, 6],
    [5, 7, 4, 11],
    [3, 7, 16, 5]
]

s = Solution()
max_value = s.getMaxValue(values, len(values), len(values[0]))
print(max_value)
