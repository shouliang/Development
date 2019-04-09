''' 
最小栈
155. Min Stack:https://leetcode.com/problems/min-stack/
'''
import heapq


class MinStack:
    def __init__(self):
        self.stack_data = []  # 存储数据的stack
        self.heap = []        # 小顶堆，维护min

    def push(self, x):
        self.stack_data.append(x)     # 正常push
        heapq.heappush(self.heap, x)  # 正常push,小顶堆自动维护

    def pop(self):
        if len(self.stack_data):
            data = self.stack_data.pop()
            # 需要判断pop的data是否与小顶堆的堆顶元素相等
            if len(self.heap) and data == self.heap[0]:
                heapq.heappop(self.heap)                 # 若相等则从小顶堆删除，小顶堆会自动维护

    def top(self):
        if len(self.stack_data):
            return self.stack_data[-1]

    def getMin(self):
        if len(self.heap):
            return self.heap[0]  # 最小数，返回小顶堆堆顶元素


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  # 返回 -3.
minStack.pop()
print(minStack.top())  # 返回 0.
print(minStack.getMin())  # 返回 -2.
