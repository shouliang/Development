'''
160. Intersection of Two Linked Lists: https://leetcode.com/problems/intersection-of-two-linked-lists/

思路1：把a、b链表弄成等长，然后一起遍历，最先相等的结点就是交点。    
思路2：双指针法：   
            ListB + ListA = Bb + intersection + A + intersection
            用大A表示ListA里面非共有 Bb表示listB里面非共有的，可以看到在第二个intersection的开头两个链表长度是一样的，必然相等
            所以我们可以遍历A再遍历B，另一个遍历B再遍历A，两个指针必定在第二个交集处相遇，没有交集就是空指针
'''
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
        pa, pb = headA, headB
        while pa != pb:
            if not pa:
                pa = headB
            else:
                pa = pa.next
            if not pb:
                pb = headA
            else:
                pb = pb.next
        return pa
