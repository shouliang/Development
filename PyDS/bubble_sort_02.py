def bubbleSort(lyst):
    n = len(lyst)
    for i in range(n):
        for j in range(n - i - 1):
            if lyst[j] > lyst[j + 1]:
                swap(lyst, j, j + 1)


def swap(lyst, i, j):
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp


lyst = [4, 5, 6, 3, 2, 1]

bubbleSort(lyst)
print(lyst)
