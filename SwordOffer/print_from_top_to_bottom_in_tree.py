# coding=utf-8
'''
题目描述: 不分行按层次打印二叉树: 结果放在一维数组中
从上往下打印出二叉树的每个节点，同层节点从左至右打印

思路：使用双向队列完成。访问节点将其压入队列，在出队列的同时判断是否有左右子树，有的话将其分别进入队列，直到队列为空

'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, pRoot):
        if not pRoot:
            return []

        resultArray = []  # 定义最终返回的数组:一维数组
        deque = []        # 双向队列

        # 首先根节点进入队列
        deque.append(pRoot)

        while deque:
            treeNode = deque.pop()            # 当前节点出队列，而后该节点的左右孩子节点进入队列，直至所有节点都已经出队列，队列为空
            resultArray.append(treeNode.val)

            if treeNode.left:
                deque.insert(0, treeNode.left)
            if treeNode.right:
                deque.insert(0, treeNode.right)

        return resultArray


s = Solution()
root = TreeNode(1)
treeNode1 = TreeNode(2)
treeNode2 = TreeNode(3)
root.left = treeNode1
root.right = treeNode2

treeNode3 = TreeNode(4)
treeNode4 = TreeNode(5)
treeNode1.left = treeNode3
treeNode1.right = treeNode4

retData = s.PrintFromTopToBottom(root)
print(retData)
