'''
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null
思路： 首先判断链表中是否有环：受"龟兔赛跑"启发，定义一慢一快两指针，有环则会相遇
      然后把一个指针退回到头节点，另外一个保持不动
      最后两个指针同时移动一位，则相遇的位置为入口结点
'''


# coding=utf-8

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        if not pHead or not pHead.next:
            return None

        slow, fast = pHead, pHead
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                slow = pHead
                while slow is not fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None


p1 = ListNode(1)
p2 = ListNode(2)
p3 = ListNode(3)
p4 = ListNode(4)
p5 = ListNode(5)

p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5
p5.next = p2

s = Solution()
entryNode = s.EntryNodeOfLoop(p1)
if entryNode:
    print(entryNode.val)
