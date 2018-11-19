# coding=utf-8
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack_data = []
        self.stack_min = []

    def push(self, node):
        self.stack_data.append(node)
        if len(self.stack_min) == 0:
            self.stack_min.append(node)
        if node < self.stack_min[len(self.stack_min) - 1]:
            self.stack_min.append(node)

    def pop(self):
        if len(self.stack_data):
            self.stack_data.pop()

    def top(self):
        pass

    def min(self):
        if len(self.stack_min):
            return self.stack_min.pop()
