from urllib.parse import urlunsplit

# 传入一个含5个参数且可迭代的对象：列表或者元组，来构造一个完整的链接
data = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']
print(urlunsplit(data))
