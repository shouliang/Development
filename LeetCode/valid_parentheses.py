class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        stack = []
        hash_map = {')': '(', ']': '[', '}': '{'}

        # 循环字符串如若遇到左括号：'(' or '[' or '{'则压入栈内
        # 否则就是右括号，需要和栈顶元素比较，如果匹配则出栈直到栈为空，否则就是不匹配
        for c in s:
            if c not in hash_map:
                stack.append(c)
            elif not stack or hash_map[c] != stack.pop():
                 return False
        return not stack


s = Solution()
print(s.isValid('{}'))
print(s.isValid('()[]{}'))
print(s.isValid('(]'))
print(s.isValid('([)]'))
print(s.isValid('{[]}'))
print(s.isValid(''))

