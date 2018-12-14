# 求平方根
# 思路：利用二分查找的思路，逐渐缩小范围
import math
class Soultion:
    def mySqrt(self, x, delta):
        if x == 0 or x == 1:
            return x
        left, right, result = 1, x, 0
        while left <= right:
            middle = (left + right) / 2
            if math.fabs(x - middle * middle) <= delta:
                return middle
            if middle * middle > x:
                right = middle
            else:
                left = middle
        return result


x, delta = 11, 0.0001
s = Soultion()
print(s.mySqrt(x,delta))
