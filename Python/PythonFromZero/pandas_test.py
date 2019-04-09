from pandas import Series, DataFrame

obj = Series([4, 5, 6, -7])

# print(obj)
#
# print(obj.index)
#
# print(obj.values)
#
# # TypeError: unhashable type: 'list'
# # {['a']:6}

# 指定索引
# obj2 = Series([4, 5, 6, -7], index=['d', 'b', 'c', 'a'])
#
# print(obj2)
#
# obj2['c'] = 99
#
# print(obj2)
#
# print('f' in obj2)
#
# # 字典转换成Series
# sdata = {'beijing': 35000, 'shanghai': 71000, 'guangzhou': 16000, 'shenzhen': 50000}
# obj3 = Series(sdata)
# print(obj3)
#
# # 修改索引
# obj3.index = ['bj', 'sh', 'gz', 'sz']
# print(obj3)

# DataFrame类似电子表格
data = {'city': ['shanghai', 'shanghai', 'shanghai', 'beijing', 'beijing'],
        'year': [2016, 2017, 2018, 2017, 2018],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]
        }
frame = DataFrame(data)
frame2 = DataFrame(data, columns=['year', 'city', 'pop'])
# print(frame)
# print(frame2)

# 二维转换为一维
# print(frame2['city'])
# print(frame2.year)

# 新增一列
frame2['new'] = 100
print(frame2)

frame2['cap'] = frame2.city == 'beijing'
print(frame2)

# 字典的嵌套
pop = {
    'beijing': {2008: 1.5, 2009: 2.0},
    'shanghai': {2008: 2.0, 2009: 3.6},
}
frame3 = DataFrame(pop)
print(frame3)
print(frame3.T)  # 行列转置

obj4 = Series([4.5, 7.2, -5.3, 3.6], index=['b', 'd', 'c', 'a'])
obj5 = obj4.reindex(['a', 'b', 'c', 'd', 'e'])
print(obj5)

# 填充默认值
obj5 = obj4.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)
print(obj5)

obj6 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
print(obj6.reindex(range(6)))
print(obj6.reindex(range(6), method='ffill'))  # 用前面的值填充

# 删除缺失值
from numpy import nan as NA

data = Series([1, NA, 2])
print(data)
print(data.dropna())

data2 = DataFrame([
    [1, 6.5, 3],
    [1, NA, NA],
    [NA, NA, NA],
])
print(data2.dropna())
print(data2.dropna(how='all'))  # 删除缺失值全是na的行

# 层次化索引
import numpy as np

data3 = Series(np.random.randn(10),
               index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
                      [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
print(data3)
# 根据索引层次提取
print(data3['b'])
print(data3['b':'c'])

# unstack转换为二维数据
print(data3.unstack())
print(data3.stack())
