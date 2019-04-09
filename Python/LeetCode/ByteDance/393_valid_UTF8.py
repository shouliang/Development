''' 
UTF-8 编码验证
393. UTF-8 Validation:https://leetcode.com/problems/utf-8-validation/
'''


class Solution:
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        count = 0
        for dt in data:
            if count == 0:
                if (dt >> 5) == 0b110:  # 判断后面有几个以“10”开头的字节
                    count = 1
                elif (dt >> 4) == 0b1110:
                    count = 2
                elif (dt >> 3) == 0b11110:
                    count = 3
                elif (dt >> 7 != 0):     # 第1位不是0，则可直接判定不是UTF-8编码
                    return False
            else:
                if (dt >> 6) != 0b10:    # 判断是否以“10”开头，不是则直接返回False，否则没判断一个减少一个
                    return False
                else:
                    count = count - 1
        return count == 0                # 最后判断count是否等于0


data = [240, 162, 138, 147]
s = Solution()
flag = s.validUtf8(data)
print(flag)
