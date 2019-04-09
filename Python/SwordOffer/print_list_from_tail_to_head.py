class ListNode:
    def __init__(self, x):
        self.val = x
        self.next =None

# 从尾到头打印链表，利用栈的"先进后出"的特性
class Solution:
    def printListFromTailToHead(self, listNode):
        stack = []
        tailToHeadList = []
        node = listNode

        # 遍历链表并压栈
        while node:
            stack.append(node.val)
            node = node.next

        while stack:
            tailToHeadList.append(stack.pop())
        return tailToHeadList


head = ListNode(0)
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

head.next = node1
node1.next = node2
node2.next = node3

s = Solution()
print(s.printListFromTailToHead(head))