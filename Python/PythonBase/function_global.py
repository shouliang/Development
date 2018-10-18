x = 50


def func():
    global x # global声明一个全局变量，改变后会影响到主代码块中的x的值

    print('x is', x)
    x = 2
    print('Changed global x to', x)


func()
print('Value of x is', x)
