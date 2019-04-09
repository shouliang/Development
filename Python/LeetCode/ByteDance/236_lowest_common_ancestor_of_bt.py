'''
二叉树的最近公共祖先
236. Lowest Common Ancestor of a Binary Tree:https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
思路：
    自底向上遍历结点，一旦遇到结点等于p或者q，则将其向上传递给它的父结点。
    父结点会判断它的左右子树是否都包含其中一个结点，如果是，则父结点一定是这两个节点p和q的最近公共祖先，传递父结点到root。
    如果不是，我们向上传递其中的包含结点p或者q的子结点，或者NULL(如果子结点不包含任何一个)。该方法时间复杂度为O(N)。

思路另解释：
    这时我们先试着用穷举法来找到所有可能的情况，现在已知根节点root和两个需要查找父节点的节点p,q
    p, q分别位于root的左子树和右子树： root为最低共同父节点
    p, q均位于root的左子树: 继续在root.left寻找最低共同父节点
    p, q均为与root的右子树: 继续在root.right寻找最低共同父节点
    root==p：最低共同父节点为p或p的某个父节点
    root==q：最低共同父节点为q或q的某个父节点
    我们再进行汇总，如果我们在向下遍历左子树和右子树的过程中，一旦遇到p或q，则返回p或q，
    因为继续往下遍历的值都不会是p和q的共同父节点。
    如果左右子树返回的最低共同父节点值都不是空，说明p和q分别位于root的左右子树，
    那么root就是最低共同父节点。如果两个都为空，说明当前根节点不包含p和q。
    如果其中一棵子树返回的值不为空，那么就说明p和q都位于那棵子树上，
    且返回的值就是遍历过程中最先遇到的p或者q，也就是最低共同父节点。

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
        return left if left else right
