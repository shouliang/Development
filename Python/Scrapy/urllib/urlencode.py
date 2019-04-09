from urllib.parse import urlencode

# urlencode在构造GETQ请求参数的时候非常有用
# 声明一个字典来将参数表示出来：可以理解为序列化
params = {
    'name': 'germey',
    'age': 22
}

base_url = 'http://www.baidu.com?'
url = base_url + urlencode(params)
print(url)
