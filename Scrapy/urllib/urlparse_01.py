from urllib.parse import urlparse

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result)

print('---------------')

result = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
print(result)

print('---------------')
result = urlparse('www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)
print(result)

print('---------------')
result = urlparse('www.baidu.com/index.html#comment', allow_fragments=False)
print(result)