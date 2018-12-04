'''
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
思路： 分成两部分计算
'''
class Solution:
    def multiply(self, A):
        result = [1] * len(A)

        # 先计算前半部分
        for i in range(1, len(A)):
            result[i] = result[i - 1] * A[i - 1]
            
        # 计算后半部分，并和前半部分相乘
        temp = 1
        for i in range(len(A) - 1, -1, -1):
            result[i] = result[i] * temp
            temp = temp * A[i]
        return result

A = [2, 3, 4, 5]
solution = Solution()
B = solution.multiply(A)
print(B)
