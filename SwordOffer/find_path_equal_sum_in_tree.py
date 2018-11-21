# -*- coding:utf-8 -*-
'''
输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.resultArray = []

    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if not root:
            return []

        path = []
        currentSum = 0
        self.FindPathCore(root, expectNumber, path, currentSum)
        return self.resultArray

    def FindPathCore(self, pRoot, expectNumber, path, currentSum):
        currentSum += pRoot.val
        path.append(pRoot.val)

        isLeaf = not pRoot.left and not pRoot.right
        if currentSum == expectNumber and isLeaf:
            self.resultArray.append(path[:])

        if pRoot.left:

            self.FindPathCore(pRoot.left, expectNumber, path, currentSum)
        if pRoot.right:

            self.FindPathCore(pRoot.right, expectNumber, path, currentSum)

        path.pop()



root = TreeNode(10)
node1 = TreeNode(5)
node2 = TreeNode(12)
root.left = node1
root.right = node2

node3 = TreeNode(4)
node4 = TreeNode(7)
node1.left = node3
node1.right = node4

s = Solution()
print(s.FindPath(root, 22))
