# coding=utf-8
'''
题目描述
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
'''


class Solution:
    def IsPopOrder(self, pushV, popV):
        stack = []  # 辅助栈

        # 遍历输入栈，比较输入栈栈顶元素和弹出栈的首元素，相等则输入栈弹出和弹出栈弹出首元素，若辅助栈为空则满足，否则不满足
        for pushValue in pushV:
            stack.append(pushValue)

            while stack:
                if stack[-1] == popV[0]:
                    stack.pop()
                    popV.pop(0)
                else:
                    break

        return not stack

s = Solution()

pushV = [1,2,3,4,5]
popV1 = [4,5,3,2,1]

flag = s.IsPopOrder(pushV,popV1)
print(flag)








