# 两两比较然后交换， 第一次将n个中最大的交换到倒数第1个位置
#                第二次将剩余的n-1个最大值交换到倒数第2个位置
def bubbleSort(lyst):
    n = len(lyst)
    for i in range(n):
        for j in range(n - i - 1):
            if lyst[j] > lyst[j + 1]: # 前面一个比后面大，就交换
                swap(lyst, j, j + 1)


def swap(lyst, i, j):
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp


lyst = [4, 5, 6, 3, 2, 1,7]

bubbleSort(lyst)
print(lyst)
