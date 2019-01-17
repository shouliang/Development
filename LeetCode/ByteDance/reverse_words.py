''' 
翻转字符串里的单词
给定一个字符串，逐个翻转字符串中的每个单词。

示例:  
输入: "the sky is blue",
输出: "blue is sky the".
说明:

无空格字符构成一个单词。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
进阶: 请选用C语言的用户尝试使用 O(1) 空间复杂度的原地解法。

思路：先翻转整个句子，再单独翻转每个单词

'''


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 去掉字符串s中多余的空格，只保留单词之间的一个空格
        # 以空格' '分割字符串，再去掉所有空格，最后再以空格' 'join各个单词
        s_array = s.split(' ')
        s_new = []
        for stri in s_array:
            if stri != '':
                s_new.append(stri)
        s = ' '.join(s_new)

        s = list(s)
        reverseStr(s, 0, len(s) - 1)
        # 定义两个指针，用于翻转单词
        start, end = 0, 0
        while start < len(s):
            if end == len(s) or s[end] == ' ':  # 后面一个指针遇到空格或者到数组的最后，则翻转单词
                reverseStr(s, start, end - 1)
                end += 1    # end指向空格的下一个，重新开始一个新单词
                start = end  # 此时start也指向新单词的开始
            else:
                end += 1

        return "".join(s)

# 翻转字符串
def reverseStr(s, start, end):
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1


 


s = "   the sky is blue   "
s_array = s.split(' ')
# print(s_array)

ss = []
for i in s_array:
    if i != '':
        ss.append(i)

print(" ".join(ss))
