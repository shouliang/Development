# -*- coding:utf-8 -*-
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
            newPath = path[:]
            self.resultArray.append(newPath)

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
