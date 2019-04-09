''' 
交换序列中的结点
24. Swap Nodes in Pairs:https://leetcode.com/problems/swap-nodes-in-pairs/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def swapPairs(self, head):
        # pre->a->b->c->…链表，交换a、b节点即把a.next指向c(c=b.next)，b.next指向a，p.next指向b
        pre = self
        pre.next = head
        while pre.next and pre.next.next:
            a = pre.next
            b = pre.next.next

            # 变换指针，a,b互相交换： a.next = b.next,b.next = a ，顺序可不颠倒且是连续的两句
            # 否则会失去b.next,从而a.next指向不了b.next
            # 但是pre.next = b可在前或在后
            a.next = b.next
            b.next = a
            pre.next = b

            # pre指向下一个指针
            pre = a
        return self.next
