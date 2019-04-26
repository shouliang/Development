''' 
链表开始入环的第一个节点
142. Linked List Cycle II:https://leetcode.com/problems/linked-list-cycle-ii/

思路：双指针，设置快慢指针，相遇后，让慢指针回到链表表头，快指针保留在原地，然后快慢指针再同步走，直到相遇则为入环的第一个节点
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                slow = head             # 相遇后，让慢指针回到链表表头，而后再同步
                while slow is not fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
