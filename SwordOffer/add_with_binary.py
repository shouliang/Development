class Solution:
    def Add(self, num1, num2):
        sum, carry = 0, 0
        while num2:
            sum = num1 ^ num2           # 异或不产生进位
            carry = (num1 & num2) << 1  # 与运算计算进位：但需要左移一位，直到不产生进位

            num1 = sum    # 将不产生进位的结果，赋值给num1
            num2 = carry  # 将进位赋值给num2,进入一下轮循环
        return num1


s = Solution()
sum = s.Add(5, 17)
print(sum)
