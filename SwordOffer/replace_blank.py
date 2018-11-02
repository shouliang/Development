# 替换字符串中的空格为%20
class Solution:
    def replace(self, s):
        if not isinstance(s, str) or not len(s) or not s:
            return ''
        # 统计空格数量
        numberOfBlank = 0
        for i in s:
            if i == ' ':
                numberOfBlank += 1

        # 计算新的字符串的末尾位置
        originalLength = len(s)
        newLength = originalLength + numberOfBlank * 2
        # 此处因用python生成了一个新的字符串并初始化
        newStr = newLength * [None]

        indexOfOriginal = originalLength - 1
        indexOfNew = newLength - 1

        # 循环：遇到空格和非空格的处理方式
        while indexOfOriginal >= 0 and indexOfNew >= indexOfOriginal:
            if s[indexOfOriginal] == ' ':
                newStr[indexOfNew - 2:indexOfNew + 1] = ['%', '2', '0']
                indexOfNew -= 3
                indexOfOriginal -= 1
            else:
                newStr[indexOfNew] = s[indexOfOriginal]
                indexOfNew -= 1
                indexOfOriginal -= 1

        return ''.join(newStr)


solution = Solution()
s = 'We are Happy'
print(solution.replace(s))
