# coding=utf-8
import requests

# 响应
r = requests.get('http://www.jianshu.com')

# requests提供了一个内置的状态码查询对象：requests.codes
print(type(r.status_code), r.status_code)
print(type(r.headers), r.headers)
print(type(r.cookies), r.cookies)
print(type(r.url), r.url)
print(type(r.history), r.history)