# coding=utf-8
# 题目描述
# 在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
# 请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。

# 思路： 二分查找 + 统计区间数字个数

class Solution:
    def duplicate(self, numbers, duplication):
        if not numbers:
            return False

        start = 0
        end = len(numbers) - 1
        while start <= end:
            # middle = (start + end) /2
            middle = start + ((end - start) >> 1)
            # 统计start到middle的个数
            count = self.countRange(numbers, start, middle)
            # start == end，表明最终聚焦到一个数，然后再判断它的数目是否大于1，来判断其是否重复
            if start == end:
                if count > 1:
                    return start, True
                else:
                    break
            if count > (middle - start) + 1:  # count的数量大于start和middle之间的数字数量，说明重复的数字在前半部分
                end = middle
            else:  # 否则说明重复的数字在后半部分
                start = middle + 1
        return -1, False

    def countRange(self, numbers, start, end):
        if not numbers:
            return 0
        count = 0
        for value in numbers:
            if value >= start and value <= end:
                count += 1
        return count


s = Solution()
numbers = [2, 3, 1, 0, 2, 5, 3]
flag = s.duplicate(numbers, duplication=-1)
print(flag)

# numbers = [2, 3, 1, 0, 3, 5, 3]
# flag = s.duplicate(numbers, duplication=-1)
# print(flag)
#
# numbers = [2, 3, 1, 0, 4, 5, 4]
# flag = s.duplicate(numbers, duplication=-1)
# print(flag)
