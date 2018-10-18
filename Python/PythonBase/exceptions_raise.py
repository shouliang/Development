# coding=utf-8
# 抛出异常
class ShortInputException(Exception):
    '''一个由用户定义的异常类'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


try:
    text = input('Enter something -->')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
except EOFError:
    print('why did you do an EOF on me')
except ShortInputException as ex:
    print('ShortInputException: The input was {} long, expected at least {}'.format(ex.length, ex.atleast))
else:
    print('No exception was raised')
