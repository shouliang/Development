# coding=utf-8

# range()返回一个可迭代对象，
# range(start,stop[, step])
#   start:默认0
#   end：计数到stop结束，但是不包括stop
#   step：默认1

# list()函数是对象迭代器，可以把range()返回的可迭代对象转为一个列表

for i in range(5):
    print(i)

print('----------')

r1 = list(range(5))
print(r1)

r2 = list(range(0, 10, 2))
print(r2)

r3 = list(range(0, 11, 2))
print(r3)
