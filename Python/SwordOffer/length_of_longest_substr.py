class Solution():
    def LengthOfLongestSubstring(self, s):
        if not s:
            return ''
        # 字典存储字符下标
        str_dict = {}
        max_len = 0
        one_max = 0
        start = 0

        for i in range(len(s)):
            # 遇到重复的字符，将起始位置向后挪动1个
            if s[i] in str_dict and str_dict[s[i]] >= start:
                start = str_dict[s[i]] + 1

            # 计算单次无重复字符串的长度
            one_max = i - start + 1

            # 更新字符的下标为当前位置
            str_dict[s[i]] = i

            max_len = max(max_len, one_max)
        return max_len


s = 'arabcacfr'
s= 'aaaa'
s = 'abcdefg'
solution = Solution()
longestLen = solution.LengthOfLongestSubstring(s)
print(longestLen)
