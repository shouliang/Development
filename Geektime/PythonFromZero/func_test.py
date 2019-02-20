# print('abc', end='\n\n')
# print('abc', end='\n\n')
#
#
# def func(a, b, c):
#     print('a = %s' % a)
#     print('b = %s' % b)
#     print('c = %s' % c)
#
#
# func(1, 2, 3)
#
# # 关键字参数可以忽略参数顺序
# func(1, c=3, b=2)


# 可变长参数
# def howlong(first, *other):
#     print(1 + len(other))
#
#
# howlong(3)
# howlong(3, 4)
# howlong(3, 4, 5)

# -------------

# var1 = 123
#
#
# def func_1():
#     var1 = 456
#     print(var1)
#
#
# def func_2():
#     global var1
#     var1 = 789
#     print(var1)
#
#
# func_1()
# print(var1)
# func_2()

# -------------
# 迭代器
# list1 = [1, 2, 3]
# it = iter(list1)
# print(next(it))
# print(next(it))
# print(next(it))
# # print(next(it)) 报错

# for i in range(10, 20, 2):
#     print(i)

# range中步长不能是小数
# for i in range(10,20,0.5):
#     print(i)

# 自定义生成器，结合yield
# def frange(start, stop, step):
#     x = start
#     while x < stop:
#         yield x  # 特别要主要此处的yield
#         x += step
#
#
# for i in frange(10, 20, 0.5):
#     print(i)

# lambda
# def truee():
#     return True
#
# lambda: True

# lamdba表达式与函数互相转换
# def add(x, y):
#     return x + y
# lambda x, y: x + y
#
# lambda x: x <= (month, day)
# def func1(x):
#     return x <= (month, day)


# 内置函数
# filter()  map()  reduce() zip()
# help(filter)

a = [1, 2, 3, 4, 5, 6, 7]
b = list(filter(lambda x: x > 2, a))
print(b)

# map 实现a 与 b 相加
a = [1, 2, 3]
print(list(map(lambda x: x + 1, a)))
b = [4, 5, 6]
print(list(map(lambda x, y: x + y, a, b)))

# reduce 需要引入functools
from functools import reduce

ret = reduce(lambda x, y: x + y, [2, 3, 4], 1)
print(ret)

# zip
for i in zip((1, 2, 3), (4, 5, 6)):
    print(i)

dicta = {'a': 'aa', 'b': 'bb'}
dictb = zip(dicta.values(), dicta.keys())
print(dict(dictb))
