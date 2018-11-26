'''
题目描述
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''


class Solution:
    def GetUglyNumber_Solution(self, index):
        if index < 1:
            return 0

        ugly_nums = [0] * index
        ugly_nums[0] = 1
        ugly_next_index = 1

        p2, p3, p5 = 0, 0, 0

        while ugly_next_index < index:
            min_value = min(ugly_nums[p2] * 2, ugly_nums[p3] * 3, ugly_nums[p5] * 5)
            ugly_nums[ugly_next_index] = min_value

            while ugly_nums[p2] * 2 <= ugly_nums[ugly_next_index]:
                p2 += 1
            while ugly_nums[p3] * 3 <= ugly_nums[ugly_next_index]:
                p3 += 1
            while ugly_nums[p5] * 5 <= ugly_nums[ugly_next_index]:
                p5 += 1

            ugly_next_index += 1

        return ugly_nums[ugly_next_index - 1]


s = Solution()
number = s.GetUglyNumber_Solution(1000)
print(number)
