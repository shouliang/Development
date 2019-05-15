class Solution:
    def lengthOfLongestSubString(self, s):
        if not s:
            return 0
        longest, i, hash_map = 0, 0, dict()
        for j in range(len(s)):
            if s[j]in hash_map and hash_map[s[j]] + 1 > i:
                i = hash_map[s[j]] + 1
            hash_map[s[j]] = j
            longest = max(longest, j-i+1)
        return longest

    def lengthOfLongestSubString_01(self, s):
        if not s:
            return 0
        longest, i, hash_map = 0, 0, dict()
        for j in range(len(s)):
            if s[j] in hash_map and hash_map[s[j]] + 1 > i:
                i = hash_map[s[j]] + 1
            hash_map[s[j]] = j
            longest = max(longest, j-i+1)
        return longest

    def lenghtofLongestSubString_02(self, s):
        if not s:
            return 0
        longest, i, hash_map = 0, 0, dict()
        for j in range(len(s)):
            if s[j] in hash_map and hash_map[s[j]] + 1 > i:
                i = hash_map[s[j]] + 1
            hash_map[s[j]] = j
            longest = max(longest, j-i+1)
        return longest

    def simplifyPath(self, path):
        if not path:
            return None
        p = path.split("/")
        stack, res = [], ""
        for s in p:
            if s == '.' or len(s) == 0:
                continue
            elif s == "..":
                if len(stack):
                    stack.pop()
            else:
                stack.append(s)

        if len(stack) == 0:
            return "/"
        for s in stack:
            res += "/" + s
        return res

    def simplifyPath_01(self, path):
        if not path:
            return None
        p = path.split("/")
        stack, res = [], ""
        for s in p:
            if s == "." or len(s) == 0:
                continue
            elif s == "..":
                if len(stack):
                    stack.pop()
            else:
                stack.append(s)

        if len(stack) == 0:
            return "/"
        for s in stack:
            res += "/" + s
        return res

    def simplifyPath_02(self, path):
        if not path:
            return None
        p = path.split("/")
        stack, res = [], ""
        for s in p:
            if s == "." or len(s) == 0:
                continue
            elif s == "..":
                if len(stack):
                    stack.pop()
            else:
                stack.append(s)

        if len(stack) == 0:
            return "/"
        for s in stack:
            res += "/" + s
        return res

    def restoreIpAddresses(self, s):
        if len(s) < 4 or len(s) > 12:
            return []
        path, result = [], []
        dfs(s, 0, path, result)
        return result

    def restoreIpAddresses_02(self, s):
        if len(s) < 4 or len(s) > 12:
            return []
        path, result = [], []
        dfs(s, 0, path, result)
        return result
    def restoreIpAddresses_03(self,s):
        if len(s) < 4 or len(s) > 12:
            return []
        path,result =[],[]
        dfs(s,0,path,result)
        return result


def dfs(s, start, path, result):
    if len(path) == 4 and start == len(s):
        result.append(".".join(path))
        return
    for i in range(1, 4):
        if start + i <= len(s):
            number = s[start: start + i]
            if str(int(number)) == number and int(number) <= 255:
                path.append(number)
                dfs(s, start + i, path, result)
                path.pop()


def dfs_01(s, start, path, result):
    if len(path) == 4 and start == len(s):
        result.append(".".join(path))
        return
    for i in range(1, 4):
        if start + i <= len(s):
            number = s[start, start + i]
            if str(int(number)) == number and int(number) <= 255:
                path.append(number)
                dfs_01(s, start + i, path, result)
                path.pop()

def dfs_02(s,start,path,result):
    if len(path)== 4 and start == len(s):
        result.append(".".join(path))
        return 
    for i in range(len(s)):
        if start + i <= len(s):
            number = s[start: start + i]
            if str(int(number)) == number and int(number)<=255:
                path.append(number)
                dfs(s,start + i,path,result)
                path.pop()



