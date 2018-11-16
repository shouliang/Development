# coding=utf-8
'''
题目描述: 分行按层次打印二叉树：结果放在二维数组中
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。

思路：使用双向队列完成。访问节点将其压入队列，在出队列的同时判断是否有左右子树，有的话将其分别进入队列，直到队列为空

'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []

        resultArray = []      # 定义最终返回的数组：二维数组
        deque = []            # 双向队列

        currentLevelNodes = 1  # 当前层节点数，初始值为根节点，故为1
        nextLevelNodes = 0     # 下一层节点数
        currentValues = []     # 当前层所有节点的值

        # 首先根节点进入队列
        deque.append(pRoot)
        while deque:
            treeNode = deque.pop()  # 利用队列先进先出的特性
            currentLevelNodes -= 1  # 遍历一次当前层节点数减少1

            currentValues.append(treeNode.val)

            if treeNode.left:
                deque.insert(0, treeNode.left)
                nextLevelNodes += 1
            if treeNode.right:
                deque.insert(0, treeNode.right)
                nextLevelNodes += 1

            # 当前层节点数为零则表示遍历完毕，将下一层节点数赋值给当前节点数，以便遍历下一层，同时情况下一层节点数，以便重新计数
            if currentLevelNodes == 0:
                currentLevelNodes = nextLevelNodes
                nextLevelNodes = 0

                resultArray.append(currentValues)
                currentValues = []

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

retData = s.Print(root)

for i in retData:
    print(i)