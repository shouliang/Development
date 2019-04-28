# 两两比较然后交换，第1次     将n个中最大的交换到倒数第1个位置，即 n - 1 的位置
#                第2次     将剩余的n-1个最大值交换到倒数第2个位置 ,即 n - 2 的位置
#                第n - 1次 将剩余的 2个最大值交换到倒数第n-1个位置 ,即 1 的 位置， 
#                                                                      此时还剩最后一个元素，它就是最大值，且已经倒数第n个位置，即第0的位置
def bubbleSort(nums):
    n = len(nums)
    for i in range(n - 1):             # 外循环只需要 n - 1 
        for j in range((n - 1) - i):
            if nums[j] > nums[j + 1]:  # 前面一个比后面大，就交换，最近的排序的结果就是从小到大
                swap(nums, j, j + 1)



def bubbleSort_02(lyst):
    n = len(lyst)
    i = 0
    while i < n - 1:
        for j in range(n - i - 1):
            if lyst[j] > lyst[j + 1]:  # 前面一个比后面大，就交换
                swap(lyst, j, j + 1)
        i += 1


def bubbleSort_03(lyst):
    n = len(lyst)

    while n > 1:                       # Do n - 1 bubbles
        for j in range(n - 1):         # Start each bubble
            if lyst[j] > lyst[j + 1]:  # Exchanged if needed
                swap(lyst, j, j + 1)
        n -= 1


def swap(lyst, i, j):
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp


lyst = [4, 5, 6, 3, 2, 1, 7, 8]
bubbleSort(lyst)
print(lyst)

lyst_03 = [4, 5, 6, 3, 2, 1, 7, 8]
bubbleSort(lyst_03)
print(lyst_03)

lyst_03 = [4, 5, 6, 3, 2, 1, 7, 8]
bubbleSort(lyst_03)
print(lyst_03)
