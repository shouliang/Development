print('Simple Assignment')
shoplist =['apple', 'mango', 'carrot', 'banana']

# 列表的赋值不会创建一个副本，必须使用切片操作来生成一份序列的副本
mylist = shoplist
del shoplist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)

print('Copy by making a full slice')
mylist = shoplist[:]
del mylist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)