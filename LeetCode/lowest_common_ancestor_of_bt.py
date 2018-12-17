'''
二叉树的最近公共祖先

思路：
自底向上遍历结点，一旦遇到结点等于p或者q，则将其向上传递给它的父结点。
父结点会判断它的左右子树是否都包含其中一个结点，如果是，则父结点一定是这两个节点p和q的最近公共祖先，传递父结点到root。
如果不是，我们向上传递其中的包含结点p或者q的子结点，或者NULL(如果子结点不包含任何一个)。该方法时间复杂度为O(N)。
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return  left if left else right