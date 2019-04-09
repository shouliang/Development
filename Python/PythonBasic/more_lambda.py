# Lambda表达式
# lambda语句可以传递一个新的函数对象
# 从本质上说，lambda需要一个参数，后跟一个表达式作为函数体，表达式的值作为新函数的返回值
points = [{'x': 2, 'y': 3},
          {'x': 4, 'y': 1}]

points.sort(key=lambda i: i['y'])
print(points)
