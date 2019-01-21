'''
求x的n次方
50. Pow(x, n):https://leetcode.com/problems/powx-n/
'''


class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # 处理n小于的情况
        if n < 0:
            x = 1 / x
            n = -n

        pow = 1
        while n:
            if n & 1:  # n为奇数，则乘以一次x
                pow *= x
            x *= x
            n >>= 1  # 右移1位，相当于除以2 ，n即使为偶数，最终也会变为1
        return pow


s = Solution()
x = 3
n = 4
pow = s.myPow(x, n)
print(pow)

# x = 2
# n= -3
# pow = s.myPow(x,n)
# print(pow)
