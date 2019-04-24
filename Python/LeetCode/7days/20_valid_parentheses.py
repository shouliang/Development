''' 
验证有效括号对
20. Valid Parentheses:https://leetcode.com/problems/valid-parentheses/
'''


class Solution(object):
    def isValid(self, s):
        if not s:
            return True 
        stack = []
        hash_map= {')':'(',']':'[','}':'{',}
        for c in s:
            if c not in hash_map:
                stack.append(c)
            elif not stack or stack.pop()!= hash_map[c]:
                return False
        return not stack 


s = Solution()
print(s.isValid('{}'))
print(s.isValid('()[]{}'))
print(s.isValid('(]'))
print(s.isValid('([)]'))
print(s.isValid('{[]}'))
print(s.isValid(''))
