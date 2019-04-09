'''
题目描述
求一到n相加的和，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

思路：递归+短路判断终止
'''
class Solution:
    def Sum_Solution(self, n):
        # write code here
        return n and n + self.Sum_Solution(n - 1)