'''
输入一个链表，输出该链表中倒数第k个结点。
思路： 设置一前一后两个指针，使其保持k-1的距离，当后一个指针到达尾部，则前一个指针到达倒数第k个位置
'''


# coding=utf-8

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        if not head or k <= 0:
            return None
        pFront, pBehind = head, head

        # 首先移动后一个指针到k-1的位置
        for i in range(k):
            if pBehind:
                pBehind = pBehind.next
            else:
                return None
        # 然后前后指针同时移动，直到后一个指针到达链表尾部
        while pBehind:
            pFront = pFront.next
            pBehind = pBehind.next

        return pFront


p1 = ListNode(1)
p2 = ListNode(2)
p3 = ListNode(3)
p4 = ListNode(4)
p5 = ListNode(5)

p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5

s = Solution()
p = s.FindKthToTail(p1, 1)
print(p.val)
