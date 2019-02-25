from pandas import Series,DataFrame

obj = Series([4,5,6,-7])

print(obj)

print(obj.index)

print(obj.values)

# TypeError: unhashable type: 'list'
# {['a']:6}