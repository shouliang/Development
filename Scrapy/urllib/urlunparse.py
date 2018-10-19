from urllib.parse import urlunparse

# urlunparse来构造链接
# 参数为一个可迭代的对象，但是长度必须为6，否则会参数不足的错误
data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']

print(urlunparse(data))
