''' 
求平方根
69. Sqrt(x):https://leetcode.com/problems/sqrtx/
思路：利用二分查找的思路，逐渐缩小范围
'''

import math

class Soultion:
    def mySqrt(self, x):
        if x == 0 or x == 1 : return x 
        low,high = 1 ,x 
        res = 0
        while low <=high:
            mid = low + ((high - low)>>1)
            if mid * mid == x :
                return mid 
            elif mid * mid > x:
                high = mid - 1
            else:
                low = mid + 1
                res = mid 
        return res 
   


x = 8
s = Soultion()
print(s.mySqrt(x))
