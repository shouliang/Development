# 带参数的函数装饰器

# def tips(func):
#     def nei(a, b):
#         print('start')
#         func(a, b)
#         print('end')
#
#     return nei
#
#
# @tips
# def add(a, b):
#     print(a + b)
#
#
# @tips
# def sub(a, b):
#     print(a - b)
#
#
# add(2, 4)
# sub(4, 1)

# 再套上一层函数，就可以实现装饰器带参数
def new_tips(argv):
    def tips(func):
        def nei(a, b):
            print('start %s' % argv)
            print('function name is %s' % func.__name__)
            func(a, b)
            print('end')

        return nei

    return tips


@new_tips('def_add')
def add(a, b):
    print(a + b)


@new_tips('def_sub')
def sub(a, b):
    print(a - b)


add(2, 4)
sub(4, 1)
