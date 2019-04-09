# coding=utf-8
'''
要查找树A中是否存在和树B结构一样的子树，可以分成两步：

第一步在树A中找到和B的根节点的值一样的结点R；
第二步再判断树A中以R为根结点的子树是不是包含和树B一样的结构。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if pRoot1 == None or pRoot2 == None:
            return False

        result = False
        # 首先判断根节点是否相等，相等则判断以此节点为根节点的是否包含一样的节点
        # 不相等则先搜索左子树，不相等后再搜索右子树
        if pRoot1.val == pRoot2.val:
            result = self.DoesTree1HaveTree2(pRoot1, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.left, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right, pRoot2)
        return result

    def DoesTree1HaveTree2(self, pRoot1, pRoot2):
        if pRoot2 == None:  # Tree2的叶子节点，则遍历结束
            return True
        if pRoot1 == None:  # Tree1的叶子节点，则Tree1遍历结束，返回False
            return False
        if pRoot1.val != pRoot2.val:  # 比较相应的值是否相等，不相等则返回False
            return False

        # 递归比较左子树和右子树，全部相等则子树相等
        return self.DoesTree1HaveTree2(pRoot1.left, pRoot2.left) and \
               self.DoesTree1HaveTree2(pRoot1.right, pRoot2.right)
