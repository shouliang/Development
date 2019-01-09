'''
简化路径
给定一个文档 (Unix-style) 的完全路径，请进行路径简化。

例如，
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

边界情况:

你是否考虑了 路径 = "/../" 的情况？
在这种情况下，你需返回 "/" 。
此外，路径中也可能包含多个斜杠 '/' ，如 "/home//foo/" 。
在这种情况下，你可忽略多余的斜杠，返回 "/home/foo" 。
'''


class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if not path:
            return None
        p = path.split("/")   # 以“/”进行分割
        stack, res = [], ""
        for s in p:           # 遍历，每个进行单独处理
            # 遇到.或者空字符串,则直接跳过，如：/home//foo/ 以“/”分割后,有空字符串，达到去除多余“/”的目的
            if s == '.' or len(s) == 0:
                continue
            elif s == "..":              # 遇到..则删除它上面挨着的一个路径，即出栈
                if len(stack):
                    stack.pop()
            else:
                stack.append(s)          # 入栈

        if len(stack) == 0:              # 如果是空的话，则直接返回“/”
            return "/"
        for s in stack:                  # 最后以“/”重新组合
            res += "/" + s
        return res

s = Solution()
path = "/home/"
path = s.simplifyPath(path)
print(path)

path = "/a/./b/../../c/"
path = s.simplifyPath(path)
print(path)

path = "/../"
path = s.simplifyPath(path)
print(path)

path = "/home//foo/"
path = s.simplifyPath(path)
print(path)