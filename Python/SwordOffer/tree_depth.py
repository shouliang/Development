# coding=utf-8
'''
题目描述
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        print(pRoot.val)
        leftDepth = self.TreeDepth(pRoot.left)
        rightDepth = self.TreeDepth(pRoot.right)

        depth = leftDepth + 1 if leftDepth > rightDepth else  rightDepth + 1
        print('depth', depth)
        return  depth


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
depth = s.TreeDepth(node1)
print(depth)

