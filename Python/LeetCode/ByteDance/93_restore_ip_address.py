''' 
复原IP
93. Restore IP Addresses:https://leetcode.com/problems/restore-ip-addresses/
'''

# 思路： DFS + backtracking （深度遍历 + 回溯）
class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 4 or len(s) > 12:  # 处理非法情况
            return []
        path, result = [], []       # 初始化其中的一个路径和最终的路径集合
        dfs(s, 0, path, result)     # DFS
        return result


def dfs(s, start, path, result):
    if len(path) == 4 and start == len(s):  # 递归终止判断
        result.append(".".join(path))
        return
    for i in range(1, 4):        # 截取从start开始的1-3个字符串，类似于图遍历时，遍历所有相邻的顶点
        if start + i <= len(s):  # 判断下标是否越界
            number = s[start:start + i]  # 截取字符串
            if isValid(number):          # 判断字符串是否是合法的IP
                path.append(number)      # 加入path
                dfs(s, start + i, path, result)  # DFS start的第i个，即第1、2、3个
                path.pop()                        # 回溯


# 判断字符串s，是否为合法的数字:
# 字符串转换为整数形式的字符串，如果还是等于原来的字符串本身，且字符串的整数形式要小于等于255
# 这样避免了: 00,000,01,012,256等非法形式的字符串
def isValid(s):
    if str(int(s)) == s and int(s) <= 255:
        return True
    return False


s = "25525511135"
# s = "010010"

solution = Solution()
res = solution.restoreIpAddresses(s)
print(res)
