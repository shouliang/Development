# coding=utf-8
'''
按之字形顺序打印二叉树(分行)：结果放在二维数组中
题目：请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，
即第一行按照从左到右的顺序打印，第二层按照从右到左顺序打印，第三行再按照从左到右的顺序打印，其他以此类推。

思路:
按之字形顺序打印二叉树需要两个栈。我们在打印某一行结点时，把下一层的子结点保存到相应的栈里。
如果当前打印的是奇数层，则先保存左子结点再保存右子结点到一个栈里；如果当前打印的是偶数层，则先保存右子结点再保存左子结点到第二个栈里。

'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, pRoot):
        if not pRoot:
            return []

        resultArray = []                            # 定义最终返回的数组:二维数组
        currentLevelNodes, nextLevelNodes = [], []  # 保存当前节点和下一层节点的栈
        flag = True                                 # 从左往右入栈还是从右往左的标志，交替进行, 刚开始是从左往右
        currentLevelNodes.append(pRoot)             # 首先根节点进入栈

        currentValues = []                          # 当前层所有节点的值
        while currentLevelNodes:
            treeNode = currentLevelNodes.pop()

            currentValues.append(treeNode.val)

            # 从左往右入栈
            if flag:
                if treeNode.left:
                    nextLevelNodes.append(treeNode.left)
                if treeNode.right:
                    nextLevelNodes.append(treeNode.right)
            else:
                if treeNode.right:
                    nextLevelNodes.append(treeNode.right)
                if treeNode.left:
                    nextLevelNodes.append(treeNode.left)

            # 遍历完当前层需要做的工作：1.变换标志 2.遍历下一层: 将下一层的栈赋值给当前层，并清空下一层，以便重新计数 3.将当前层的所有值的数组添加到最终的返回数组中，并清空当前层的值的数组
            if len(currentLevelNodes) == 0:
                flag = not flag                    # 变换标志
                currentLevelNodes = nextLevelNodes # 将下一层赋值给当前层，从而继续遍历当前层
                nextLevelNodes = []                # 清空下一层的节点数，从而重新计数

                resultArray.append(currentValues)
                currentValues = []
        return resultArray


s = Solution()
root = TreeNode(1)
treeNode2 = TreeNode(2)
treeNode3 = TreeNode(3)
root.left = treeNode2
root.right = treeNode3

treeNode4 = TreeNode(4)
treeNode5 = TreeNode(5)
treeNode2.left = treeNode4
treeNode2.right = treeNode5

treeNode6 = TreeNode(6)
treeNode7 = TreeNode(7)
treeNode3.left = treeNode6
treeNode3.right = treeNode7

retData = s.Print(root)

for i in retData:
    print(i)
