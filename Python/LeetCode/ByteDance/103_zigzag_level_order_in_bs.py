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
        result = []
        queue = []          # 队列
        queue.append(root)  # 根节点进入队列
        flag = True
        while queue:
            cur_level = []
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.pop(0) if flag else queue.pop()
                cur_level.append(node.val)
                if flag:                           # 加入队列尾部：left->right，出队列时反而从队列头部开始
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                else:                              # 加入队列头部：right->left, 出队列时反而从队列尾部开始
                    if node.right:
                        queue.insert(0, node.right)
                    if node.left:
                        queue.insert(0, node.left)

            flag = not flag                        # 隔行变换标志
            result.append(cur_level)
        return result


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
