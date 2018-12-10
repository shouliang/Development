# coding=utf-8
def insertionSort(lyst):
    n = len(lyst)
    for i in range(1, n):     # i从1开始，因为是从未排序的向已排序的部分插入，开始已排序的位数组第一个元素
        itemToInsert = lyst[i]
        j = i - 1

        # 循环直到找到比itemToInsert要小的元素，将itemToInsert插入到j的后面一位，即j+1
        while j >= 0 and lyst[j] > itemToInsert:
            lyst[j + 1] = lyst[j]  # 移动元素
            j = j - 1

        lyst[j + 1] = itemToInsert


lyst = [4, 5, 6, 1, 2, 3]

insertionSort(lyst)

print(lyst)
