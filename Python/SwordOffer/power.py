# coding=utf-8
'''
需要注意的地方:
当指数为负数的时候
当底数为零切指数为负数的情况
在判断底数base是不是等于0的时候,不能直接写base==0, 因为计算机内表示小数时有误差,只能判断他们的差的绝对值是不是在一个很小的范围内
当n为偶数, a^n = a^(n/2) * a^(n/2)
当n为奇数, a^n = a^((n-1)/2) * a^((n-1)/2)) * a
利用右移一位运算代替除以2
利用位与运算代替了求余运算法%来判断一个数是奇数还是偶数
优化代码速度
'''


class Solution:
    def Power(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base

        # exponent小于0时，计算绝对值
        tempExponent = exponent
        if tempExponent < 0:
            exponent = -exponent

        # 先计算偶数部分
        result = self.Power(base, exponent >> 1)
        result = result * result
        # 如果exponent为奇数，算完偶数部分后还需要再乘以一次底，另位与运算为1：说明是奇数
        if exponent & 0x1 == 1:
            result = result * base

        # exponent小于0时，结果为其倒数
        if tempExponent < 0:
            result = 1 / result
        return result


s = Solution()
num = s.Power(2, 3)
print(num)

num = s.Power(2, -3)
print(num)
