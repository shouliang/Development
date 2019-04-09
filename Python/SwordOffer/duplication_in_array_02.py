# coding=utf-8
# 题目描述
# 在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
# 请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。

class Solution:
    def duplicate(self, numbers, duplication):
        if not numbers:
            return False
        for i, value in enumerate(numbers):
            # 检测i与numbers[i]是否相同，不相同则一直交换
            # 交换的位置: i和numbers[i],对应的数值则为 numbers[i]和numbers[numbers[i]]
            while i != numbers[i]:
                if numbers[i] == numbers[numbers[i]]:
                    duplication = numbers[i]
                    return duplication, True

                # 交换numbers[i] 与 numbers[ numbers[i] ]
                temp = numbers[i]
                numbers[i] = numbers[temp]
                numbers[temp] = temp

        return -1, False


numbers = [2, 4, 3, 1, 4]

s = Solution()
flag = s.duplicate(numbers, duplication=-1)
print(flag)
