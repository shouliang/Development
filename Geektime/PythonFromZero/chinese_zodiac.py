# 记录生肖，根据年份来判断生肖

# chinese_zodiac = '鼠牛虎兔龙蛇马羊猴鸡狗猪'

# print(chinese_zodiac[0])
# print(chinese_zodiac[0:4])
# print(chinese_zodiac[-1])

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
year = 2018
print(year % 12)
print(chinese_zodiac[year % 12])

# 成员关系
print('狗' in chinese_zodiac)
print('狗' not in chinese_zodiac)

# 连接关系
print(chinese_zodiac + chinese_zodiac)
print(chinese_zodiac + 'abcd')

# 重复操作符
print(chinese_zodiac * 3)
