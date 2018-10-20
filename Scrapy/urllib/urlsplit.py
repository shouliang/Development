from urllib.parse import urlsplit

# 只返回5个结果，params会合并到path中
# 返回结果是SplitResult,其实也是一个元组
# 可以通过属性值或者索引获取值
result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result)
print(result[0])
