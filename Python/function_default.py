# 函数参数times默认为1
# 只有那些位于参数列表末尾的参数才能被赋予默认参数值
def say(message, times = 1):
    print(message * times)

say('Hello')
say('World', 5)