import heapq
import collections


class MinStack:
    def __init__(self):
        self.stack_data = []
        self.heap = []

    def push(self, x):
        self.stack_data.append(x)
        heapq.heappush(self.heap, x)

    def pop(self):
        if len(self.stack_data):
            data = self.stack_data.pop()
            if len(self.heap) and data == self.heap[0]:
                heapq.heappop(self.heap)

    def top(self):
        if len(self.stack_data):
            return self.stack_data[-1]

    def getMin(self):
        if len(self.heap):
            return self.heap[0]


class MinStack01:
    def __init__(self):
        self.stack_data = []
        self.heap = []

    def push(self, x):
        self.stack_data.append(x)
        heapq.heappush(self.heap, x)

    def pop(self):
        if len(self.stack_data):
            data = self.stack_data.pop()
            if len(self.heap) and data == self.heap[0]:
                heapq.heappop(self.heap)

    def top(self):
        if len(self.stack_data):
            return self.stack_data[-1]

    def getMin(self):
        if len(self.heap):
            return self.heap[0]


class MinStack02:
    def __init__(self):
        self.stack_data = []
        self.heap = []

    def push(self, x):
        self.stack_data.append(x)
        heapq.heappush(self.heap, x)

    def pop(self):
        if len(self.stack_data):
            data = self.stack_data.pop()
            if len(self.heap) and data == self.heap[0]:
                heapq.heappop(self.heap)

    def top(self):
        if len(self.stack_data):
            return self.stack_data[-1]

    def getMin(self):
        if len(self.heap):
            return self.heap[0]


class LRUCache:
    def __init__(self, capacity):
        self.dict = collections.OrderedDict()
        self.remain = capacity

    def get(self, key):
        if key not in self.dict:
            return -1
        val = self.dict.pop(key)
        self.dict[key] = val
        return val

    def put(self, key, value):
        if key in self.dict:
            self.dict.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.dict.popitem(last=False)

        self.dict[key] = value


class LRUCache01:
    def __init__(self, capacity):
        self.dict = collections.OrderedDict()
        self.remain = capacity

    def get(self, key):
        if key not in self.dict:
            return -1
        value = self.dict.pop(key)
        self.dict[key] = value

    def set(self, key, value):
        if key in self.dict:
            self.dict.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.dict.popitem(last=False)
        self.dict[key] = value


class LRUCache02:
    def __init__(self, capacity):
        self.dict = collections.OrderedDict()
        self.remain = capacity

    def get(self, key):
        if key not in self.dict:
            return -1
        value = self.dict.pop(key)
        self.dict[key] = value
        return value

    def set(self, key, value):
        if key in self.dict:
            self.dict.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.dict.popitem(last=False)

        self.dict[key] = value


class LRUCache03:
    def __init__(self, capacity):
        self.dict = collections.OrderedDict()
        self.remain = capacity

    def get(self, key):
        if key not in self.dict:
            return -1
        value = self.dict.pop(key)
        self.dict[key] = value
        return value

    def set(self, key, value):
        if key in self.dict:
            self.dict.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.dict.popitem(last=False)

        self.dict[key] = value
