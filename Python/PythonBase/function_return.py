def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The number are equal'
    else:
        return y

print(maximum(2, 3))

# 每一个函数末尾都隐含一句 return None,除非你写了自己的 return 语句
def some_function():
    pass

print(some_function())
