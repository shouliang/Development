# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        stackA, stackB = [], []
        while headA:
            stackA.append(headA.val)
            headA = headA.next
        while headB:
            stackB.append(headB.val)
            headB = headB.next
        
        while stackA and stackB and :
            valueA = stackA.pop()
            valueB = stackB.pop()
            if valueA == valueB:
                stackA
