'''
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''
# coding=utf-8
# 单链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        p = merge = self
        while pHead1 and pHead2:
            if pHead1.val > pHead2.val:
                merge.next = pHead2
                pHead2 = pHead2.next
            elif pHead2.val >= pHead1.val:
                merge.next = pHead1
                pHead1.next = pHead1
            merge.next = merge
        #注意：当由于其中一链表pHead1或者pHead2为null，导致跳出while循环时，
        #此时，还需要将另一不为null的链表的后续部分赋给合并链表。 
        merge = pHead1 or pHead2
        return p.next

p11 = ListNode(1)
p12 = ListNode(3)
p13 = ListNode(6)
p11.next = p12
p12.next = p13

p21 = ListNode(2)
p22 = ListNode(4)
p23 = ListNode(5)

p21.next = p22
p22.next = p23

