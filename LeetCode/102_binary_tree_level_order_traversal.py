'''
二叉树按层次遍历
102. Binary Tree Level Order Traversal:https://leetcode.com/problems/binary-tree-level-order-traversal/

思路： 使用队列这种数据结构：首先根节点进入队列，然后在队列头部弹出节点的同时，将其左右分支依次插入队列的尾部，
      直至队列为空
      其实这就是图的bfs，但是二叉树就是一种特殊的图
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
        result = []
        queue = []          # 队列
        queue.append(root)  # 根节点进入队列

        while queue:
            cur_level = []
            level_size = len(queue)
            for _ in range(level_size):   # 遍历当前层，处理完当前层，再将当前层的一维数组加入到二维结果中
                node = queue.pop(0)       # 在队列头部弹出节点的同时，将其左右分支依次append()到队列的尾部
                cur_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(cur_level)

        return result


class Solution2(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        queue = []          # 队列
        queue.append(root)  # 根节点进入队列

        while queue:
            node = queue.pop(0)       # 在队列头部弹出节点的同时，将其左右分支依次append()到队列的尾部
            result.append(node.val)   # 处理结点，访问其相邻的节点并进入队列
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
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

ret = s.levelOrder(root)
print(ret)

s2 = Solution2()
ret = s2.levelOrder(root)
print(ret)
