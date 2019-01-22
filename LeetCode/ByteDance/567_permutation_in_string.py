'''
字符串的排列
567. Permutation in String:https://leetcode.com/problems/permutation-in-string/

思路:滑动窗口 
    其实不需要找到s1的全排列，因为我们只需要考虑s2中是否包含s1中同样个数的字符，
    并且这些字符是连在一起的就行了。因此，我们可以使用一个滑动窗口，在s2上滑动。
    在这个滑动窗口中的字符及其个数是否刚好等于s1中的字符及其个数，此外滑动窗口保证了这些字符是连在一起的。
'''


class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        hash_map1 = dict()                               # hash_map1记录s1中的字符情况
        for c in s1:
            hash_map1[c] = hash_map1.get(c, 0) + 1

        i, j = 0, 0
        hash_map2 = dict()        # 用i,j两个指针指向滑动窗口的左边界和右边界
        while j < len(s2):
            if j - i < len(s1):   # 当i和j的间距小于s1的长度时，j向后移动
                hash_map2[s2[j]] = hash_map2.get(s2[j], 0) + 1
                j = j + 1
            else:
                if hash_map1 == hash_map2:      # 滑动窗口大小等于s1的长度时，判断是hash_map1是否相等
                    return True                 # 若相等则直接返回True,不相等则移除i加入j 
                else:
                    hash_map2[s2[i]] = hash_map2[s2[i]] - 1
                    if hash_map2[s2[i]] == 0:
                        del hash_map2[s2[i]]

                    hash_map2[s2[j]] = hash_map2.get(s2[j], 0) + 1
                    i += 1
                    j += 1

        return hash_map1 == hash_map2  # 处理完i和j之后最后判断hash_map1 == hash_map2是否相等


solution = Solution()

s1 = "ab"
s2 = "eidbaooo"
flag = solution.checkInclusion(s1, s2)
print(flag)
