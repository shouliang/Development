# coding=utf-8
'''
题目描述
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
'''
import heapq
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        result = []

        for index in range(0, len(tinput)):
            if index < k:
                result.append(tinput[index])
            else:
                max_in_k = max(result)
                if tinput[index] < max_in_k:
                    result.remove(max_in_k)
                    result.append(tinput[index])

        return result

array = [4, 5, 1, 6, 2, 7, 3, 8]

s = Solution()
print(s.GetLeastNumbers_Solution(array, 4))
