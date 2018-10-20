from urllib.parse import urlparse

# 解析链接
# 返回6个部分：schema://netloc/path;params?query?#fragment
# 返回结果ParseResult实际上是一个元组，可以通过索引顺序来获取
result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result)

print('---------------')

# 解析链接： 知道scheme
result = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
print(result)

print('---------------')
result = urlparse('www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)
print(result)

print('---------------')
result = urlparse('www.baidu.com/index.html#comment', allow_fragments=False)
print(result)