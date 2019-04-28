def bubbleSort(lyst):
    n = len(lyst)
    while n > 1:
        i = 1

        while i < n:
            if lyst[i - 1] > lyst[i]:
                swap(lyst, i - 1, i)
            i = i + 1

        n = n - 1

def swap(lyst, i, j):
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp

lyst = [4,5,6,3,2,1]

bubbleSort(lyst)
print(lyst)