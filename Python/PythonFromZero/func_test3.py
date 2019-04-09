# a * x  + b = y

# def a_line(a, b):
#     def arg_y(x):
#         return a * x + b
#
#     return arg_y


def a_line(a, b):
    return lambda x: a * x + b


line1 = a_line(3, 5)
print(line1(10))
print(line1(20))

line2 = a_line(5, 10)

# 对比 def_func1(a,b,x)
