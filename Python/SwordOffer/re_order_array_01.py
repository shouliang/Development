'''
题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

思路： 两指针，一个从左向右扫描，遇到偶数停止，一个从右往左扫描，遇到奇数停止，然后交换两数
但是此方便不能保证奇数和奇数，偶数和偶数之间的相对位置不变
'''
# coding=utf-8
class Solution:
    def reOrderArray(self, array):
        if not array:
            return []
        begin, end = 0, len(array) - 1

        while begin < end:
            # 向右一直移动，直到找到偶数
            while begin < end and array[begin] & 0x1 != 0:
                begin += 1

            # 向左一直移动，直到找到奇数
            while begin < end and array[end] & 0x1 == 0:
                end -= 1

            # 交换
            if begin < end:
                temp = array[begin]
                array[begin] = array[end]
                array[end] = temp
        return array


s = Solution()
array = [1, 2, 3, 4, 5, 6, 7]

s.reOrderArray(array)
print(array)
