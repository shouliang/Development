class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        return longestCommonPrefix_helper(strs, 0, len(strs) - 1)

# 分治法


def longestCommonPrefix_helper(strs, low, high):
    if low == high:                # 递归的终止条件,后面的嵌套递归会一直分一直分，直到low = high，即某一个字符串，开始返回，计算公共前缀
        return strs[low]           # 返回字符串

    # 数组分半
    mid = low + (high - low) // 2

    # 嵌套调用
    str_left = longestCommonPrefix_helper(strs, low, mid)
    str_right = longestCommonPrefix_helper(strs, mid+1, high)

    # 计算两个字符串的公共前缀
    return commonPrefix(str_left, str_right)

# 计算两个字符串的公共前缀


def commonPrefix(str_left, str_right):
    minLen = min(len(str_left), len(str_right))

    # 只循环短的字符串，逐个进行比较，遇到不相等则直接返回，否则返回短的字符串
    for i in range(minLen):
        while str_left[i] != str_right[i]:
            return str_left[:i]
    return str_left[:minLen]


s = Solution()

strs = ["flower", "flow", "flight"]
lcp = s.longestCommonPrefix(strs)
print(lcp)

strs = ["dog", "racecar", "car"]
lcp = s.longestCommonPrefix(strs)
print(lcp)
