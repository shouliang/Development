'''
判断链表是否有环
141. Linked List Cycle:https://leetcode.com/problems/linked-list-cycle/
思路 ： 双指针，存在环：则快慢指针肯定相遇，不存在环：快指针能到达表尾
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        slow, fast = head, head.next
        while slow is not fast:
            if fast is None or fast.next is None:
                return False
                
            slow = slow.next
            fast = fast.next.next
        return True
