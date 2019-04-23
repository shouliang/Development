''' 
合并k个有序链表
23. Merge k Sorted Lists:https://leetcode.com/problems/merge-k-sorted-lists/
思路：
    这道题让我们合并k个有序链表，之前我们做过一道Merge Two Sorted Lists 混合插入有序链表，是混合插入两个有序链表。
    这道题增加了难度，变成合并k个有序链表了，但是不管合并几个，基本还是要两两合并。
    那么我们首先考虑的方法是能不能利用之前那道题的解法来解答此题。
    答案是肯定的，但是需要修改，怎么修改呢，最先想到的就是两两合并，就是前两个先合并，合并好了再跟第三个，然后第四个直到第k个。
    这样的思路是对的，但是效率不高，没法通过OJ，
    所以我们只能换一种思路，这里就需要用到分治法 Divide and Conquer Approach。
    简单来说就是不停的对半划分，比如k个链表先划分为合并两个k/2个链表的任务，再不停的往下划分，
    直到划分成只有一个链表的任务，开始合并。
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return []
        return self.partition(lists, 0, len(lists) - 1)

    def partition(self, lists, low, high):
        if low == high:
            return lists[low]  # 当low == high时,递归终止条件，返回lists[low]

        # 将列表分成两半
        mid = low + (high - low) // 2

        # 递归调用，继续分半
        left = self.partition(lists, low, mid)
        right = self.partition(lists, mid + 1, high)

        # 合并有序链表
        return self.merge(left, right)

    # 合并有序链表
    def merge(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val < l2.val:
            l1.next = self.merge(l1.next, l2)  # 递归调用
            return l1
        else:
            l2.next = self.merge(l1, l2.next)
            return l2


l11 = ListNode(1)
l12 = ListNode(30)
l11.next = l12

l21 = ListNode(2)
l22 = ListNode(5)
l23 = ListNode(9)
l24 = ListNode(45)
l21.next = l22
l22.next = l23
l23.next = l24

l31 = ListNode(16)
l32 = ListNode(22)
l33 = ListNode(56)
l31.next = l32
l32.next = l33

lists = [l11, l21, l31]

s = Solution()
merged = s.mergeKLists(lists)

while merged:
    print(merged.val)
    merged = merged.next
