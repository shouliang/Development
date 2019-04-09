''' 
无重复字符的最长子串
3. Longest Substring Without Repeating Characters:https://leetcode.com/problems/longest-substring-without-repeating-characters/
思路：
    假设子串的初始下标为 i，结束下标为 j。i 和 j 的初始值均为 0。j 开始一次往后遍历，如果这个字符串没有重复字符，
    那么 j 会一直走到最后，此时最长子串就是字符串本身。实际情况没有那么理想，我们主要分析这类场景。
    当处于 j 位置的字符和子串之前的字符重复（假设位置为 k），那么就应该停下，并且更新最长子串的长度（假设最长长度为 max），
    j 继续往后走，同时 i 的位置需要挪到重复字符之后，即 k+1 处。直到遍历到字符串的最后
'''


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        longest = 0
        i = 0
        hash_map = dict()
        for j in range(len(s)):
            if s[j] in hash_map and hash_map[s[j]] + 1 > i:  # try to extend the range[i,j]
                # hash_map[s[j]] + 1 确定重新出现的字符在窗口内
                i = hash_map[s[j]] + 1

            hash_map[s[j]] = j
            longest = longest if longest > j - i + 1 else j - i + 1  # 每次更新最长子串的长度

        return longest

# s = 'abc'
# print('a' in s)


s = 'abcabcbb'
s = 'bbbbb'
s = 'pwwkew'
s = 'dvdf'
s = 'tmmzuxt'
solution = Solution()
od = solution.lengthOfLongestSubstring(s)
print(od)  # get the last key)

# import collections
# od = collections.OrderedDict([('p', 1), ('pw', 2), ('wk', 2), ('wke', 3)])
# print(next(reversed(od.items())) # get the last item)
