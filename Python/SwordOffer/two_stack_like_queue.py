'''
题目：用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''

'''
有两个栈stackA、stackB，A是入栈的，B是出栈的，入栈时，直接进入A即可，出栈时，先判断是否有元素，
如果B没有元素，pop肯定报错，应该先将A中所有的元素压倒B里面，再pop最上面一个元素，如果B中有就直接pop出，就可以，
这是最优的思路，两个栈实现了先进后出，在一起又实现了队列的先进先出。

'''

# 用俩个栈模拟队列的进队列，出队列

# 思路：入队列：始终压入stackA
#      出队列：stackB不为空：出stackB的栈顶元素；stackB为空：则将stackA的每一个元素依次并弹出压入stackA中
class Solution:
    def __init__(self):
        self.stackA = []
        self.stackB = []

    def push(self, node):
        # write code here
        self.stackA.append(node)

    def pop(self):
        if self.stackB:
            return self.stackB.pop()
        else:
            while self.stackA:
                 self.stackB.append(self.stackA.pop())
            return self.stackB.pop()


s = Solution()
s.push(1)
s.push(2)
s.push(3)
s.push(4)

print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())





