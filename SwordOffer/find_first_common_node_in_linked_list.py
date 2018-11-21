# coding=utf-8
'''
题目描述
输入两个链表，找出它们的第一个公共结点。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None

        len1 = self.GetLength(pHead1)
        len2 = self.GetLength(pHead2)
        lenDiff = len1 - len2

        pLong, pShort = pHead1, pHead2
        if lenDiff < 0:
            pLong, pShort = pHead2, pHead1

        # 长的列表直接跳到长短列表的数量差
        for i in range(lenDiff):
            pLong = pLong.next

        while pLong and pShort and pLong != pShort:
            pLong = pLong.next
            pShort = pShort.next

        return pShort

    def GetLength(self, pHead):
        length = 0
        while pHead:
            pHead = pHead.next
            length += 1
        return length


p1 = ListNode(1)
p2 = ListNode(2)
p3 = ListNode(3)
p4 = ListNode(4)
p5 = ListNode(5)
p6 = ListNode(6)

p1.next = p2
p2.next = p3
p3.next = p4

p5.next = p6
p6.next = p3

s = Solution()
p = s.FindFirstCommonNode(p1, p5)
if p:
    print(p.val)
