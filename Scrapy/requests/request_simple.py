import requests

# 直接调用get方法返回，得到一个Response对象
# 然后分别输出Response的类型、状态码、响应体、cookie等
r = requests.get('https://www.baidu.com')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)