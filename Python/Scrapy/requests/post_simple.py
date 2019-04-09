# coding=utf-8
import requests

# POST data,在data参数中可直接赋予字典形式的参数
data = {
    'name': 'germey',
    'age': 22
}
r = requests.post('http://httpbin.org/post', data=data)
print(r.text)
