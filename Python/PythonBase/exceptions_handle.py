# 处理异常
# 至少有一个except与try相对应

try:
    text = input('Enter something -->')
except EOFError:
    print('why did you do an EOF on me')
except KeyboardInterrupt:
    print('You cancelled the operation')
else:
    print('You entered {}'.format(text))
