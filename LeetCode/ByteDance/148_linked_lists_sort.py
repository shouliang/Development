''' 
排序链表
148. Sort List:https://leetcode.com/problems/sort-list/
解释：
    在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

    示例 1:
    输入: 4->2->1->3
    输出: 1->2->3->4

    示例 2:
    输入: -1->5->3->4->0
    输出: -1->0->3->4->5
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 归并排序( 针对链表)


class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        fast, slow = head, head
        while fast.next and fast.next.next:  # 设置一快一慢指针，快指针每次走2步，慢指针每次走1步，到快指针走到链表尾部时，慢指针刚好走到链表中间
            fast = fast.next.next
            slow = slow.next

        # 让链表在中间位置断裂成两个链表，以便后面的递归调用，继续分裂
        mid = slow              # 前半部分链表的尾部
        right_head = slow.next  # 后半部分链表的头部
        mid.next = None         # 让前半部分链表在尾部断裂

        left = self.sortList(head)
        right = self.sortList(right_head)
        return merge(left, right)

# 合并两个有序链表


def merge(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    if l1.val < l2.val:
        temp = l1
        temp.next = merge(l1.next, l2)
        return temp
    else:
        temp = l2
        temp.next = merge(l1, l2.next)
        return temp
