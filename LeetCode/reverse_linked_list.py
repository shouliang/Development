# 单链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 反转链表
class Solution:
    def reverseList(self, head):
        """
        反转链表
        :param head: ListNode
        :return:
        """
        # 初始化当前节点cur指向head, 前一个节点prev指向None
        pre = None
        cur =head

        while cur:
            # tmp保存cur的下一个节点信息
            # 这样保证单链表不会因为失去当前节点的next而断裂
            tmp = cur.next
            # 保存完当前节点的next后，就可以让其next重新指向前一个节点prev
            cur.next = pre
            # 让prev和cur都向后移动一个节点，继续下一次的指针反转
            pre = cur
            cur = tmp
        return pre


# test, 建立链表1->2->3->4->None
head = ListNode(1)
p1 = ListNode(2)
p2 = ListNode(3)
p3 = ListNode(4)
head.next = p1
p1.next = p2
p2.next = p3

s = Solution()
p = s.reverseList(head)
# 输出链表 4->3->2->1->None
while p:
    print(p.val)
    p = p.next
