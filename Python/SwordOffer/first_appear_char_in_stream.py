
class Solution:
    def __init__(self):
        self.charlist =[]
    # 返回对应char
    def FirstAppearingOnce(self):
         for key in self.charlist:
             if self.charlist.count(key) == 1:
                 return key
         return '#'
    def Insert(self, char):
        self.charlist.append(char)

s = Solution()
s.Insert('g')
s.Insert('o')

print(s.FirstAppearingOnce())

s.Insert('o')
s.Insert('g')
s.Insert('l')
s.Insert('e')

print(s.FirstAppearingOnce())