# coding=utf-8
# 字符串是不可变的
# 一串字符串是字符的序列
age = 20
name = 'Swaroop'

# 索引是从0开始计数，以此类推
print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))

# 索引是一个可选项
print('{} was {} years old when he wrote this book'.format(name, age))
print('Why is {} playing with that python?'.format(name))

# 保留浮点数小数点后三位
print('{0:.3f}'.format(1.0/3))

# 使用下划线填充文本
# 使用(^)定义字符串长度为11
print('{0:_^11}'.format('hello'))

# 基于关键词输出
print('{name} wrote {book}'.format(name = 'Swaroop', book = 'A Byte of Python'))

# print 总会以一个不可见的"新一行"字符(\n)来结尾，防止它可通过end指定特定的字符
print('a', end = '')
print('b', end = '')

print()

print('a', end= ' ')
print('b', end= ' ')
print('c')

# 转义字符，需要加反斜杠(\)
print('what\'s your name')

# 可以在双引号中使用单引号而不需要转义
print("what's your name")

