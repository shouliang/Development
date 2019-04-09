# coding=utf-8

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def IsBalanced_Solution(self, pRoot):
        return self.getDepth(pRoot) != -1

    def getDepth(self, node):
        if not node:
            return 0

        left = self.getDepth(node.left)
        right = self.getDepth(node.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1

        return max(left, right) + 1


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

node1.left = node2
node1.right = node3

node2.left = node4
node2.right = node5

node3.right = node6

node5.left = node7

s = Solution()
flag = s.IsBalanced_Solution(node1)
print(flag)
