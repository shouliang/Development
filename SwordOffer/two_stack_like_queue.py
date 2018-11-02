# 用俩个栈模拟队列的进队列，出队列

# 思路：入队列：始终压入stack1
#      出队列：stack2不为空：出stack2的栈顶元素；stack2为空：则将stack1的每一个元素依次并弹出压入stack1中
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        # write code here
        self.stack1.append(node)

    def pop(self):
        if self.stack2:
            return self.stack2.pop()
        else:
            while self.stack1:
                 self.stack2.append(self.stack1.pop())
            return self.stack2.pop()


s = Solution()
s.push(1)
s.push(2)
s.push(3)
s.push(4)

print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())





