# coding=utf-8
'''
题目描述
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
'''


class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False

            # 获取根节点
        root = sequence[-1]

        # 根据二叉搜索树的性质，左孩子的每个结点的值都小于根节点
        i = 0
        for i in range(len(sequence)):
            if sequence[i] > root:
                break

        # 判断是否右孩子的每个结点的值都大于根结点
        for j in range(i, len(sequence)):
            if sequence[j] < root:
                return False

        left = True
        # i > 0 的时候证明有左孩子
        if i > 0:
            # 递归遍历左孩子
            left = self.VerifySquenceOfBST(sequence[: i])

        right = True
        # 证明有右孩子，通过i的值不在最后一个结点判断，len(sequence) - 1 为sequence的最后一个结点
        if i < len(sequence) - 1:
            right = self.VerifySquenceOfBST(sequence[i: -1])

        return left and right


sequence = [5, 7, 6, 9, 11, 10, 8]
#sequence = [7, 4, 6, 5]

s = Solution()
flag = s.VerifySquenceOfBST(sequence)
print(flag)
