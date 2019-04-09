# coding=utf-8
'''
题目描述
请实现两个函数，分别用来序列化和反序列化二叉树
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Serialize(self, root):
        if not root:
            return '#'
        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)

    def Deserialize(self, s):
        list = s.split(',')
        return self.DeserializeCore(list)

    def DeserializeCore(self, list):
        if len(list) == 0:
            return None
        val = list.pop(0)
        root = None
        if val != '#':
            root = TreeNode(int(val))
            root.left = self.DeserializeCore(list)
            root.right = self.DeserializeCore(list)
        return root


root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

root.left = node2
root.right = node3

node2.left = node4
node3.left = node5
node3.right = node6

s = Solution()
seria = s.Serialize(root)
print(seria)

tree = s.Deserialize(seria)

print(tree.val)

