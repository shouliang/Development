'''
题目描述
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''
class Solution:
    def GetUglyNumber_Solution(self, index):
        if index < 0:
            return 0
        number = 1
        uglyNum = 1

        while uglyNum < index:
            number +=1
            if self.IsUgly(number):
                print(number)
                uglyNum +=1

        return number

    def IsUgly(self, number):
        while number % 2 == 0:
            number //= 2

        while number % 3 == 0:
            number //= 3

        while number % 5 == 0:
            number //= 5

        return number == 1


s = Solution()
number = s.GetUglyNumber_Solution(100)
# print(number)