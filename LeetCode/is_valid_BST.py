# 验证是否是二叉搜索树
# 何为二叉搜索树：在树中的任意一个节点，其左子树中的每个节点的值，都要小于这个节点的值，而右子树中的每个结点的值，都要大于这个节点的值
# 思路：中序遍历二叉树后，则已排序好，但此处可通过比较当前节点和前驱节点的大小来判定
# https://leetcode.com/problems/validate-binary-search-tree/
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.prev = None
        return self.helper(root)

    def helper(self, root):
        if root is None:               # 根节点为空，则直接判定为是二叉搜索树
            return True

        # 中序遍历
        if not self.helper(root.left): # 遍历左子树
            return False
        if self.prev and self.prev.val >= root.val:  # 遍历当前节点：比较当前驱节点和当前节点的数值大小
            return False
        self.prev = root                             # 遍历右子树：遍历之前将当前节点赋值给前驱节点
        return self.helper(root.right)