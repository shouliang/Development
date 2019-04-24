'''
计算逆波兰式
150. Evaluate Reverse Polish Notation:https://leetcode.com/problems/evaluate-reverse-polish-notation/
思路 ： 双指针，存在环：则快慢指针肯定相遇，不存在环：快指针能到达表尾
基本思路
什么是逆波兰表达式？其实就是后缀表达式！！！你又问了，什么是后缀表达式呢？你数据结构一定都忘光了！！！

后缀表达式就是把操作数放前面，把操作符后置的一种写法，我们通过观察可以发现，第一个出现的运算符，
其前面必有两个数字，当这个运算符和之前两个数字完成运算后从原数组中删去，把得到一个新的数字插入到原来的位置，
继续做相同运算，直至整个数组变为一个数字。

此题其实是栈的完美应用

从前往后遍历数组，遇到数字则压入栈中，遇到符号，则把栈顶的两个数字拿出来运算，把结果再压入栈中，
直到遍历完整个数组，栈顶数字即为最终答案。

注意⚠️：

这里的除法操作是针对整数的，会对结果进行去尾操作。
对负数与整数的除法操作也与Python自带的计算方式不同，Python计算-1//2结果为-1，
而在这里应该为0，所以要进行特殊的处理。

参考：https://blog.csdn.net/alicelmx/article/details/83096865 

'''

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token not in ("+", "-", "*", "/"):
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if token == '+':
                    res = num1 + num2
                elif token == '-':
                    res = num1 - num2
                elif token == '*':
                    res = num1 * num2
                else:
                    # 除法是针对Python语言有特殊处理，其他语言大多数直接是 res = num1 // num2 即可
                    if num1*num2 < 0:
                        res = -(abs(num1)//abs(num2))
                    else:
                        res = num1 // num2
                stack.append(res)
        return stack.pop()
    

tokens = ["2","1","+","3","*"]
tokens = ["0","3","/"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

s = Solution()
num = s.evalRPN(tokens)
print(num)
