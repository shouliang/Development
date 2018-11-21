# coding=utf-8
'''
题目描述: 按层次打印二叉树
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。

思路：使用双向队列完成。访问节点将其压入队列，在出队列的同时判断是否有左右子树，有的话将其分别进入队列，直到队列为空

'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if root == None:
            return []

        retData = []  # 定义最终返回的数组
        deque = []  # 双向队列

        level = 0  # 层数
        levelNum = 1  # 每层节点数

        # 首先根节点进入队列
        deque.append(root)

        while deque:
            treeNode = deque.pop()  # 利用队列先进先出的特性

            retData.insert(0, treeNode.val)  # 在弹出首元素的同时压入这个元素相对应的左右子树

            if treeNode.left:
                deque.insert(0, treeNode.left)

            if treeNode.right:
                deque.insert(0, treeNode.right)

        return retData


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
print()
