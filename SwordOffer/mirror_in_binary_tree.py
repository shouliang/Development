# coding=utf-8
'''
二叉树的镜像

思路：前序遍历，交换非叶子节点的左右节点
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if root == None:  # 节点为空则直接返回
            return
        if root.left == None and root.right == None:  # 遍历到叶子节点则终止,递归的终止条件写在前面
            return

        # 交换根节点左右子树
        temp = root.left
        root.left = root.right
        root.right = temp

        # 递归左右子树
        self.Mirror(root.left)
        self.Mirror(root.right)


root = TreeNode(8)
treeNode1 = TreeNode(6)
treeNode2 = TreeNode(10)

root.left = treeNode1
root.right = treeNode2

s = Solution()
s.Mirror(root)

print()
