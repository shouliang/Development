'''
二叉树按层次遍历
102. Binary Tree Level Order Traversal:https://leetcode.com/problems/binary-tree-level-order-traversal/

思路： 使用双向队列这种数据结构：首先根节点进入双向队列，然后在双向队列尾部弹出节点的同时，将其左右分支依次插入到双向队列的头部，
      直至双向队列为空

'''

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        results, dequeue = [], []   # 双向队列
        dequeue.append(root)        # 根节点进入双向队列
        while dequeue:
            level_size = len(dequeue)
            cur_level = []
            for _ in range(level_size):
                node = dequeue.pop()  # 在双向队列尾部弹出节点的同时，将其左右分支依次插入到双向队列的头部
                cur_level.append(node.val)
                if node.left:
                    dequeue.insert(0, node.left)
                if node.right:
                    dequeue.insert(0, node.right)

            results.append(cur_level)
        return results


s = Solution()
root = TreeNode(3)
treeNode1 = TreeNode(9)
treeNode2 = TreeNode(20)
root.left = treeNode1
root.right = treeNode2

treeNode3 = TreeNode(15)
treeNode4 = TreeNode(7)
treeNode2.left = treeNode3
treeNode2.right = treeNode4

ret = s.levelOrder(root)
print(ret)
