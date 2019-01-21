''' 
Z字型遍历二叉树
103. Binary Tree Zigzag Level Order Traversal:https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
解释： 
  给定一个二叉树，返回其节点值的锯齿形层次遍历。
  （即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

  例如：
  给定二叉树 [3,9,20,null,null,15,7],

      3
    / \
    9  20
      /  \
    15   7
  返回锯齿形层次遍历如下：

  [
    [3],
    [20,9],
    [15,7]
  ]
'''

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        results = []
        dequeue = []         # 双向队列
        dequeue.append(root)
        while dequeue:
            cur_level = []
            for i in range(len(dequeue)):
                treeNode = dequeue.pop()  # 在双向队列尾部弹出节点的同时，将其左右分支依次插入到双向队列的头部
                cur_level.append(treeNode.val)
                if treeNode.left:
                    dequeue.insert(0, treeNode.left)
                if treeNode.right:
                    dequeue.insert(0, treeNode.right)
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

ret = s.zigzagLevelOrder(root)
print(ret)
