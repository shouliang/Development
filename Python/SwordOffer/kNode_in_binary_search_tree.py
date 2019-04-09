'''
题目描述
给定一棵二叉搜索树，请找出其中的第k小的结点。例如，（5，3，7，2，4，6，8） 中，
按结点数值大小顺序第三小结点的值为4。

思路：中序遍历二叉搜索树，即按照从小到大的顺序搜索，其中第k个元素即第k小的节点
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if not pRoot or not k:
            return None
        res = []
        self.InOrder(pRoot, res)
        if len(res) < k:
            return None
        return res[k - 1]

    def InOrder(self, pRoot, res):
        if not pRoot: return
        if pRoot.left:
            self.InOrder(pRoot.left, res)
        res.append(pRoot)
        if pRoot.right:
            self.InOrder(pRoot.right, res)


p5 = TreeNode(5)
p3 = TreeNode(3)
p7 = TreeNode(7)
p5.left = p3
p5.right = p7

p2 = TreeNode(2)
p4 = TreeNode(4)
p3.left = p2
p3.right = p4

p6 = TreeNode(6)
p8 = TreeNode(8)
p7.left = p6
p7.right = p8

s = Solution()
kNode = s.KthNode(p5, 4)
if kNode:
    print(kNode.val)
