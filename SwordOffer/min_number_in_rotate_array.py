# coding=utf-8

# 旋转数组的最小数字： 如：1，2，3, 4, 5 旋转为3，4，5，1，2
# 局部有序，利用二分查找的思想来相似地解决
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray:
            return 0

        start = 0
        end = len(rotateArray) - 1
        middle = start
        while rotateArray[start] >= rotateArray[end]:
            if end - start == 1:
                middle = end
                break

            middle = start + ((end - start) >> 1)

            # 相等则顺序查找
            if rotateArray[start] == rotateArray[middle] and rotateArray[end] == rotateArray[middle]:
                self.minInorder(rotateArray, start, end)

            if rotateArray[middle] >= rotateArray[start]:
                start = middle
            elif rotateArray[middle] <= rotateArray[start]:
                end = middle

        return rotateArray[middle]

    # 顺序查找最小值
    def minInorder(self, rotateArray, start, end):
        minNum = rotateArray[start]
        length = end - start
        for i in range(length):
            if rotateArray[start + i] < minNum:
                minNum = rotateArray[start + i]
        return minNum


s = Solution()

num = s.minNumberInRotateArray([3, 4, 5, 1, 2])
print(num)


