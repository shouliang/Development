# coding=utf-8
'''
题目描述
输入一棵二叉树，判断该二叉树是否是平衡二叉树。平衡二叉树左右分支的高度不超过1
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getDepth(self, Root):
        if Root == None:
            return 0
        leftDepth = self.getDepth(Root.left)
        rightDepth = self.getDepth(Root.right)
        return leftDepth + 1 if leftDepth > rightDepth else rightDepth + 1

    def IsBalanced_Solution(self, node):
        if not node:
            return True
        leftDepth = self.getDepth(node.left)
        rightDepth = self.getDepth(node.right)
        diff = leftDepth - rightDepth
        if diff < -1 or diff > 1:
            return False
        return self.IsBalanced_Solution(node.left) and self.IsBalanced_Solution(node.right)


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
