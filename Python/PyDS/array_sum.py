# coding=utf-8
'''
数组求和
'''

# 循环遍历做法
def sum1(array):
    sum = 0
    for value in array:
        sum += value
    return sum


# 递归： 分解为最后一位+前n-1项的求和，递归终止条件：n == 1
def sum2(array):
    def sumCore(array, n):
        if n == 1:
            return array[0]
        return array[n - 1] + sumCore(array, n - 1)

    return sumCore(array, len(array))

# 二分递归：分解为前后两部分求和
def sum3(array):
    def sumCore(array, i, n):
        if n <= 1:
            return array[i]
        return sumCore(array, i, n // 2) + sumCore(array, i + (n // 2), n // 2)

    return sumCore(array, 0, len(array) - 1)


sum1 = sum1([5, 3, 6, 7])
print(sum1)

sum2 = sum2([5, 3, 6, 7])
print(sum2)

sum3 = sum3([5, 3, 6, 7])
print(sum2)
