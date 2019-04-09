'''
有效字母的异位词
242. Valid Anagram:https://leetcode.com/problems/valid-anagram/description/

思路：利用两个哈希表分别记录两个字符串中每个字母的数量，然后再判断这两个哈希表是否相等
'''


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hash_map1, hash_map2 = {}, {}
        for c in s:
            if c not in hash_map1:
                hash_map1[c] = 1
            else:
                hash_map1[c] += 1
        for c in t:
            if c not in hash_map2:
                hash_map2[c] = 1
            else:
                hash_map2[c] += 1

        return hash_map1 == hash_map2

    def isAnagram_01(self, s, t):
        hash_map1, hash_map2 = {}, {}
        for c in s:
            hash_map1[c] = hash_map1.get(c, 0) + 1
        for c in t:
            hash_map2[c] = hash_map2.get(c, 0) + 1

        return hash_map1 == hash_map2

    def isAnagram_02(self, s, t):
        hash_map1, hash_map2 = [0] * 26, [0] * 26
        for c in s:
            hash_map1[ord(c) - ord('a')] += 1
        for c in t:
            hash_map2[ord(c) - ord('a')] += 1

        return hash_map1 == hash_map2


s = 'abcd'
t = 'bdca'

solution = Solution()
flag = solution.isAnagram(s, t)
print(flag)

flag = solution.isAnagram_01(s, t)
print(flag)

flag = solution.isAnagram_02(s, t)
print(flag)
