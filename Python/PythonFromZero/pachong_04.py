import requests

# get请求
url = 'http://httpbin.org/get'
data = {'key': 'value', 'abc': 'xyz'}
response = requests.get(url, data)
print(response.text)

# post请求
url = 'http://httpbin.org/post'
data = {'key': 'value', 'abc': 'xyz'}
response = requests.post(url, data)
# 返回类型可以设置为json
print(response.json())
