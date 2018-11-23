# coding=utf-8
''''
题目描述
牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。
同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。例如，“student. a am I”。
后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。
Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？

思路：先翻转整个句子，再单独翻转每个单词
'''
class Solution:
    def ReverseSentence(self, s):
        if not s:
            return s
        s = list(s)
        self.rerverse(s, 0, len(s) - 1)
        # 定义两个指针，用于翻转单词
        start, end = 0, 0
        while start < len(s):
            if end == len(s) or s[end] == ' ':
                self.rerverse(s, start, end - 1)
                end += 1
                start = end
            else:
                end += 1

        return "".join(s)

    def rerverse(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1


s = 'I am a student.'

solution = Solution()
print(solution.ReverseSentence(s))
