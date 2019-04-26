# n个数，第1次找出n个数中最小的放到第1个位置
#       第2次  找出后面n-1个数中最小的放到第2个位置
#       第n-1次找出后面2个数中最小的放到第n-1个位置
#       第n次  找出后面1个数中最小的放到第n个位置,故第n次可以不用做，即外层循环为n-1次

def selectionSort(nums):
    n = len(nums)
    for i in range(n-1):  # 外层循环只需要n-1次
        minIndex = i
        for j in range(i + 1, n):
            if nums[j] < nums[minIndex]:
                minIndex = j

        # i如果已经在正确的位置上，则不需要交换
        if minIndex != i:
            swap(lyst, minIndex, i)


def swap(lyst, i, j):
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp


lyst = [4, 5, 6, 1, 2, 3,7]

selectionSort(lyst)
print(lyst)
