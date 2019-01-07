import math


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest, i, j = 0, 0, 0
        charSet = set()
        while i < len(s) and j < len(s):
            # try to extend the range [i, j]
            if s[j] not in charSet:
                charSet.add(s[j])
                j = j + 1
                longest = longest if longest > (j - i) else j - i
            else:
                charSet.remove(s[i])
                i = i + 1


s = "abcabcbb"
# s = " "

solution = Solution()
longest = solution.lengthOfLongestSubstring(s)
print(longest)
