# 序列的主要功能是资格测试，即：in与not in表达式和索引操作
# 列表，元组，字符串都拥有切片运算符
shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

# 索引或者下标操作符
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])

# 负数表示倒数第几
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])

print('Character 0 is', name[0])

# 切片 on list,包括其实位置，但不包括介绍位置
print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])

# 切片 on string
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])

# 第三个参数为步长，默认为1
print(shoplist[::2])
print(shoplist[::3])
print(shoplist[::-1])
