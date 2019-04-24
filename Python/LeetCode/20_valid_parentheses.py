''' 
验证有效括号对
20. Valid Parentheses:https://leetcode.com/problems/valid-parentheses/
'''


class Solution(object):
    def isValid(self, s):
        if not s:
            return True
        stack = []
        hash_map = {')': '(', ']': '[', '}': '{'}

        # 循环字符串如若遇到左括号：'(' or '[' or '{'则压入栈内
        # 否则就是右括号，需要和栈顶元素比较，如果匹配则出栈直到栈为空，否则就是不匹配
        for c in s:
            if c not in hash_map:
                stack.append(c)                           # 压入左括号
            elif not stack or stack.pop() != hash_map[c]: # 根据右括号从hash_map获取左括号 并和 栈顶的左括号比较
                return False
        return not stack


s = Solution()
print(s.isValid('{}'))
print(s.isValid('()[]{}'))
print(s.isValid('(]'))
print(s.isValid('([)]'))
print(s.isValid('{[]}'))
print(s.isValid(''))
