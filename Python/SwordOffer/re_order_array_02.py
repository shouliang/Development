'''
题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

思路： 遍历原数组，将奇数和偶数放入对应的数组，最后合并两数组并返回
'''

# coding=utf-8
class Solution:
    def reOrderArray(self, array):
        if not array:
            return []
        odd, even = [],[]
        for value in array:
            if value & 0x1 == 1:
                odd.append(value)  # 放入奇数数组
            else:
                even.append(value) # 方式偶数数组
        return odd + even          # 返回奇数数组 + 偶数数组

s = Solution()
array = [1, 2, 3, 4, 5, 6, 7]

newArray = s.reOrderArray(array)
print(newArray)
