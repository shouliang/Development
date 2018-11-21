# coding=utf-8
'''
题目描述
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
'''


class Solution:
    def __init__(self):
        self.stack_data = []  # 保存数据的栈
        self.stack_min = []  # 保存最小值的栈

    # 向数据栈内压入数据，若最小值栈为空或者当前节点的值小于最小值栈的栈顶元素则该节点压入最小值栈
    def push(self, node):
        self.stack_data.append(node)
        if len(self.stack_min) == 0:
            self.stack_min.append(node)
        if node < self.stack_min[- 1]:
            self.stack_min.append(node)

    # 数据栈退栈，若最小值栈的栈顶元素刚好等于退出的数值，则最小值栈也退栈
    def pop(self):
        if len(self.stack_data):
            data = self.stack_data.pop()
            if len(self.stack_min) and data == self.stack_min[-1]:
                self.stack_min.pop()
        return

    def top(self):
        if len(self.stack_data):
            return self.stack_data[-1]
        return 0

    def min(self):
        if len(self.stack_min):
            return self.stack_min[- 1]
        return 0
