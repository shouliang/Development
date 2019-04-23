'''
合并两个有序链表
21. Merge Two Sorted Lists:https://leetcode.com/problems/merge-two-sorted-lists/
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

思路分析：
我们拿到题目首先注意到的是，有序，并且这两个链表的长度是不定的，
所以有可能出现的情况是：一个链表为空，另外一个链表是4个长度。这些细节我们在分析问题的时候都需要考虑到。

既然是有序链表，我们就需要比较两个数值的大小来决定谁排在前面。
我们可以吧这个问题当成数组的问题，那么我们就需要重新设定一个新的数组，然后遍历这两个有序数组，然后小的存进新的数组。

而在链表中，我们需要先设定一个头结点，然后就相当于是定义了一个新的链表。
我们把值一个一个往里面装就可以了，最后需要考虑的问题的是：链表的长度不一致的时候，
我们需要把我们的新的链表指向还不为空的那个链表。
参考：https://zhuanlan.zhihu.com/p/39274660

示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

