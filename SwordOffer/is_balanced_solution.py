# coding=utf-8

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        depth = 0
        return self.IsBalancedCore(pRoot, depth)

    def IsBalancedCore(self, pRoot, depth):
        if not pRoot:
            return True

        leftDepth = [0]
        rightDepth = [0]
        if self.IsBalancedCore(pRoot.left, leftDepth) and self.IsBalancedCore(pRoot.right, rightDepth):
            diff = leftDepth[0] - rightDepth[0]
            if diff <= 1 and diff >= -1:
                depth = leftDepth[0] + 1 if leftDepth[0] > rightDepth[0] else rightDepth[0] + 1
                return True

        return False

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