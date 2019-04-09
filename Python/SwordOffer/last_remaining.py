'''
题目：
0,1，...n-1这n个数字排成一个圆圈，从数字0开始每次从这个圆圈里删除第m个数字，求出这个圆圈里剩下的最后一个数字。

实质约瑟夫环的公式是：
f(n, m) = 0           (n = 1)
f(n, m) = [f(n-1, m) +m] % n  (n > 1)
'''
class Solution:
    def LastRemaining_Solution(self, n, m):
        if n == 0 or m < 1:
            return -1
        last = 0
        for i in range(2, n + 1):
            last = (last + m) % i
        return last
