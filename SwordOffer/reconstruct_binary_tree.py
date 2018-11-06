'''
题目：
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''


# 重建二叉树

# 思路：
# 设定前序遍历序列为pre，中序遍历序列为mid；
#
# 1、首先我们先从前序遍历序列寻找root节点
#
# 2、递归过程
# +++6
# ①前序遍历序列找到root节点后（pre[0]）
#
# ②我们在中序遍历找到root结点，并记住其位置root_index：
#
# ③如此我们将左子树和右子树分开：
#
# 左子树的前序遍历和中序遍历为：pre[1:root_index+1]和mid[:root_index]
#
# 右子树的前序遍历和中序遍历为：pre[root_index+1:]和mid[root_index+1:]
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 重建二叉树
    def reConstructBinaryTree(self, pre, mid):
        if not pre:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        else:
            root = TreeNode(pre[0])
            root_index = mid.index(pre[0])
            root.left = self.reConstructBinaryTree(pre[1:root_index + 1], mid[:root_index])
            root.right = self.reConstructBinaryTree(pre[root_index + 1:], mid[root_index + 1:])
        return root

    # 打印二叉树
    def PrintTree(self, root):
        if not root:
            return None
        print(root.val)
        self.PrintTree(root.left)
        self.PrintTree(root.right)


s = Solution()
root = s.reConstructBinaryTree([1, 2, 4, 7, 3, 5, 6, 8], [4, 7, 2, 1, 5, 3, 8, 6])
s.PrintTree(root)
