'''
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''


# coding=utf-8
# 单链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 返回合并后列表
class Solution:
    # 递归版本
    def Merge(self, pHead1, pHead2):
        # 判断pHead1和pHead2是否为空
        if pHead1 == None:
            return pHead2
        if pHead2 == None:
            return pHead1

        pMergedHead = self

        # 确定新的表头，下一个节点通过递归来实现
        if pHead1.val < pHead2.val:
            pMergedHead = pHead1
            pMergedHead.next = self.Merge(pHead1.next, pHead2)
        else:
            pMergedHead = pHead2
            pMergedHead.next = self.Merge(pHead1, pHead2.next)

        return pMergedHead

    # 非递归版本
    def Merge2(self, pHead1, pHead2):
        # 判断pHead1和pHead2是否为空
        if pHead1 == None:
            return pHead2
        if pHead2 == None:
            return pHead1

        # 确定合并后的链表的表头
        pMergedHead = self
        if pHead1.val < pHead2.val:
            pMergedHead = pHead1
            pHead1 = pHead1.next
        else:
            pMergedHead = pHead2
            pHead2 = pHead2.next

        # 新声明一个指针指向合并后的链表的表头
        pCurrent = pMergedHead
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                pCurrent.next = pHead1
                pHead1 = pHead1.next
            else:
                pCurrent.next = pHead2
                pHead2 = pHead2.next

            pCurrent = pCurrent.next

        # pHead1或者pHead2不为空，则直接接到新链表的尾部
        if pHead1:
            pCurrent.next = pHead1
        if pHead2:
            pCurrent.next = pHead2

        return pMergedHead


p11 = ListNode(1)
p12 = ListNode(3)
p13 = ListNode(6)
p11.next = p12
p12.next = p13

p21 = ListNode(2)
p22 = ListNode(4)
p23 = ListNode(5)
p24 = ListNode(8)

p21.next = p22
p22.next = p23
p23.next = p24

s = Solution()
pMerged = s.Merge(p11, p21)
#pMerged2 = s.Merge2(p11, p21)

while pMerged:
    print(pMerged.val)
    pMerged = pMerged.next
