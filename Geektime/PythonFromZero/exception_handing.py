# throw NameError
# i = j

# SyntaxError
# print(()

# IndexError
# a = '123'
# print(a[3])

# KeyError
# d = {'a': 1, 'b': 2}
# print(d['c'])

# ValueError: 例如输入一个字母，不能转换成 int
# year = int(input('input year:'))

# try:
#     year = int(input('input year:'))
# except ValueError:
#     print('年份要输入数字')

# AttributeError
# a =123
# a.append()

# 捕获多异常
# except (ValueError,AttributeError,KeyError)

try:
    print(1 / 0)
except ZeroDivisionError as e:
    print('0不能做除数 %s' % e)

try:
    a.append()
except Exception as e:
    print(' %s' % e)

try:
    raise NameError('helloError')
except NameError:
    print('my custom error')

try:
    a = open('name.txt')
except Exception as e:
    print(e)
finally:
    a.close()