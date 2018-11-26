'''
题目描述
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
'''
class Solution:
    def FirstNotRepeatingChar(self, s):
        if not s:
            return -1
        slist = list(s)
        hashmap = dict()

        # python2中通过不了，是因为dic()里面是乱序的，而python3可以通过
        for char in slist:
            if char in hashmap:
                hashmap[char] += 1
            else:
                print(char)
                hashmap[char] = 1

        for char in hashmap:
            if hashmap[char] == 1:
                return slist.index(char)


s = 'google'
sol = Solution()
print(sol.FirstNotRepeatingChar(s))
