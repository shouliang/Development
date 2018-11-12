# coding=utf-8
'''
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。

思路：（设二叉树左子树为，右子树为root2，root1、root2均指向左右子树的根）
递归：root1和root2的值相等，并且root1的左子树与root2的右子树对称，root1的右子树与root2的左子树对称

'''


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetrical(self, pRoot):
        if pRoot == None:  # 空树是对称的
            return True
        return self.isSymmetircalInTwoTree(pRoot, pRoot)

    # 判断两棵树是否对称
    def isSymmetircalInTwoTree(self, pRoot1, pRoot2):
        if pRoot1 == None and pRoot2 == None:  # 两棵树同时全部遍历完毕，返回True
            return True
        if pRoot1 == None or pRoot2 == None:   # 一颗遍历完毕，一颗未遍历完毕，则肯定不对称，返回False
            return False

        # 树root1和树root2对称的条件：root1和root2的值相同，并且root1的左子树与root2的右子树对称，root1的右子树与root2的左子树对称
        return pRoot1.val == pRoot2.val and self.isSymmetircalInTwoTree(pRoot1.left, pRoot2.right) and \
               self.isSymmetircalInTwoTree(pRoot1.right, pRoot2.left)
