def mergeSort(lyst):
    mergeSortHelper(lyst, 0, len(lyst) - 1)


def mergeSortHelper(lyst, low, high):
    if low < high:
        middle = (low + high) // 2
        mergeSortHelper(lyst, low, middle)
        mergeSortHelper(lyst, middle + 1, high)
        merge(lyst, low, middle, high)


def merge(lyst, low, middle, high):
    copyBuffer = Array(len(lyst))
    i1 = low
    i2 = middle + 1
    for i in range(low, high + 1):
        if i1 > middle:
            copyBuffer[i] = lyst[i2]
            i2 += 1
        elif i2 > high:
            copyBuffer[i] = lyst[i1]
        elif lyst[i1] < lyst[i2]:
            copyBuffer[i] = lyst[i1]
            i1 += 1
        else:
            copyBuffer[i] = lyst[i2]
            i2 += 1

    for i in range(low, high + 1):
        lyst[i] = copyBuffer[i]


class Array(object):
    def __init__(self, capacity, fillValue=None):
        self.items = list()
        for count in range(capacity):
            self.items.append(fillValue)

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, newItem):
        self.items[index] = newItem


lyst = [4, 5, 6, 1, 2, 3, 8, 7]
mergeSort(lyst)
print(lyst)
