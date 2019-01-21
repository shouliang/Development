''' 
求两数之和
2. Add Two Numbers:https://leetcode.com/problems/add-two-numbers/
'''
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        p3 = ListNode(0)
        temp = p3
        isCarry = False      # 是否有进位的标志
        while p1 or p2:      # 循环遍历p1 和 p2
            val = 0          # 将p1.val + p2.val 相加，并判断是否有进位，若有进位，下一次结果要加上1
            if p1:
                val += p1.val
                p1 = p1.next
            if p2:
                val += p2.val
                p2 = p2.next
            if isCarry:
                val += 1

            if val < 10:
                p3.next = ListNode(val)
                isCarry = False               # 无进位，需将进位标志再次标记为False
            else:
                p3.next = ListNode(val % 10)
                isCarry = True
            p3 = p3.next

        if isCarry:  # 此处是判断最后一位是否有进位，有进位则还需要新加一个值为1的节点
            p3.next = ListNode(1)

        return temp.next

# 改进版


class Solution2:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        p3 = ListNode(0)
        temp = p3            # 临时变量保存p3的头部
        carry = 0
        while p1 or p2:      # 循环遍历p1 和 p2
            val = 0          # 将p1.val + p2.val 相加，并判断是否有进位，若有进位，下一次结果要加上1
            if p1:
                val += p1.val
                p1 = p1.next
            if p2:
                val += p2.val
                p2 = p2.next
            val += carry
            carry = val // 10            # 通过整除来判断是否有进位
            p3.next = ListNode(val % 10)  # 通过求余来求值
            p3 = p3.next

        if carry:  # 此处是判断最后一位是否有进位，有进位则还需要新加一个值为1的节点
            p3.next = ListNode(1)

        return temp.next  # 只返回p3.next，从而不包括p3初始化的值
# #[   2,4,3]
# l1 = ListNode(2)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)


# # [5,6,4]
# l2 = ListNode(5)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)
l1 = ListNode(5)
l2 = ListNode(5)

s = Solution()
p = s.addTwoNumbers(l1, l2)
while p:
    print(p.val)
    p = p.next
