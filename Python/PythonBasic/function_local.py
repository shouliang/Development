x = 50


def func(x):
    print('x is', x)
    x = 2  # x是该函数内的局部变量，不会改变主代码块中的x
    print('Changed local x to', x)


func(x)
print('x is still', x)
