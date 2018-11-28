'''
题目描述
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
如果有多对数字的和等于S，输出两个数的乘积最小的。
'''


class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if not array:
            return []
        begin, end = 0, len(array) - 1
        cursum = 0
        while begin < end:
            cursum = array[begin] + array[end]
            if cursum == tsum:
                return [array[begin], array[end]]
            elif cursum > tsum:
                end -= 1
            else:
                begin += 1
        return []


array,tsum = [1, 2, 4, 7, 11, 15],15
# array, tsum = [1, 2, 4, 7, 11, 16], 10
# array, tsum = [], 0

s = Solution()
res = s.FindNumbersWithSum(array, tsum)
print(res)
