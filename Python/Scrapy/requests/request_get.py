import requests

r = requests.get('http://httpbin.org/get')
print(r.text)
print(type(r.text))

# json()方法可以直接解析返回结果得到一个字典
print(r.json())
print(type(r.json()))

# 利用params参数直接通过字典构造参数
print('--------------------')
data = {
    'name': 'germey',
    'age': 22
}
r = requests.get('http://httpbin.org/get', params=data)
print(r.text)
