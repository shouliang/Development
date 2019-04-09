'''
题目描述：
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5

思路：
要删除有序链表中所有的重复节点，而头结点有可能就是重复节点。这样的比较好的解决方式就是新建头结点，然后往后遍历，同样的值就全部略过。
'''

# coding=utf-8
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplication(self, pHead):
        if not pHead or not pHead.next:
            return pHead

        # 初始化前指针pre和当前指针cur
        pre = self
        pre.next = pHead
        cur = pHead

        # 保存pre到临时变量temp
        temp = pre

        while cur and cur.next:
            # 判断cur和cur.next的val是否相等，相等还需判断后续还有重复的元素，让pre.next指向最终的cur
            # 否则后移pre和cur
            if cur.val == cur.next.val:
                val = cur.val
                # 判断后续是否还有重复的元素
                while cur and cur.val == val:
                    cur = cur.next
                # 让pre.next指向最终的cur
                pre.next = cur
            else:
                pre = cur
                cur = cur.next

        return temp.next

s = Solution()

p1 = ListNode(1)
p2 = ListNode(2)
p3 = ListNode(3)
p4 = ListNode(3)
p5 = ListNode(4)
p6 = ListNode(4)
p7 = ListNode(5)

p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5
p5.next = p6
p6.next = p7

pHead = s.deleteDuplication(p1)

while pHead:
    print(pHead.val)
    pHead = pHead.next

print('----------')

p1 = ListNode(1)
p2 = ListNode(1)
p3 = ListNode(1)
p4 = ListNode(1)
p5 = ListNode(1)
p6 = ListNode(1)
p7 = ListNode(2)

p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5
p5.next = p6
p6.next = p7

pHead = s.deleteDuplication(p1)

while pHead:
    print(pHead.val)
    pHead = pHead.next

# print(s.deleteDuplication(None))
#
# p = ListNode(10)
# while p:
#     print(p.val)
#     p = p.next
