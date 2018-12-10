def selectionSort(lyst):
    n = len(lyst)
    for i in range(0, n - 1):
        minIndex = i
        for j in range(i + 1, n):
            if lyst[j] < lyst[minIndex]:
                minIndex = j

        # i如果已经在正确的位置上，则不需要交换
        if minIndex != i:
            swap(lyst, minIndex, i)


def swap(lyst, i, j):
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp


lyst = [4, 5, 6, 1, 2, 3]

selectionSort(lyst)
print(lyst)
