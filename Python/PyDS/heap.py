class Heap:
    def __init__(self, capaciyt):
        self.a = [] * (capaciyt + 1)
        self.n = capaciyt
        self.count = 0

    def insert(self, data):
        if self.count >= self.n:
            return
        self.count += 1
        self.a[self.count] = data

        i = self.count
        while i // 2 > 0 and self.a[i] > self.a[i // 2]:
            swap(self.a, i, i // 2)
            i = i // 2

    def removeMax(self):
        if self.count == 0:
            return -1
        self.a[1] = self.a[self.count]
        self.count -= 1

    def heapify(self, a, n, i):
        while True:
            maxPos = i
            if i * 2 <= n and a[i] < a[i * 2]:
                maxPos = i * 2
            if i * 2 + 1 <= n and a[maxPos] < a[i * 2 + 1]:
                maxPos = i * 2 + 1
            if maxPos == i:
                break
            swap(a, i, maxPos)
            i = maxPos


def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp
