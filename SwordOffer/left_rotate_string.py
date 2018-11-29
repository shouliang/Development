class Solution:
    def LeftRotateString(self, s, n):
        if not s:
            return ''
        s = list(s)
        # 翻转三次
        self.Reverse(s, 0, n - 1)
        self.Reverse(s, n, len(s) - 1)
        self.Reverse(s, 0, len(s) - 1)
        return ''.join(s)

    def Reverse(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1


s, n = 'abcXYZdef', 3
solution = Solution()
print(solution.LeftRotateString(s, n))
