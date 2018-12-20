# name = input("What's your name")
# sum = 100 + 100
# print('hello,%s'%name)
# print('sum = %d'%sum)

# range使用，此例中求0-10的和，不包括11
sum = 0
for number in range(11):
    sum += number
print(sum)

# while循环适合循环次数不确定的循环
sum, number = 0, 1
while number < 11:
    sum += number
    number += 1
print(sum)

# 列表：相当于数组，具有怎删改查的功能
lists = ['a', 'b', 'c']
lists.append('d')
print(lists)

lists.insert(0, 'mm')
print(lists)

lists.pop()
print(lists)

# 元组：一旦初始化就不能修改
tuples = ('tupleA', 'tupleB')
print(tuples[0])

# 字典：key:value的形式
score = {'zhangsan': 95, 'lisi': 89}

score['wangwu'] = 98
print(score)

score.pop('zhangsan')
print(score)

print('zhangsan' in score)
print('lisi' in score)

print(score.get('lisi'))
print(score.get('lisi_02', 99))
print(score)

# 集合set,最重要的功能是去重
s = set(['a', 'a', 'b', 'c'])
print(s)
s.add('b')
print(s)
print('c' in s)
print('d' in s)
