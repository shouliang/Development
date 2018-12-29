# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists: return []
        return self.partition(lists, 0, len(lists) - 1)

    def partition(self, lists, low, high):
        if low == high: return lists[low]  # 当low == high时,递归终止条件，返回lists[low]

        # 将列表分成两半
        mid = low + (high - low) // 2

        # 递归调用，继续分半
        left = self.partition(lists, low, mid)
        right = self.partition(lists, mid + 1, high)

        # 合并有序链表
        return self.merge(left, right)

    # 合并有序链表
    def merge(self, left, right):
        if not left: return right
        if not right: return left

        if left.val < right.val:
            temp = left
            temp.next = self.merge(left.next, right)  # 递归调用
            return temp
        else:
            temp = right
            temp.next = self.merge(left, right.next)
            return temp


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
l32.next =l33

lists = [l11,l21,l31]

s = Solution()
merged = s.mergeKLists(lists)

while merged:
    print(merged.val)
    merged = merged.next


