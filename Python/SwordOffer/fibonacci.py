# 斐波那契
# 递归：简洁但是会产生重复的计算
class Solution:
    # def Fibonacci(self, n):
    #     if n == 0 or n == 1:
    #         return n
    #     return self.Fibonacci(n - 1) + self.Fibonacci(n - 2)

    # 循环的方式求斐波那契数列
    def Fibonacci(self, n):
        # 特殊处理0和1的情况
        if n == 0 or n == 1:
            return n

        fbn_1 ,fbn_2 ,fbn = 0,1,0

        # i从2开始
        for i in range(2, n + 1):
            fbn = fbn_1 + fbn_2
            fbn_1 = fbn_2
            fbn_2 = fbn
        return fbn


s = Solution()

i = 0
while i < 10:
    print(s.Fibonacci(i))
    i += 1
